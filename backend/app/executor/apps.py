import os

APPLICATIONS = {
    "notepad": "notepad",
    "calculator": "calc",
    "paint": "mspaint",
    "cmd": "cmd",
    "explorer": "explorer",

    "vs code": os.path.expandvars(
        r"%LOCALAPPDATA%\Programs\Microsoft VS Code\Code.exe"
    ),
    "visual studio code": os.path.expandvars(
        r"%LOCALAPPDATA%\Programs\Microsoft VS Code\Code.exe"
    ),

    "chrome": "chrome",
}