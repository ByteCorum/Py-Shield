from sys import argv, exit
from os import walk
from inspect import isclass, isabstract
from utils.optionsParser import OptionsParser
from utils.logger import Log
from config import Command, NAME
from commands.basic.help import Help


class PyShield:
    class CommandReference:
        def __init__(self, path, name):
            self.path = path
            self.name = name

        path: str
        name: str

    def __init__(self):
        self.commands = []

        try:
            self.ParseArgs()
            self.SetGlobalVars()
            self.RunCommand()
        except Exception as error:
            Log.Fail(f"Fatal error occurred: {error}", True)

    def GetCommands(self, path: str = "commands/"):
        for dirpath, dirnames, filenames in walk(path):
            for filename in filenames:
                if filename.endswith(".py"):
                    self.commands.append(self.CommandReference(f"{dirpath}/{filename}", ""))
            for dirname in dirnames:
                self.GetCommands(f"{dirpath}/{dirname}")

    def ParseArgs(self):
        self.GetCommands()

        print(self.commands)

        for reference in self.commands:
            for cmdName in dir(reference.path):
                cmd = getattr(reference.path, cmdName)
                if isclass(cmd) and not isabstract(cmd) and issubclass(cmd, Command) and cmd.__name__ != 'Command':
                    reference.name = cmdName.lower()

        print(self.commands)

        try:
            if len(argv) < 2:
                raise Exception("missing command name.")

            if argv[1] not in self.commandsList:
                raise Exception(f"invalid command name: \"{argv[1]}\".")

        except Exception as error:
            Help.Handler(Help)
            Log.Fail("Command parsing failed: "+str(error), True)

        self.commandName = argv[1]
        try:
            for reference in self.commands:
                if reference.name == self.commandName:
                    self.command: Command = getattr(reference.path, self.commandName.title())
                    break

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
            Log.Success(f"{self.commandName.title()} successfully completed.")
        except Exception as error:
            Log.Fail(f"{self.commandName.title()} failed: {error}", True)