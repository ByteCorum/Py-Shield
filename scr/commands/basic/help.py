from utils.logger import Log
from config import Help, Command

def HelpHandler(command: Command = None):
    if not command:
        Log.Custom(Help.help)
    else:
        Log.Custom(command.help)