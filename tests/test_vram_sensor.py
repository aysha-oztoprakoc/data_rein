from reins.harness import vram_sensor


def test_query_free_vram_degrades_when_no_vendor_tool(monkeypatch):
    monkeypatch.setattr(vram_sensor.shutil, "which", lambda _name: None)
    assert vram_sensor.query_free_vram_gb() is None


def test_nvidia_free_memory_is_converted_to_gib(monkeypatch):
    monkeypatch.setattr(vram_sensor.shutil, "which", lambda name: "/usr/bin/nvidia-smi" if name == "nvidia-smi" else None)
    monkeypatch.setattr(vram_sensor.external_io, "run", lambda *args, **kwargs: type("R", (), {"stdout": str(4 * 1024**3)})())
    assert vram_sensor.query_free_vram_gb() == 4.0
