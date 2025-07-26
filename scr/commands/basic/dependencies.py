from utils.logger import Log, Fore
from config import Command


def DependenciesHandler(this: Command):
    if this.options["--all"]:
        Log.Custom(f"")