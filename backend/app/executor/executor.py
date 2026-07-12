import subprocess

from app.executor.apps import APPLICATIONS


class Executor:

    def execute(self, command: str):

        command = command.lower()

        for app_name, executable in APPLICATIONS.items():

            if app_name in command:

                try:
                    subprocess.Popen(executable)

                    return f"✅ {app_name.title()} opened successfully."

                except Exception as e:
                    return f"❌ {e}"

        return "❌ Application not supported yet"