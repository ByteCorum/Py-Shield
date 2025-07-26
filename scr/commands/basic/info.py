from utils.logger import Log,Fore
import config as cfg

def Info():
    if cfg.Info.options["--all"]:
        Log.Custom(f"\n{cfg.NAME} version {cfg.VERSION}\nby {cfg.AUTHOR}\n{cfg.DESCRIPTION}\nRepo: {Fore.BLUE if Log.colored else ""}{cfg.URL}{Fore.RESET}")

    elif cfg.Info.options["--version"]:
        Log.Custom(f"\n{cfg.NAME} version {cfg.VERSION}")

    elif cfg.Info.options["--url"]:
        Log.Custom(f"\nRepo: {Fore.BLUE if Log.colored else ""}{cfg.URL}{Fore.RESET}")

    elif cfg.Info.options["--description"]:
        Log.Custom(f"\n{cfg.DESCRIPTION}")
