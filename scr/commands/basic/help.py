from utils.logger import Log
import config as cfg

def Help(command = None):
    if not command:
        Log.Custom(cfg.Help.help)
    else:
        Log.Custom(command.help)