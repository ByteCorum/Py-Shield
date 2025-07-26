from sys import argv, exit
from inspect import isclass, isabstract
from utils.optionsParser import OptionsParser
from utils.logger import Log
from config import Command, NAME
import commands.commands as cmds


class PyShield:
    def __init__(self):
        self.command = None
        self.commandName = ""
        self.noOptions = False
        self.ParseArgs()
        self.SetGlobalVars()
        self.RunCommand()

    def ParseArgs(self):
        commands = []
        for cmdName in dir(cmds):
            cmd = getattr(cmds, cmdName)
            if isclass(cmd) and not isabstract(cmd) and issubclass(cmd, Command) and cmd.__name__ != 'Command':
                commands.append(cmdName.lower())

        try:
            if len(argv) < 2:
                raise Exception("missing command name.")

            if argv[1] not in commands:
                raise Exception(f"invalid command name: \"{argv[1]}\".")
        
        except Exception as error:
            cmds.Help.handler(cmds.Help)
            Log.Fail("Command parsing failed: "+str(error), True)
        
        self.commandName = argv[1]
        try:
            self.command: Command = getattr(cmds, self.commandName.title())
            if not self.command.options:
                self.noOptions = True
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
        if self.noOptions:
            return

        if "--log" in self.command.options:
            Log.logFile = self.command.options["--log"]
        
        if "--quiet" in self.command.options:
            Log.quiet = self.command.options["--quiet"]
        
        if "--no-color" in self.command.options:
            Log.colored = not self.command.options["--no-color"]
        
        if "--no-input" in self.command.options:
            Log.noInput = self.command.options["--no-input"]

    def RunCommand(self):
        Log.Info(f"{NAME}\n", True)
        try:
            self.command.handler(self.command)
            Log.Success(f"\n{self.commandName.title()} successfully completed.")
        except Exception as error:
            Log.Fail(f"{self.commandName.title()} failed: {error}", True)