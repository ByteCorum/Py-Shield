import sys
import os
from config import CFG


class Args:
    def __init__(self) -> None:
        self.SetVars()
        self.Get()
        self.Separate()
        self.Check()
    
    @property
    def args(self):
        return [self.mainfile,self.loops, self.modes, self.output, self.imports, self.files, self.dirs]

    def SetVars(self):
        self.mainfile = ""
        self.dirPath = ""
        self.output = ""
        self.file = ""
        self.loops = 0
        self.mode = ""
        self.imports = False

    def Get(self):
        if len(sys.argv) > 1:
                for i in range(1,len(sys.argv),2):
                    match sys.argv[i]:
                        case "--loops":
                            if i+1 < len(sys.argv) and sys.argv[i+1].find("--") == -1:
                                self.loops = int(sys.argv[i+1])
                            else:
                                print("[!] --loops not initialized")
                                os._exit(-1)

                        case "--mode":
                            if i+1 < len(sys.argv) and sys.argv[i+1].find("--") == -1:
                                self.mode = sys.argv[i+1]
                            else:
                                print("[!] --mode not initialized")
                                os._exit(-1)
            
                        case "--dirs":
                            if i+1 < len(sys.argv) and sys.argv[i+1].find("--") == -1:
                                self.dirPath = sys.argv[i+1]
                            else:
                                print("[!] --dirs not initialized")
                                os._exit(-1)
            
                        case "--files":
                            if i+1 < len(sys.argv) and sys.argv[i+1].find("--") == -1:
                                self.file = sys.argv[i+1]
                            else:
                                print("[!] --files not initialized")
                                os._exit(-1)
            
                        case "--output":
                            if i+1 < len(sys.argv) and sys.argv[i+1].find("--") == -1:
                                self.output = sys.argv[i+1]
                            else:
                                print("[!] --output not initialized")
                                os._exit(-1)
                    
                        case "--install-deps":
                            os.system("pip install cryptography")
                            os.system("pip install pycryptodome")
                            os.system("pip install cython")
                            os._exit(-1)
                    
                        case "--follow":
                            if sys.argv[i+1] == "imports":
                                self.imports = True
                            else:
                                print("[!] --follow not initialized")
                                os._exit(-1)
            
                        case "--help":
                            print(CFG.helpText)
                            os._exit(0)
                
                        case _:
                            if i == len(sys.argv)-1:
                                if sys.argv[i].find(".py"):
                                    self.mainfile = sys.argv[i]
                                else:
                                    print("[!] invalid main file")
                                    os._exit(-1)
                            else:
                                print("[!] invalid option type \"--help\"")
                                os._exit(-1)
        else:
            print(CFG.helpText)
            os._exit(0)

    def Separate(self):
        if self.file:
            self.files = self.file.split(";")
        else:
            self.files = []

        if self.dirPath:
            self.dirs = self.dirPath.split(";")
        else:
            self.dirs = []
        
        if self.mode:
            self.modes = self.mode.split(";")
            if "hashstr" not in self.modes and "crypt" not in self.modes and "looping" not in self.modes and "aes" not in self.modes:
                self.modes = []
                print("[!] invalid mode key")
                os._exit(-1)
        else:
            self.modes = []
            print("[!] --mode not declared")
            os._exit(-1)
    
    def Check(self):
        if not self.mainfile:
            print("[!] main file not selected")
            os._exit(-1)
            
        if self.loops <= 0 and "looping" in self.modes:
            print("[!] --loops not declared")
            os._exit(-1)
