"""Edge device client stub."""

import requests
from typing import Dict, Any


class EdgeClient:
    """Simple client to request tasks and report status."""

    def __init__(self, coordinator_url: str) -> None:
        self.coordinator_url = coordinator_url.rstrip("/")

    def dispatch_task(self, task_type: str, params: Dict[str, Any]) -> Dict[str, Any]:
        payload = {"task_details": {"task_type": task_type, "parameters": params}}
        resp = requests.post(f"{self.coordinator_url}/dispatch_task", json=payload, timeout=5)
        return resp.json()

    def get_status(self) -> Dict[str, Any]:
        resp = requests.get(f"{self.coordinator_url}/system_status", timeout=5)
        return resp.json()
