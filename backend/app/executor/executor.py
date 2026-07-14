import subprocess

from app.agent.context import AgentContext


class Executor:

    def execute(self, context: AgentContext):

        print("[Executor] Executing...")

        if context.resolved_type != "application":
            context.execution_status = "FAILED"
            context.response = "Unsupported target."
            return context

        try:
            subprocess.Popen(context.resolved_value)

            context.execution_status = "SUCCESS"
            context.response = (
                f"Opened {context.target} successfully."
            )

        except Exception as e:
            context.execution_status = "FAILED"
            context.response = str(e)

        return context