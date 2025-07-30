from utils.logger import Log
from config import Command

def HelpHandler(command: Command):
    Log.Custom(command.help)