from os import system
from utils.logger import Log
from config import Command


def DependenciesHandler(this: Command):
    dependencies = ["cryptography", "pycryptodome", "cython", "nuitka", "colorama"]

    if this.options["--show"]:
        string = ""
        for dep in dependencies:
            string+=f"\n  {dep}"
        Log.Custom(f"Project's dependencies:{string}")

    if this.options["--install"]:
        for dep in dependencies:
            system(f"pip install {f" --log {Log.logFile}" if Log.logFile else ""}{ "--quiet" if Log.quiet else ""}{ "--no-input" if Log.noInput else ""} {dep}")

    if this.options["--uninstall"]:
        for dep in dependencies:
            system(f"pip uninstall {f" --log {Log.logFile}" if Log.logFile else ""}{ "--quiet" if Log.quiet else ""}{ "--no-input" if Log.noInput else ""} {dep}")

    if this.options["--update"]:
        for dep in dependencies:
            system(f"pip install --upgrade {f" --log {Log.logFile}" if Log.logFile else ""}{ "--quiet" if Log.quiet else ""}{ "--no-input" if Log.noInput else ""} {dep}")