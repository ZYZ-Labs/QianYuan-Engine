"""Simple intelligent coordinator prototype."""

from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any, Dict, List
import time

from .models import Task


class TaskDetail(BaseModel):
    task_type: str
    parameters: Dict[str, Any] = {}


class DispatchRequest(BaseModel):
    task_details: TaskDetail


def create_app() -> FastAPI:
    app = FastAPI(title="QianYuan Coordinator")
    coordinator = Coordinator()

    @app.post("/dispatch_task")
    def dispatch_task(req: DispatchRequest):
        task_type = req.task_details.task_type
        params = req.task_details.parameters
        task = coordinator.dispatch_task(task_type, params)
        return {
            "status": "success",
            "data": {"task_id": task.id, "timestamp": int(time.time())},
            "message": "Task dispatched successfully.",
        }

    @app.get("/system_status")
    def system_status():
        return {
            "status": "success",
            "data": coordinator.status(),
            "message": "",
        }

    @app.put("/update_config")
    def update_config(cfg: Dict[str, int]):
        coordinator.update_config(cfg)
        return {"status": "success", "data": {}, "message": "Configuration updated."}

    return app


class Coordinator:
    """In-memory task coordinator."""

    def __init__(self) -> None:
        self.tasks: List[Task] = []
        self.config: Dict[str, int] = {
            "max_task_timeout": 5000,
            "retry_attempts": 3,
        }

    def dispatch_task(self, task_type: str, parameters: Dict) -> Task:
        task = Task(task_type=task_type, parameters=parameters)
        self.tasks.append(task)
        return task

    def status(self) -> Dict[str, int]:
        return {
            "connected_devices": 0,
            "average_cpu_usage": 0.0,
            "average_mem_usage": 0.0,
            "pending_tasks": len(self.tasks),
        }

    def update_config(self, config: Dict[str, int]) -> None:
        self.config.update(config)
