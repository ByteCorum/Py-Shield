from utils.logger import Log
from utils.optionsParser import OptionsParser
import config as cfg
from sys import argv, exit

class PyShield:
    def __init__(self):
        self.command = None
        self.commandName = ""
        self.ParseArgs()
        self.SetGlobalVars()
        self.RunCommand()

    def ParseArgs(self):
        commands = [cmd.lower() for cmd in dir(cfg) if isinstance(getattr(cfg, cmd), type.__class__)]

        try:
            if len(argv) < 2:
                raise Exception("missing command name")

            if argv[1] not in commands:
                raise Exception(f"invalid command name: \"{argv[1]}\"")
        
        except Exception as error:
            cfg.Help.handler()
            Log.Fail("Command parsing failed: "+str(error), True)
        
        self.commandName = argv[1]
        try:
            self.command = getattr(cfg, self.commandName.title())
            if not hasattr(self.command, "options"):
                return

            parser = OptionsParser(argv[2:], self.command)
            parser.Parse()
            if parser.ended:
                exit(0)

            parser.Validate()
            self.command = parser.command

        except Exception as error:
            Log.Fail(f"Options parsing failed: {error}", True)
    
    def SetGlobalVars(self):
        if "--log" in self.command.options:
            Log.logFile = self.command.options["--log"]
        
        if "--quiet" in self.command.options:
            Log.quiet = self.command.options["--quiet"]
        
        if "--no-color" in self.command.options:
            Log.colored = not self.command.options["--no-color"]
        
        if "--no-input" in self.command.options:
            Log.noInput = self.command.options["--no-input"]

    def RunCommand(self):
        try:
            self.command.handler()
        except Exception as error:
            Log.Fail(f"{self.commandName} failed: {error}", True)