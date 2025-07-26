from utils.logger import Log, Fore
from config import Info, NAME, VERSION, AUTHOR, URL, DESCRIPTION

def InfoHandler():
    if Info.options["--all"]:
        Log.Custom(f"\n{NAME} version {VERSION}\nby {AUTHOR}\n{DESCRIPTION}\nRepo: {Fore.BLUE if Log.colored else ""}{URL}{Fore.RESET}")

    elif Info.options["--version"]:
        Log.Custom(f"\n{NAME} version {VERSION}")

    elif Info.options["--url"]:
        Log.Custom(f"\nRepo: {Fore.BLUE if Log.colored else ""}{URL}{Fore.RESET}")

    elif Info.options["--description"]:
        Log.Custom(f"\n{DESCRIPTION}")
