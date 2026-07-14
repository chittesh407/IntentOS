import psutil

from app.agent.context import AgentContext


class Verifier:

    def verify(self, context: AgentContext):

        print("[Verifier] Verifying execution...")

        if context.execution_status != "SUCCESS":
            context.verified = False
            return context

        if context.resolved_type == "application":

            expected = context.resolved_value.lower()

            for process in psutil.process_iter(["name"]):

                try:

                    name = process.info["name"]

                    if name and expected in name.lower():
                        context.verified = True
                        return context

                except Exception:
                    pass

        context.verified = False

        return context