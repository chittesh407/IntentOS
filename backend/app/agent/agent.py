from app.planner.llm_planner import LLMPlanner
from app.memory.memory import Memory
from app.agent.context import AgentContext
from app.resolver.resolver import Resolver
from app.risk.risk import RiskEngine
from app.executor.executor import Executor
from app.verifier.verifier import Verifier


class Agent:

    def __init__(self):
        self.memory = Memory()
        self.planner = LLMPlanner()
        self.resolver = Resolver()
        self.risk = RiskEngine()
        self.executor = Executor()
        self.verifier = Verifier()
    def handle(self, message: str):

        context = AgentContext(
            user_input=message
        )

        context = self.memory.retrieve(context)

        plan = self.planner.plan(message)

        context.intent = plan["intent"]
        context.target = plan["target"]
        context = self.resolver.resolve(context)
        context = self.risk.evaluate(context)
        if not context.confirmation_required:
            context = self.executor.execute(context)
            context = self.verifier.verify(context)
        else:
            context.response = (
                f"{context.risk} risk detected. "
                "Confirmation required before execution."
            )


        context = self.memory.store(context)

        return context.model_dump()