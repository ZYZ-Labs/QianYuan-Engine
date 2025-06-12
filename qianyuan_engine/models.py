from dataclasses import dataclass, field
from typing import Any, Dict
import uuid


@dataclass
class Task:
    """Simple task representation."""

    task_type: str
    parameters: Dict[str, Any]
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
