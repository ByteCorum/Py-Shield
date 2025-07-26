from utils.logger import Log, Fore
from config import Command, NAME, VERSION, AUTHOR, URL, DESCRIPTION

def InfoHandler(this: Command):
    if this.options["--all"]:
        Log.Custom(f"\n{NAME} version {VERSION}\nby {AUTHOR}\n{DESCRIPTION}\nRepo: {Fore.BLUE if Log.colored else ""}{URL}{Fore.RESET}")

    elif this.options["--version"]:
        Log.Custom(f"\n{NAME} version {VERSION}")

    elif this.options["--url"]:
        Log.Custom(f"\nRepo: {Fore.BLUE if Log.colored else ""}{URL}{Fore.RESET}")

    elif this.options["--description"]:
        Log.Custom(f"\n{DESCRIPTION}")
