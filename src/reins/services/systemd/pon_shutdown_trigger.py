from typing import Any
import sys
import json
import threading
import time

try:
    from paho.mqtt.client import CallbackAPIVersion  # type: ignore[attr-defined]
    PAHO_V2 = True
except ImportError:
    PAHO_V2 = False
import paho.mqtt.client as mqtt

TRIGGER_TOPIC = "data_rein/backup/trigger"
RESULT_TOPIC = "data_rein/backup/result"
TIMEOUT_SEC = 300  # 5 minutes max wait

event_finished = threading.Event()
success = False


def on_connect(client: Any, userdata: Any, flags: Any, rc: int, *args: Any) -> None:
    if rc == 0:
        client.subscribe(RESULT_TOPIC)
        # Publish the trigger once subscribed
        client.publish(TRIGGER_TOPIC, json.dumps(
            {"source": "shutdown_hook", "timestamp": time.time()}))


def on_message(client: Any, userdata: Any, msg: Any) -> None:
    global success
    if msg.topic == RESULT_TOPIC:
        try:
            payload = json.loads(msg.payload.decode('utf-8'))
            if payload.get("event") == "finish":
                # Check report
                report = payload.get("report", {})
                if len(report.get("errors", [])) == 0 and report.get("success", 0) > 0:
                    success = True
                event_finished.set()
        except json.JSONDecodeError as e:
            print(f"Ignored json.JSONDecodeError: {e}")


def main() -> None:
    if PAHO_V2:
        client = mqtt.Client(CallbackAPIVersion.VERSION1)
    else:
        client = mqtt.Client(client_id="pon_shutdown_trigger")

    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect("localhost", 1883, 60)
        client.loop_start()

        # Block until finished or timeout (PON compliant wait)
        event_finished.wait(TIMEOUT_SEC)

        client.loop_stop()
        client.disconnect()

        if success:
            sys.exit(0)
        else:
            sys.exit(1)

    except Exception:
        sys.exit(1)


if __name__ == "__main__":
    main()
