"""
Cluster Telemetry Profiler ("getinfo") for the data_rein harness.

Scans live hardware on both nodes and writes the single canonical hardware
manifest (``knowledge_base/HARDWARE.md``) plus the model registry. This is the
source of truth the Prime Directive points at, so future hardware changes flow
in automatically on the next scan instead of being hard-coded anywhere.

Node-aware VRAM detection:
* ``amdy`` (AMD RX 9060 XT) has no nvidia-smi -> read the discrete GPU's
  ``/sys/class/drm/card*/device/mem_info_vram_total`` (falls back to glxinfo).
* ``tell`` (NVIDIA GTX 1060) -> ``nvidia-smi`` over SSH.

PON-compliant: reacts to an MQTT trigger, no polling.
"""

import os
import re
import json
import glob
import threading
import subprocess
from datetime import datetime, timezone
from typing import Any, Optional

from reins.services.logger import get_logger
from reins.harness import paths

logger = get_logger("sys_profiler")


class SysProfiler:
    """Live hardware telemetry + model-fit scoring, integrated into data_rein."""

    def __init__(self, mqtt_client: Any = None) -> None:
        self.mqtt = mqtt_client
        self.registry_path = str(paths.model_registry())
        self.min_model_score = 85

        if self.mqtt is not None:
            self.mqtt.subscribe("data_rein/getinfo/trigger")
            self.mqtt.message_callback_add("data_rein/getinfo/trigger", self.on_trigger)
            # Back-compat alias.
            self.mqtt.subscribe("data_rein/sys_profiler/trigger")
            self.mqtt.message_callback_add("data_rein/sys_profiler/trigger", self.on_trigger)
        logger.info("SysProfiler (getinfo) online. Ready for cluster telemetry scans.")

    # -- trigger --------------------------------------------------------------
    def on_trigger(self, client: Any, userdata: Any, msg: Any) -> None:
        threading.Thread(target=self.profile_cluster, daemon=True).start()

    # -- probes ---------------------------------------------------------------
    def _run(self, cmd: list, host: Optional[str] = None, timeout: int = 6) -> Optional[str]:
        if host:
            cmd = ["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=3", host] + cmd
        try:
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
            if res.returncode == 0:
                return res.stdout.strip()
        except Exception:
            pass
        return None

    def get_vram(self, host: Optional[str] = None) -> float:
        """Total VRAM in GB for the node's discrete GPU. Degrades to 0.0 (unknown)."""
        if host is None:
            # amdy: AMD card, no nvidia-smi. Read the largest dGPU from sysfs.
            best_mb = 0
            for path in glob.glob("/sys/class/drm/card*/device/mem_info_vram_total"):
                try:
                    mb = int(open(path).read().strip()) / (1024 * 1024)
                    best_mb = max(best_mb, mb)
                except Exception:
                    continue
            if best_mb:
                return round(best_mb / 1024, 1)
            # Fallback: glxinfo dedicated video memory.
            out = self._run(["glxinfo"])
            if out:
                m = re.search(r"Dedicated video memory:\s*(\d+)\s*MB", out)
                if m:
                    return round(int(m.group(1)) / 1024, 1)
            return 0.0
        # remote node (tell): NVIDIA -> nvidia-smi over ssh.
        out = self._run(["nvidia-smi", "--query-gpu=memory.total", "--format=csv,noheader,nounits"], host)
        if out:
            try:
                return round(int(out.splitlines()[0].strip()) / 1024, 1)
            except Exception:
                pass
        return 0.0

    def get_ram_gb(self, host: Optional[str] = None) -> float:
        out = self._run(["cat", "/proc/meminfo"], host) if host else None
        if out is None and host is None:
            try:
                out = open("/proc/meminfo").read()
            except Exception:
                out = None
        if out:
            m = re.search(r"MemTotal:\s*(\d+)\s*kB", out)
            if m:
                return round(int(m.group(1)) / (1024 * 1024), 1)
        return 0.0

    def get_cpu(self, host: Optional[str] = None) -> dict:
        out = self._run(["lscpu"], host)
        info: dict = {}
        if out:
            for line in out.splitlines():
                if line.startswith("Model name:"):
                    info["model"] = line.split(":", 1)[1].strip()
                elif line.startswith("CPU(s):") and "NUMA" not in line:
                    info.setdefault("threads", line.split(":", 1)[1].strip())
                elif line.startswith("Core(s) per socket:"):
                    info["cores_per_socket"] = line.split(":", 1)[1].strip()
        return info

    # VRAM headroom reserved for the KV-cache / context window (GB).
    VRAM_HEADROOM_GB = 1.0

    # User-provided specs, shown when a node is unreachable at scan time.
    LAST_KNOWN = {
        "tell": {
            "vram_gb": 6.0,
            "ram_gb": 16.0,
            "cpu": {"model": "Intel Core i5 (7th gen)", "cores_per_socket": "4", "threads": "4"},
        },
    }

    def _local_model_sizes(self) -> dict:
        """Read real model weights sizes (GB) from the local Ollama manifest store.

        Works offline (no running server) by summing layer sizes in each manifest.
        """
        sizes: dict = {}
        try:
            from reins.harness import local
            store = local.model_store()
        except Exception:
            store = None
        base = (store / "manifests") if store else None
        if not base or not base.exists():
            return sizes
        for mf in base.rglob("*"):
            if not mf.is_file():
                continue
            # .../library/<name>/<tag>  ->  name:tag
            parts = mf.parts
            if "library" not in parts:
                continue
            i = parts.index("library")
            name = ":".join(parts[i + 1:])
            try:
                d = json.loads(mf.read_text())
                total = sum(l.get("size", 0) for l in d.get("layers", []))
                total += d.get("config", {}).get("size", 0)
                sizes[name] = round(total / 1e9, 1)
            except Exception:
                continue
        return sizes

    def _remote_model_sizes(self, host: str) -> dict:
        """Parse `ollama list` (NAME ... SIZE ...) over SSH into {name: size_gb}."""
        out = self._run(["ollama", "list"], host, timeout=10)
        sizes: dict = {}
        if out:
            for line in out.splitlines()[1:]:
                m = re.match(r"(\S+)\s+\S+\s+([\d.]+)\s*GB", line)
                if m:
                    sizes[m.group(1)] = float(m.group(2))
                else:
                    parts = line.split()
                    if parts:
                        sizes[parts[0]] = 0.0
        return sizes

    # -- scoring --------------------------------------------------------------
    def fits(self, size_gb: float, total_vram_gb: float) -> bool:
        if not total_vram_gb:
            return False
        if not size_gb:  # unknown size -> can't vouch it fits
            return False
        return size_gb + self.VRAM_HEADROOM_GB <= total_vram_gb

    def fit_score(self, size_gb: float, total_vram_gb: float) -> float:
        if not (total_vram_gb and size_gb):
            return 0.0
        return round(max(0.0, min(100.0, 100 * (1 - size_gb / total_vram_gb))), 1)

    def process_node(self, node_name: str, host: Optional[str] = None) -> dict:
        vram = self.get_vram(host)
        reachable = vram > 0.0 or host is None
        if reachable:
            sizes = self._local_model_sizes() if host is None else self._remote_model_sizes(host)
            hardware = {"vram_gb": vram, "ram_gb": self.get_ram_gb(host), "cpu": self.get_cpu(host)}
        else:
            # Node offline: fall back to documented last-known specs, no model scan.
            sizes = {}
            hardware = dict(self.LAST_KNOWN.get(node_name, {"vram_gb": 0.0, "ram_gb": 0.0, "cpu": {}}))
            vram = hardware.get("vram_gb", 0.0)
        fitting = []
        for name, size_gb in sorted(sizes.items()):
            if self.fits(size_gb, vram):
                fitting.append({"model": name, "size_gb": size_gb, "score": self.fit_score(size_gb, vram)})
            else:
                logger.warning(
                    f"{node_name}: {name} does NOT fit ({size_gb}GB + {self.VRAM_HEADROOM_GB}GB headroom > {vram}GB VRAM)"
                )
        return {
            "reachable": reachable,
            "hardware": hardware,
            "models_installed": sorted(sizes.keys()),
            "models_fit": fitting,
        }

    # -- manifest -------------------------------------------------------------
    def write_hardware_manifest(self, result: dict) -> None:
        """Write the single canonical HARDWARE.md and mirror a wiki memory."""
        ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
        lines = [
            "# // HARDWARE MANIFEST — data_rein",
            "",
            "> Single source of truth for cluster hardware. Auto-generated by the",
            "> `getinfo` scan (`SysProfiler`). Do not hand-edit — re-run the scan.",
            "> The Prime Directive points here so hardware changes flow in on the next scan.",
            "",
            f"**Last scan:** {ts}",
            "",
        ]
        for node in ("amdy", "tell"):
            p = result.get(node, {})
            hw = p.get("hardware", {})
            cpu = hw.get("cpu", {})
            status = "online" if p.get("reachable") else "UNREACHABLE at scan (last-known below)"
            lines += [
                f"## {node} — {status}",
                "",
                f"- **GPU VRAM:** {hw.get('vram_gb', 0.0)} GB",
                f"- **System RAM:** {hw.get('ram_gb', 0.0)} GB",
                f"- **CPU:** {cpu.get('model', 'unknown')} "
                f"({cpu.get('cores_per_socket', '?')} cores / {cpu.get('threads', '?')} threads)",
                f"- **Models fitting VRAM:** {', '.join(m['model'] for m in p.get('models_fit', [])) or '(none / node offline)'}",
                "",
            ]
        try:
            paths.hardware_manifest().write_text("\n".join(lines))
            logger.info(f"Hardware manifest written -> {paths.hardware_manifest()}")
        except Exception as e:
            logger.error(f"Could not write hardware manifest: {e}")

        # Mirror a compact fact into the shared wiki (best effort).
        try:
            from reins.harness.wiki import WikiDB
            amdy_hw = result.get("amdy", {}).get("hardware", {})
            fact = (
                f"amdy GPU VRAM is {amdy_hw.get('vram_gb')}GB (RX 9060 XT), "
                f"RAM {amdy_hw.get('ram_gb')}GB. See knowledge_base/HARDWARE.md (getinfo scan)."
            )
            with WikiDB() as db:
                db.add_memory(fact, category="system", source="getinfo", owner="data-hermes")
        except Exception as e:
            logger.warning(f"Could not mirror hardware memory into wiki: {e}")

    # -- entrypoint -----------------------------------------------------------
    def profile_cluster(self, publish: bool = True) -> dict:
        try:
            result = {
                "scanned_at": datetime.now(timezone.utc).isoformat(),
                "amdy": self.process_node("amdy"),
                "tell": self.process_node("tell", "tell"),
            }
            os.makedirs(os.path.dirname(self.registry_path), exist_ok=True)
            with open(self.registry_path, "w") as f:
                json.dump(result, f, indent=2)
            self.write_hardware_manifest(result)
            if publish and self.mqtt is not None:
                self.mqtt.publish("data_rein/getinfo/result", json.dumps({"status": "success", "registry": result}))
            logger.info("Cluster profile + hardware manifest updated.")
            return result
        except Exception as e:  # graceful degradation
            logger.error(f"Failed to profile cluster: {e}")
            if publish and self.mqtt is not None:
                self.mqtt.publish("data_rein/getinfo/result", json.dumps({"status": "error", "error": str(e)}))
            return {"status": "error", "error": str(e)}


if __name__ == "__main__":
    # Allow a one-shot local scan: `python -m reins.services.sys_profiler`
    print(json.dumps(SysProfiler().profile_cluster(publish=False), indent=2))
