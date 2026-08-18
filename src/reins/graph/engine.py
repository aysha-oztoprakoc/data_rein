"""
PON-Compliant Graph Engine.

Coordinates reactive Graph Nodes via MQTT and FBE state transitions.
Enforces zero-polling, decoupled worker threads, graceful degradation,
and loop budgets.
"""
from __future__ import annotations

import json
import logging
import threading
from typing import Any, Callable, Dict, List, Optional

import paho.mqtt.client as mqtt

from reins.graph.fbe import FBEAttribute, FBEState, LoopBudget, LoopBudgetExceededError
from reins.harness import external_io
from reins.services.logger import log_degradation

logger = logging.getLogger("reins.graph.engine")


class GraphNode:
    """Base class for all reactive PON Graph Nodes."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.engine: Optional[PONGraphEngine] = None

    def bind_engine(self, engine: PONGraphEngine) -> None:
        self.engine = engine

    def handle_event(self, attribute: FBEAttribute) -> Optional[FBEAttribute]:
        """Method to be overridden by subclass nodes. Executes in detached thread."""
        raise NotImplementedError


class PONGraphEngine:
    """
    Zero-polling event-driven graph engine communicating over MQTT.
    """

    def __init__(
        self,
        broker_host: str = "127.0.0.1",
        broker_port: int = 1883,
        client_id: str = "reins_graph_engine",
        loop_budget: Optional[LoopBudget] = None,
    ) -> None:
        self.broker_host = broker_host
        self.broker_port = broker_port
        self.client_id = client_id
        self.loop_budget = loop_budget or LoopBudget(max_iterations=12)
        
        self._nodes: Dict[str, List[GraphNode]] = {}
        self._mqtt_client: Optional[mqtt.Client] = None
        self._connected = False
        self._lock = threading.Lock()

    def register_node(self, state: str | FBEState, node: GraphNode) -> None:
        """Register a node to handle transitions for a given FBEState or MQTT topic."""
        state_key = state.value if isinstance(state, FBEState) else str(state)
        node.bind_engine(self)
        with self._lock:
            if state_key not in self._nodes:
                self._nodes[state_key] = []
            self._nodes[state_key].append(node)
        
        # Subscribe if client is already running
        if self._mqtt_client and self._connected:
            self._subscribe_topic(state_key)

    def _subscribe_topic(self, topic: str) -> None:
        if self._mqtt_client:
            try:
                external_io.call(
                    "mqtt:subscribe",
                    lambda: self._mqtt_client.subscribe(topic) if self._mqtt_client else None,
                )
                logger.info("Subscribed to MQTT topic: %s", topic)
            except Exception as e:
                logger.warning("Failed to subscribe to %s: %s", topic, e, exc_info=True)
                log_degradation("reins.graph.engine.subscribe")

    def start(self) -> None:
        """Connect to MQTT broker and start non-blocking network loop."""
        try:
            # Handle paho-mqtt v1 vs v2 callback API version
            try:
                self._mqtt_client = mqtt.Client(
                    callback_api_version=mqtt.CallbackAPIVersion.VERSION2,  # type: ignore
                    client_id=self.client_id,
                )
            except (AttributeError, TypeError):
                self._mqtt_client = mqtt.Client(client_id=self.client_id)

            self._mqtt_client.on_connect = self._on_connect
            self._mqtt_client.on_message = self._on_message
            external_io.call(
                "mqtt:connect",
                lambda: self._mqtt_client.connect(self.broker_host, self.broker_port, keepalive=60) if self._mqtt_client else None,
            )
            self._mqtt_client.loop_start()
            logger.info("Graph Engine started connecting to %s:%d", self.broker_host, self.broker_port)
        except Exception as e:
            logger.warning("Failed to connect to MQTT broker (%s:%d): %s; operating offline", self.broker_host, self.broker_port, e, exc_info=True)
            log_degradation("reins.graph.engine.connect")

    def stop(self) -> None:
        """Disconnect and stop MQTT background network thread."""
        if self._mqtt_client:
            try:
                self._mqtt_client.loop_stop()
                self._mqtt_client.disconnect()
            except Exception as e:
                logger.debug("Engine stop disconnect note: %s", e, exc_info=True)
                log_degradation("reins.graph.engine.stop")
            self._connected = False

    def _on_connect(self, client: Any, userdata: Any, flags: Any, rc: Any, *args: Any) -> None:
        self._connected = True
        logger.info("Graph Engine connected to MQTT broker successfully.")
        with self._lock:
            for topic in self._nodes.keys():
                self._subscribe_topic(topic)

    def _on_message(self, client: Any, userdata: Any, msg: Any) -> None:
        topic = msg.topic
        payload_bytes = msg.payload
        try:
            attr = FBEAttribute.from_json(payload_bytes)
        except Exception as parse_err:
            logger.debug("Treating payload as raw attribute string: %s", parse_err, exc_info=True)
            log_degradation("reins.graph.engine.message_parse")
            attr = FBEAttribute(
                name=topic,
                value=payload_bytes.decode("utf-8", errors="replace"),
                task_id="anonymous",
            )

        with self._lock:
            nodes_to_run = list(self._nodes.get(topic, []))

        for node in nodes_to_run:
            threading.Thread(
                target=self._execute_node_safe,
                args=(node, attr),
                name=f"node-{node.name}-{attr.task_id}",
                daemon=True,
            ).start()

    def _execute_node_safe(self, node: GraphNode, attr: FBEAttribute) -> None:
        """Execute node with LoopBudget check and exception degradation."""
        try:
            if attr.task_id and attr.task_id != "anonymous":
                self.loop_budget.record_step(attr.task_id)
            
            result_attr = node.handle_event(attr)
            if result_attr:
                self.publish_attribute(result_attr)
        except LoopBudgetExceededError as e:
            logger.error("Loop budget exceeded for node %s on task %s: %s", node.name, attr.task_id, e)
            log_degradation(f"reins.graph.engine.loop_budget.{node.name}")
            blocked_attr = FBEAttribute(
                name=FBEState.BLOCKED.value,
                value={"error": str(e), "original_attribute": attr.name},
                task_id=attr.task_id,
            )
            self.publish_attribute(blocked_attr)
        except Exception as e:
            logger.exception("Error executing node %s: %s", node.name, e)
            log_degradation(f"reins.graph.engine.{node.name}")

    def publish_attribute(self, attribute: FBEAttribute) -> None:
        """Publish attribute state transition to MQTT and dispatch locally."""
        topic = attribute.name
        payload_str = attribute.to_json()
        
        # 1. Publish to MQTT if connected
        if self._mqtt_client and self._connected:
            try:
                external_io.call(
                    "mqtt:publish",
                    lambda: self._mqtt_client.publish(topic, payload_str) if self._mqtt_client else None,
                )
            except Exception as e:
                logger.warning("Failed to publish to MQTT topic %s: %s", topic, e, exc_info=True)
                log_degradation("reins.graph.engine.publish")

        # 2. Local dispatch if nodes are registered locally
        with self._lock:
            local_nodes = list(self._nodes.get(topic, []))
        for node in local_nodes:
            threading.Thread(
                target=self._execute_node_safe,
                args=(node, attribute),
                name=f"local-node-{node.name}-{attribute.task_id}",
                daemon=True,
            ).start()
