from utils.logger import Log, Color
from utils.optionsParser import OptionsParser
import config as cfg
from sys import argv

class PyShield:
    def __init__(self):
        self.commands = [cmd.lower() for cmd in dir(cfg) if isinstance(getattr(cfg, cmd), type.__class__)]
        self.ParseArgs()

    def ParseArgs(self):
        try:
            if len(argv) < 2:
                raise Exception("missing command name")

            if argv[1] not in self.commands:
                raise Exception(f"invalid command name: \"{argv[1]}\"")
        
        except Exception as error:
            cfg.Help.handler()
            Log.Fail("Command parsing failed: "+str(error), True)
        
        try:
            command = getattr(cfg, argv[1].title())
            if not hasattr(command, "options"):
                return

            OptionsParser(argv[2:], command).Parse()

        except Exception as error:
            if isinstance(error, ValueError):
                cfg.Help.handler()
            Log.Fail(f"Options parsing failed: {error}", True)