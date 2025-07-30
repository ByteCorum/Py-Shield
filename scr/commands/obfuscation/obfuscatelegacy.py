from os import path, sep, walk, getcwd, makedirs
from shutil import rmtree
from utils.logger import Log
from config import Command
from utils.obfuscation import LegacyObfuscation
from utils.langMgr import RemoveComments

class ObfuscationLegacy:
    def __init__(self, this: Command):
        self.this = this
        self.workingDir = getcwd()
        self.CheckOptions()
        self.ObfuscateFiles()

    def CheckOptions(self):
        Log.Info("Legacy obfuscation.")

        if self.this.options["--loops"] < 1:
            raise Exception("Invalid --loops value.")
        if self.this.options["--mode"] < 1 or self.this.options["--mode"] > 4:
            raise Exception("Invalid --mode value.")

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

        if self.this.options["--files"]:
            Log.Info(f"Included files: {self.this.options["--files"]}")
        if self.this.options["--dirs"]:
            Log.Info(f"Included dirs: {self.this.options["--dirs"]}")

        Log.Info(f"loops amount: {self.this.options["--loops"]}")
        Log.Info(f"obfuscation mode: {self.this.options["--mode"]}")
        Log.Info(f"output dir: {self.this.options["--output"]}\n")

    def ObfuscateFiles(self):
        for file in self.this.options["--files"]:
            with open(file, "r", encoding="utf-8") as pyFile:
                context = pyFile.read()
            if not context:
                Log.Warning(f"File {file} is empty")
                continue

            filepath, filename = path.split(file)
            if filepath:
                filepath = path.relpath(filepath, self.workingDir)

            context = RemoveComments(context)

            obfuscator = LegacyObfuscation(self.this.options["--mode"], self.this.options["--loops"], LegacyObfuscation.GenSeperator(12))
            context = obfuscator.Encrypt(context)
            context = obfuscator.Wrap(context)

            self.SaveFile(filename, filepath, context)

        for dir in self.this.options["--dirs"]:
            for dirpath, dirnames, filenames in walk(dir):
                for filename in filenames:

                    if filename.endswith(".py"):
                        with open(dirpath+sep+filename, "r", encoding="utf-8") as file:
                            context = file.read()
                        if not context:
                            Log.Warning(f"Empty file {filename} in dir {dirpath}")
                            continue

                        dirpath = path.relpath(dirpath, self.workingDir)

                        context = RemoveComments(context)

                        obfuscator = LegacyObfuscation(self.this.options["--mode"], self.this.options["--loops"], LegacyObfuscation.GenSeperator(12))
                        context = obfuscator.Encrypt(context)
                        context = obfuscator.Wrap(context)

                        self.SaveFile(filename , dirpath, context)

    def SaveFile(self, filename, filepath, content):
        filepath = self.this.options["--output"]+sep+filepath
        makedirs(filepath, exist_ok=True)

        with open(filepath+sep+filename, "w", encoding="utf-8") as file:
            file.write(content)

        Log.Info(f"{filename} saved in {filepath[:-1]}")