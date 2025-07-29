from abc import ABC

NAME = "Py-Shield"
AUTHOR = "ByteCorum"
URL = "https://github.com/ByteCorum/Py-Shield"
VERSION = "3.0.0.0"
DESCRIPTION = "Tool/Library for Python used to obfuscate and protect your code in static and runtime from decompilation, reverse debug, etc. Also, can prevent detection by antiviruses."

class Command(ABC):
    exclusiveOptions: list
    requiredOptions: list
    options: dict

    handler: callable
    help: str