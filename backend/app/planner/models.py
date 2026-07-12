from enum import Enum
from pydantic import BaseModel
from typing import List


class IntentType(str, Enum):
    CHAT = "chat"
    EXECUTE = "execute"
    SYSTEM = "system"
    FILE = "file"


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Plan(BaseModel):

    intent: IntentType

    target: str

    risk: RiskLevel

    steps: List[str]