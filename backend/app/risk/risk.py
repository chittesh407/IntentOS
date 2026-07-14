from app.agent.context import AgentContext


class RiskEngine:

    LOW_RISK = [
        "open",
        "launch",
        "show",
        "display"
    ]

    MEDIUM_RISK = [
        "install",
        "download",
        "update"
    ]

    HIGH_RISK = [
        "delete",
        "remove",
        "format",
        "shutdown",
        "restart",
        "kill"
    ]

    def evaluate(self, context: AgentContext):

        print("[Risk] Evaluating...")

        text = context.user_input.lower()

        if any(word in text for word in self.HIGH_RISK):
            context.risk = "HIGH"
            context.confirmation_required = True

        elif any(word in text for word in self.MEDIUM_RISK):
            context.risk = "MEDIUM"
            context.confirmation_required = True

        else:
            context.risk = "LOW"
            context.confirmation_required = False

        return context