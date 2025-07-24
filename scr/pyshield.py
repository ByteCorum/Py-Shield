from utils.logger import Log, Color
from config import *
from sys import argv

class PyShield:
    def __init__(self):
        ...

    def ParseArgs(self):
        try:
            if len(argv) < 2:
                Log.Custom(Help.help)

        except Exception as error:
            Log.Fail("Arguments parsing failed: "+error.__context__, True)