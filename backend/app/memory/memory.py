from app.agent.context import AgentContext


class Memory:

    def retrieve(self, context: AgentContext):
        print("[Memory] Retrieving context...")
        return context

    def store(self, context: AgentContext):
        print("[Memory] Storing context...")
        return context