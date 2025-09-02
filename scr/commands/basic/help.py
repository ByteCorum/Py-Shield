from utils.logger import Log
from config import Command

class Help(Command):
    exclusiveOptions = None
    requiredOptions = None
    options = None

    def Handler(command: Command = None):
        Log.Custom(command.help)

    help = f'''
Usage:
  py-shield <command> [options]
Example:
  py-shield obfuscate --help

Commands:
  obfuscate         -> obfuscate code using advanced techniques.
  obfuscatelegacy   -> obfuscate code using legacy techniques.
  dependencies      -> command to work with dependencies.
  info              -> show general information about the program.
  help              -> show general help.

General Options:
  --help            -> show help for commands.
  --quiet           -> give less output.
  --log <path>      -> write all logs to a file.
  --no-color        -> suppress colored output.
  --no-input        -> disable prompting for input.'''