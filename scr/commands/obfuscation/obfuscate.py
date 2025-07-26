from os import path, sep, walk, getcwd, makedirs
from shutil import rmtree
from utils.logger import Log
from config import Command
from utils.langMgr import RemoveComments

class Obfuscation:
    def __init__(self, this: Command):
        self.this = this
        self.workingDir = getcwd()
        self.imports = []
        self.CheckOptions()
        self.ObfuscateFiles()

    def CheckOptions(self):
        Log.Info("Obfuscation.")
        if self.this.options["--recursive"] < 0:
            raise Exception("Invalid --recursive value.")

        if not self.this.options["--output"]:
            self.this.options["--output"] = "obfuscated"

        if path.exists(self.this.options["--output"]):
            Log.Warning(f"Output directory already exists: \"{self.this.options['--output']}\".")
            responce = ""
            while responce != "y" or responce != "n" or responce != "ignore":
                responce = Log.Question("Override directory? (y/n)").lower()

                match responce:
                    case "ignore":
                        rmtree(self.this.options["--output"])
                        Log.Info("Directory overridden.")
                        break
                    case "y":
                        rmtree(self.this.options["--output"])
                        Log.Success("Directory overridden.")
                        break
                    case "n":
                        Log.Success("Directory skipped.")
                        break
                    case _:
                        Log.Fail("Invalid response. Please enter 'y' or 'n'.")
            print()

        self.entryPoint = self.this.options["entrypoint"]
        if not path.exists(self.entryPoint) or not path.isfile(self.entryPoint) or not self.entryPoint.endswith(".py"):
            raise Exception(f"Invalid entrypoint path: \"{self.entryPoint}\".")
        if path.isabs(self.entryPoint):
            raise Exception(f"Abs path is unsupported: \"{self.entryPoint}\"")

        for file in self.this.options["--files"]:
            if not path.exists(file) or not path.isfile(file) or not file.endswith(".py"):
                raise Exception(f"Invalid file path: \"{file}\".")
            if path.isabs(file):
                raise Exception(f"Abs path is unsupported: \"{file}\"")

        for dir in self.this.options["--dirs"]:
            if not path.exists(dir) or not path.isdir(dir):
                raise Exception(f"Invalid directory path: \"{dir}\".")
            if path.isabs(dir):
                raise Exception(f"Abs path is unsupported: \"{dir}\"")

        Log.Info(f"Entrypoint file: {self.entryPoint}")
        if self.this.options["--files"]:
            Log.Info(f"Included files: {self.this.options["--files"]}")
        if self.this.options["--dirs"]:
            Log.Info(f"Included dirs: {self.this.options["--dirs"]}")

        methods = f"{"hashdata, " if self.this.options["--hashdata"] else ""}{"fernet, " if self.this.options["--fernet"] else ""}{"aes, " if self.this.options["--aes"] else ""}{"rsa, " if self.this.options["--rsa"] else ""}{"base64, " if self.this.options["--base64"] else ""}{f"recursive<{self.this.options["--recursive"]}>, " if self.this.options["--recursive"]>0 else ""}"[:-2]
        if methods:
            Log.Info(f"Obfuscation methods: {methods}")

        options = f"{"follow-imports, " if self.this.options["--follow-imports"] else ""}"[:-2]
        if options:
            Log.Info(f"Additional options: {options}")
        Log.Info(f"output dir: {self.this.options["--output"]}\n")

    def ObfuscateFiles(self):
        ...