"""Simple protocol gateway placeholder."""

from typing import Any


class ProtocolGateway:
    """Placeholder for protocol conversion layer."""

    def __init__(self) -> None:
        self.handlers = {}

    def register_handler(self, protocol: str, handler: Any) -> None:
        self.handlers[protocol] = handler

    def convert(self, protocol: str, data: Any) -> Any:
        handler = self.handlers.get(protocol)
        if handler is None:
            raise ValueError(f"Unsupported protocol: {protocol}")
        return handler(data)
