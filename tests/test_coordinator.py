import sys
import os
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from qianyuan_engine.coordinator import create_app


def test_dispatch_and_status():
    app = create_app()
    client = TestClient(app)

    resp = client.post(
        "/dispatch_task",
        json={"task_details": {"task_type": "compute_square", "parameters": {"number": 2}}},
    )
    assert resp.status_code == 200
    data = resp.json()
    assert data["status"] == "success"

    status_resp = client.get("/system_status")
    assert status_resp.status_code == 200
    status_data = status_resp.json()
    assert status_data["data"]["pending_tasks"] == 1
