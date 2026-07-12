from enum import Enum


class IntentType(str, Enum):
    CHAT = "chat"
    EXECUTE = "execute"
    SYSTEM = "system"
    FILE = "file"


class Planner:

    def classify(self, prompt: str):

        text = prompt.lower()

        execute_words = [
            "open",
            "launch",
            "run",
            "install",
            "close",
            "delete",
            "shutdown",
            "restart"
        ]

        system_words = [
            "cpu",
            "ram",
            "memory",
            "system",
            "battery",
            "storage",
            "disk"
        ]

        file_words = [
            "find",
            "search",
            "locate",
            "file",
            "folder"
        ]

        if any(word in text for word in execute_words):
            return IntentType.EXECUTE

        if any(word in text for word in system_words):
            return IntentType.SYSTEM

        if any(word in text for word in file_words):
            return IntentType.FILE

        return IntentType.CHAT