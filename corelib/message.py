from dataclasses import dataclass, field
from time import time
import uuid


@dataclass
class Message:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    type: str = ""
    source: str = ""
    target: str = ""
    payload: dict = field(default_factory=dict)
    timestamp: float = field(default_factory=time)

    def to_dict(self):
        return {
            "id": self.id,
            "type": self.type,
            "source": self.source,
            "target": self.target,
            "payload": self.payload,
            "timestamp": self.timestamp,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data.get("id", str(uuid.uuid4())),
            type=data.get("type", ""),
            source=data.get("source", ""),
            target=data.get("target", ""),
            payload=data.get("payload", {}),
            timestamp=data.get("timestamp", time()),
        )