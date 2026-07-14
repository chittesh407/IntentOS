from app.agent.context import AgentContext


APPLICATIONS = {
    "visual studio code": "code",
    "vs code": "code",
    "vscode": "code",

    "notepad": "notepad",
    "calculator": "calc",
    "paint": "mspaint",

    "command prompt": "cmd",
    "cmd": "cmd",

    "file explorer": "explorer",
    "explorer": "explorer",
}


class Resolver:

    def resolve(self, context: AgentContext):

        print("[Resolver] Resolving target...")

        target = context.target.lower()

        for app, command in APPLICATIONS.items():

            if app == target:

                context.resolved_type = "application"

                context.resolved_value = command

                return context

        return context