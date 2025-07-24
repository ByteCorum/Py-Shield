class Obfuscate:
    parameters = {
        "--quiet": False,
        "--log": "",
        "--no-color ": False,
        "--no-input": "",
        "--hashdata": False,
        "--fernet": False,
        "--aes": False,
        "--rsa": False,
        "--base64": False,
        "--recursive": 0,
        "--dirs": [],
        "--files": [],
        "--output": "",
        "--follow-imports" : False
    }

    handler = None

    help = f'''
Usage:
  py-shield obfuscate [options] main.py
Example:
  py-shield obfuscate --hashdata --aes --follow-imports main.py

Notes:
  text;text         -> to add more than one arg to option.
  main.py           -> the entry point of your program.

Options:
  --help            -> show help for commands.
  --quiet           -> give less output.
  --log <path>      -> write all logs to a file.
  --no-color        -> suppress colored output.
  --no-input <y/n>  -> disable prompting for input.

  --hashdata        -> convert all strings and var names into hash.
  --fernet          -> obfuscation and encryption using fernet.
  --aes             -> obfuscation and encryption using aes256.
  --rsa             -> obfuscation and encryption using rsa.
  --base64          -> obfuscation and encryption using base64
  --recursive <num> -> recursive obfuscation, best to hide the program from AVs.
  --dirs <path>     -> obfuscate all files in dir.
  --files <path>    -> files for obfuscation.
  --output <path>   -> output dir.
  --follow-imports  -> add all imports to the protected script.
'''

class ObfuscateLegacy:
    parameters = {
        "--quiet": False,
        "--log": "",
        "--no-color ": False,
        "--no-input": "",
        "--loops": 0,
        "--mode": 0,
        "--dirs": [],
        "--files": [],
        "--output": ""
    }

    handler = None

    help = f'''
Usage:
  py-shield obfuscate-legacy [options]
Example:
  py-shield obfuscate-legacy --loops 3 --mode 2 --file code.py

Notes:
  *                 -> required option.
  text;text         -> to add more than one arg to option.

Options:
  --help            -> show help for commands.
  --quiet           -> give less output.
  --log <path>      -> write all logs to a file.
  --no-color        -> suppress colored output.
  --no-input <y/n>  -> disable prompting for input.

  --loops <num>*    -> number of obfuscation loops.
  --mode <num>*     -> obfuscation mode(1-4) as bigger number as better obfuscation but the output file is larger.
  --dirs <path>     -> obfuscate all files in dir.
  --files <path>*   -> files for obfuscation.
  --output <path>   -> output dir.
'''

class Dependencies:
    parameters = {
        "--quiet": False,
        "--log": "",
        "--no-color ": False,
        "--no-input": "",
        "--show": False,
        "--install": False,
        "--uninstall": False,
        "--update": False,
    }

    handler = None

    help = f'''
Usage:
  py-shield dependencies [options]
Example:
  py-shield dependencies --quiet --no-input y --install

Options:
  --help            -> show help for commands.
  --quiet           -> give less output.
  --log <path>      -> write all logs to a file.
  --no-color        -> suppress colored output.
  --no-input <y/n>  -> disable prompting for input.

  --show            -> show all dependencies of the program.
  --install         -> install all dependencies of the program.
  --uninstall       -> uninstall all dependencies of the program.
  --update          -> update all dependencies of the program
'''

class Info:
    parameters = {
        "--log": "",
        "--no-color ": False,
        "--all": False,
        "--version": False,
        "--url": False,
        "--description": False,
    }

    handler = None

    help = f'''
Usage:
  py-shield info [options]
Example:
  py-shield info --all

Options:
  --help            -> show help for commands.
  --log <path>      -> write all logs to a file.
  --no-color        -> suppress colored output.

  --all             -> show all information about the program.
  --version         -> show version of the program.
  --url             -> show URL of program's github repo.
  --description     -> show description of the program.

'''

class Help:
    help = f'''
Usage:
  py-shield <command> [options]
Example:
  py-shield obfuscate --help

Commands:
  obfuscate         -> obfuscate code using advanced techniques.
  obfuscate-legacy  -> obfuscate code using legacy techniques.
  dependencies      -> command to work with dependencies.
  info              -> show general information about the program.
  help              -> show general help.

General Options:
  --help            -> show help for commands.
  --quiet           -> give less output.
  --log <path>      -> write all logs to a file.
  --no-color        -> suppress colored output.
  --no-input <y/n>  -> disable prompting for input.
'''