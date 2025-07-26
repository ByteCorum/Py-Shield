from utils.logger import Log, Fore
from config import Dependencies


def DependenciesHandler():
    if Dependencies.options["--all"]:
        Log.Custom(f"")