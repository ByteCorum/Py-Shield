from config import Command

from commands.basic.dependencies import DependenciesHandler
from commands.basic.help import HelpHandler
from commands.basic.info import InfoHandler

from commands.obfuscation.obfuscate import Obfuscation
from commands.obfuscation.obfuscatelegacy import ObfuscationLegacy

# class Name_of_the_command(Command): #note: only first letter should be capital
#
#     #May be left not initialized if your command has no options#
#     exclusiveOptions = [["--install","--uninstall"], ["--up","--down"]] #groups of options that can't be used together
#     requiredOptions = ["entrypoint", [""]] #options and groups(any option from a group is required) that are required
#
#     options = { #all the options that your command has. note: don't write help here, it's hendeled elsewhere
#         #General Options
#         "--quiet": False,
#         "--log": "",
#         "--no-color ": False,
#         "--no-input": False,
#
#         #Your Options
#         "--option1": False,
#         "entrypoint": "" #only 1 fixed option name used to store program entrypoint file path
#     }
#
#     #Should be always initialized#
#     handler = None #command handler that will be called when the command is executed
#     help = f'''I\'ll help u''' #help message for the command

class Obfuscate(Command):
    exclusiveOptions = []
    requiredOptions = ["entrypoint", ["--hashdata", "--fernet", "--aes", "--chacha", "--salsa" "--base64", "--recursive"]]
    options = {
        "--quiet": False,
        "--log": "",
        "--no-color ": False,
        "--no-input": False,

        "--hashdata": False,
        "--fernet": False,
        "--aes": False,
        "--chacha": False,
        "--salsa": False,
        "--base64": False,
        "--recursive": 0,
        "--no-protect": False,
        "--dirs": [],
        "--files": [],
        "--output": "",
        "--follow-imports" : False,
        "entrypoint": ""
    }

    handler = Obfuscation

    help = f'''
Usage:
  py-shield obfuscate [options] main.py
Example:
  py-shield obfuscate --hashdata --aes --follow-imports main.py

Notes:
  text|text         -> to add more than one arg to option.
  main.py           -> the entry point of your program.

Options:
  --help            -> show help for commands.
  --quiet           -> give less output.
  --log <path>      -> write all logs to a file.
  --no-color        -> suppress colored output.
  --no-input        -> disable prompting for input.

  --hashdata        -> convert all strings and var names into hash.
  --fernet          -> obfuscation and encryption using fernet.
  --aes             -> obfuscation and encryption using aes256.
  --chacha          -> obfuscation and encryption using chacha20.
  --salsa           -> obfuscation and encryption using salsa20.
  --base64          -> obfuscation and encryption using base64.
  --recursive <num> -> not strong but good if u need to hide ur prog from AVs.
  --no-protect      -> disable file modification protection.
  --dirs <path>     -> obfuscate all files in dir.
  --files <path>    -> files for obfuscation.
  --output <path>   -> output dir.
  --follow-imports  -> add all imports to the protected script.'''

class Obfuscatelegacy(Command):
    exclusiveOptions = []
    requiredOptions = ["--loops", "--mode", ["--files", "--dirs"]]
    options = {
        "--quiet": False,
        "--log": "",
        "--no-color ": False,
        "--no-input": False,

        "--loops": 0,
        "--mode": 0,
        "--dirs": [],
        "--files": [],
        "--output": ""
    }

    handler = ObfuscationLegacy

    help = f'''
Usage:
  py-shield obfuscatelegacy [options]
Example:
  py-shield obfuscatelegacy --loops 3 --mode 2 --file code.py

Notes:
  *                 -> required option.
  text|text         -> to add more than one arg to option.

Options:
  --help            -> show help for commands.
  --quiet           -> give less output.
  --log <path>      -> write all logs to a file.
  --no-color        -> suppress colored output.
  --no-input        -> disable prompting for input.

  --loops <num>*    -> number of obfuscation loops.
  --mode <num>*     -> obfuscation mode(1-4) as bigger number as better obfuscation but the output file is larger.
  --dirs <path>*    -> obfuscate all files in dir(required files or/and dir).
  --files <path>*   -> files for obfuscation(required files or/and dir).
  --output <path>   -> output dir.'''

class Dependencies(Command):
    exclusiveOptions = [["--show", "--install", "--uninstall", "--update"]]
    requiredOptions = [["--show", "--install", "--uninstall", "--update"]]

    options = {
        "--quiet": False,
        "--log": "",
        "--no-color ": False,
        "--no-input": False,

        "--show": False,
        "--install": False,
        "--uninstall": False,
        "--update": False,
    }

    handler = DependenciesHandler

    help = f'''
Usage:
  py-shield dependencies [options]
Example:
  py-shield dependencies --quiet --no-input y --install

Note:
  `                 -> only one option from a group can be used.
  *                 -> required option.

Options:
  --help            -> show help for commands.
  --quiet           -> give less output.
  --log <path>      -> write all logs to a file.
  --no-color        -> suppress colored output.
  --no-input        -> disable prompting for input.

  --show*`          -> show all dependencies of the program.
  --install*`       -> install all dependencies of the program.
  --uninstall*`     -> uninstall all dependencies of the program.
  --update*`        -> update all dependencies of the program'''

class Info(Command):
    exclusiveOptions = [["--all", "--version", "--url", "--description"]]
    requiredOptions = [["--all", "--version", "--url", "--description"]]

    options = {
        "--log": "",
        "--no-color": False,

        "--all": False,
        "--version": False,
        "--url": False,
        "--description": False,
    }

    handler = InfoHandler

    help = f'''
Usage:
  py-shield info [options]
Example:
  py-shield info --all

Note:
  `                 -> only one option from a group can be used.
  *                 -> required option.

Options:
  --help            -> show help for commands.
  --log <path>      -> write all logs to a file.
  --no-color        -> suppress colored output.

  --all*`           -> show all information about the program.
  --version*`       -> show version of the program.
  --url*`           -> show URL of program's github repo.
  --description*`   -> show description of the program.'''

class Help(Command):
    exclusiveOptions = None
    requiredOptions = None
    options = None

    handler = HelpHandler

    help = f'''
Usage:
  py-shield <command> [options]
Example:
  py-shield obfuscate --help

Commands:
  obfuscate         -> obfuscate code using advanced techniques.
  obfuscatelegacy  -> obfuscate code using legacy techniques.
  dependencies      -> command to work with dependencies.
  info              -> show general information about the program.
  help              -> show general help.

General Options:
  --help            -> show help for commands.
  --quiet           -> give less output.
  --log <path>      -> write all logs to a file.
  --no-color        -> suppress colored output.
  --no-input        -> disable prompting for input.'''