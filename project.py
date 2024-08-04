import os
from args import Args
from obfuscate import Obfuscator
from imports import ImportManager



class PySheild:
    def __init__(self) -> None:
        self.imports = []

        try:
            self.GetArgs(Args().args)
        except Exception as error:
            print(f"[!] Arguments parsing error: {error}")
            os._exit(-1)
        
        try:
            self.Stream()
        except Exception as error:
            print(f"[!] Stream error: {error}")
            os._exit(-1)

    def GetArgs(self,argslist):
        self.mainfile = argslist[0]
        self.loops = argslist[1]
        self.mode = argslist[2]
        self.output = argslist[3]
        self.importBool = argslist[4]
        self.files = argslist[5]
        self.dirs = argslist[6]
    
    def GetImports(self, filepath):
        if self.importBool:
            buff = ImportManager(filepath).imports
            for module in buff:
                if not module in self.imports:
                    self.imports.append(module)
    
    def Stream(self):
            print("[i] Py-Sheild")
            self.workDir= os.getcwd()
            print(f"main file: {self.mainfile}")
            
            if self.files:
                print(f"included files: {self.files}")
            if self.dirs:
                print(f"included dirs: {self.dirs}")
            
            print(f"obfuscation modes: {self.mode}")
            if self.loops > 0:
                print(f"loops amount: {self.loops}")
            
            if self.output:
                print(f"output dir: {self.output}")
            else:
                print(f"output dir: /done")
                self.output = f"{self.workDir}\\done"
            print("\n")
            print("Obfuscation...")

            os.makedirs(self.output)

            obfuscation = Obfuscator(self.mode,self.output,self.loops)
            
            for file in self.files:
                self.GetImports(file)
                with open(file, "r", encoding="utf-8") as f:
                    context = f.read()
                index = file.rfind(os.sep)
                fileName = file[index+1:]
                context = obfuscation.Obfuscate(context)
                obfuscation.SaveContext(context,[fileName,""])
            
            for dir in self.dirs:
                for dirpath, dirnames, filenames in os.walk(dir):
                    for filename in filenames:
                        if filename.endswith(".py"):
                            self.GetImports(dirpath+os.sep+filename)
                            with open(dirpath+os.sep+filename, "r", encoding="utf-8") as f:
                                context = f.read()
                            index = dir.rfind(os.sep)+1
                            
                            context = obfuscation.Obfuscate(context)
                            obfuscation.SaveContext(context,[filename,dirpath[index:]])
            
            self.GetImports(self.mainfile)
            with open(self.mainfile, "r", encoding="utf-8") as f:
                context = f.read()
            index = self.mainfile.rfind(os.sep)
            fileName = self.mainfile[index+1:]
   
            context = obfuscation.Obfuscate(context)
            obfuscation.SaveContext(context,[fileName,""], self.imports)
            obfuscation.CreateExecutor()
            