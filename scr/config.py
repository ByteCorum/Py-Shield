from abc import ABC

NAME = "Py-Shield"
AUTHOR = "ByteCorum"
URL = "https://github.com/ByteCorum/Py-Shield"
VERSION = "3.0.0.0"
DESCRIPTION = "Tool/Library for Python used to obfuscate and protect your code from decompilation, reverse engineering, etc. Also, can prevent detections by antiviruses."

class Command(ABC):
    exclusiveOptions: list
    requiredOptions: list
    options: dict

    handler: callable
    help: str