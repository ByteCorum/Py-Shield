from sys import argv, exit
from os import walk, path
from inspect import isclass, isabstract
from importlib.util import spec_from_file_location, module_from_spec

from utils.optionsParser import OptionsParser
from utils.logger import Log
from config import Command, NAME
from commands.basic.help import Help


class PyShield:
    command: Command
    commandName: str
    noOptions = False

    def __init__(self):
        try:
            self.ParseArgs()
            self.SetGlobalVars()
            self.RunCommand()
        except Exception as error:
            Log.Fail(f"Fatal error occurred: {error}", True)

    def ParseArgs(self):
        try:
            if len(argv) < 2:
                raise Exception("missing command name.")

            self.commandName = argv[1].title()
            self.command = self.GetCommand(self.commandName)

        except Exception as error:
            Help.Handler(Help)
            Log.Fail("Command parsing failed: "+str(error), True)

        try:
            if not self.command.options:
                self.noOptions = True
                return

            parser = OptionsParser(argv[2:], self.command)
            parser.Parse()
            if parser.ended:
                exit(0)

            parser.Validate()
            self.command = parser.command#get filled command object

        except Exception as error:
            Log.Fail(f"Options parsing failed: {error}", True)

    def GetCommand(self, name):
        command = self.SearchCommand(name, f"{path.dirname(path.abspath(__file__))}/commands/")
        if not command:
            raise Exception(f"invalid command name: \"{name}\".")

        return command


    def SearchCommand(self, name: str, path: str):
        for dirpath, dirnames, filenames in walk(path):
            for filename in filenames:
                if filename.endswith(".py") and filename != "__init__.py":
                    filePath = f"{dirpath}/{filename}"
                    spec = spec_from_file_location("temp_module", filePath)

                    if spec and spec.loader:
                        module = module_from_spec(spec)
                        try:
                            spec.loader.exec_module(module)
                            for cmdName in dir(module):
                                command = getattr(module, cmdName)
                                if (isclass(command) and
                                    not isabstract(command) and
                                    issubclass(command, Command) and
                                    command.__name__ != 'Command' and
                                    command.__name__ == name):
                                    return command

                        except Exception as error:
                            # Skip files that can't be imported
                            continue
        return None


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
            self.command.Handler(self.command)
            Log.Success(f"{self.commandName} successfully completed.")
        except Exception as error:
            Log.Fail(f"{self.commandName} failed: {error}", True)