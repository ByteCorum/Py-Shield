import zlib
import base64
import tokenize
import io
from cryptography.fernet import Fernet
import sys
import os



class Obfuscator:
    def __init__(self) -> None:
        self.SEPARATOR = b"/%p@K^(Y#C/_/jUEIakSX%/"
        self.GetArgs()
        self.SeparateArgs()
        self.Stream()
    
    def SeparateArgs(self):
        context = False

        if self.file:
            self.files = self.file.split(";")
            context = True
        else:
            self.files = []

        if self.dirPath:
            self.dirs = self.dirPath.split(";")
            context = True
        else:
            self.dirs = []

        if not context:
            print("[!] files and dir not selected")
            os._exit(0)

    
    def Stream(self):
            print("[i] Py-Sheild")
            self.workDir= os.getcwd()
            if self.file:
                print(f"included files: {self.files}")
            if self.dirPath:
                print(f"included dirs: {self.dirs}")
            
            if self.loops > 0:
                print(f"loops amount: {self.loops}")
            else:
                print("[!] --loops not declared")
                os._exit(0)

            if self.mode > 0:
                print(f"obfuscation mode: {self.mode}")
            else:
                print("[!] --mode not declared")
                os._exit(0)
            
            if self.output:
                print(f"output dir: {self.output}")
            else:
                print(f"output dir: /done")
                self.output = f"{self.workDir}\\done"
            print("\n")
            
            for file in self.files:
                with open(file, "r", encoding="utf-8") as f:
                    context = f.read()
                index = file.rfind(os.sep)
                fileName = file[index+1:]
                self.Obfuscate(context,[fileName,""])
            
            for dir in self.dirs:
                for dirpath, dirnames, filenames in os.walk(dir):
                    for filename in filenames:
                        if filename.endswith(".py"):
                            with open(dirpath+os.sep+filename, "r", encoding="utf-8") as f:
                                context = f.read()
                            index = dir.rfind(os.sep)+1
                            self.Obfuscate(context, [filename, dirpath[index:]])
                    

    def GetArgs(self):
        self.dirPath = ""
        self.output = ""
        self.file = ""
        self.loops = -1
        self.mode = -1
        if len(sys.argv) > 1:
            for i in range(1,len(sys.argv),2):
                match sys.argv[i]:
                    case "--loops":
                        if i+1 < len(sys.argv) and sys.argv[i+1].find("--") == -1:
                            self.loops = int(sys.argv[i+1])
                        else:
                            print("[!] --loops not initialized")
                            os._exit(0)

                    case "--mode":
                        if i+1 < len(sys.argv) and sys.argv[i+1].find("--") == -1:
                            self.mode = int(sys.argv[i+1])
                        else:
                            print("[!] --mode not initialized")
                            os._exit(0)
            
                    case "--dir":
                        if i+1 < len(sys.argv) and sys.argv[i+1].find("--") == -1:
                            self.dirPath = sys.argv[i+1]
                        else:
                            print("[!] --dir not initialized")
                            os._exit(0)
            
                    case "--file":
                        if i+1 < len(sys.argv) and sys.argv[i+1].find("--") == -1:
                            self.file = sys.argv[i+1]
                        else:
                            print("[!] --file not initialized")
                            os._exit(0)
            
                    case "--output":
                        if i+1 < len(sys.argv) and sys.argv[i+1].find("--") == -1:
                            self.output = sys.argv[i+1]
                        else:
                            print("[!] --output not initialized")
                            os._exit(0)
            
                    case "--help":
                        print('''
Py-Sheild legacy
v1.0.0.0
                      
options:
--loops (int)*  -> number of obfuscation loops 
--mode (int)*   -> obfuscation mode(1-4) as bigger number as better obfuscation but the output file is larger
--dir (str)     -> obfuscate all in dir
--file (str)*   -> files for obfuscation
--output (str)  -> output dir   
--help          -> get help
*               -> required option
text;text       -> to add more than one arg to option
                      
example of usage:
py-sheild-legacy --loops 3 --mode 2 --file code.py''')
                        os._exit(0)
                
                    case _:
                        print("[!] invalid option type \"--help\"")
                        os._exit(0)
        else:
            print('''
Py-Sheild legacy
v1.0.0.0
                      
options:
--loops (int)*  -> number of obfuscation loops 
--mode (int)*   -> obfuscation mode(1-4) as bigger number as better obfuscation but the output file is larger
--dir (str)     -> obfuscate all in dir
--file (str)*   -> files for obfuscation
--output (str)  -> output dir   
--help          -> get help
*               -> required option
text;text       -> to add more than one arg to option
                      
example of usage:
py-sheild-legacy --loops 3 --mode 2 --file code.py''')
            os._exit(0)
    
    def Obfuscate(self, context, fileProp = ["name", "path"]):
            context = self.RemoveComments(context)
            for i in range(self.loops):
                if self.mode == 4:
                    context = self.PowerObfuscate(context)
                elif self.mode == 3:
                    context = self.MediumObfuscate(context)
                elif self.mode == 2:
                    context = self.NormalObfuscate(context)
                elif self.mode == 1:
                    context = self.LiteObfuscate(context)
                else:
                    print("[i] invalid mode\n")
                    os._exit(0)
                
            if self.mode == 4:
                context = "_=lambda __:__import__('zlib').decompress(__import__('base64').b64decode(__import__('zlib').decompress((__import__('cryptography.fernet').fernet.Fernet(__import__('base64').b64decode(((__import__('zlib').decompress(__))[::-1].split(b'/%p@K^(Y#C/_/jUEIakSX%/'))[1])).decrypt(((__import__('zlib').decompress(__))[::-1].split(b'/%p@K^(Y#C/_/jUEIakSX%/'))[0])))[::-1]));"+context
            elif self.mode == 3:
                context = "_=lambda __:__import__('zlib').decompress(__import__('cryptography.fernet').fernet.Fernet(__import__('base64').b64decode(((__import__('zlib').decompress(__))[::-1].split(b'/%p@K^(Y#C/_/jUEIakSX%/'))[1])).decrypt(((__import__('zlib').decompress(__))[::-1].split(b'/%p@K^(Y#C/_/jUEIakSX%/'))[0])[::-1]);"+context
            elif self.mode == 2:
                context = "_=lambda __:__import__('zlib').decompress(__import__('cryptography.fernet').fernet.Fernet(((__import__('zlib').decompress(__))[::-1].split(b'/%p@K^(Y#C/_/jUEIakSX%/'))[1]).decrypt(((__import__('zlib').decompress(__))[::-1].split(b'/%p@K^(Y#C/_/jUEIakSX%/'))[0])[::-1]);"+context
            elif self.mode == 1:
                context = "_=lambda __:__import__('zlib').decompress(__import__('base64').b64decode((__import__('zlib').decompress(__))[::-1])[::-1]);"+context
            else:
                print("[i] invalid mode\n")
                os._exit(0)
                
            context = "#Obfuscated by Py-Sheild v1.0.0.0\n\n"+context

            dirPath = self.output+"\\"+fileProp[1]
            os.makedirs(dirPath, exist_ok=True)
                
            with open(f"{dirPath}\\{fileProp[0]}", "w", encoding="utf-8") as file:
                file.write(context)
                print(f"[i] code was saved as {dirPath}\\{fileProp[0]}")
            


    def PowerObfuscate(self, context):
        context = context.encode('utf-8')
        context = zlib.compress(context)
        encContext = base64.b64encode(context)
        encContext = encContext[::-1]
        encContext = zlib.compress(encContext)

        key = Fernet.generate_key()
        fernet = Fernet(key)
        encContext = fernet.encrypt(encContext)+self.SEPARATOR+base64.b64encode(key)

        encContext = encContext[::-1]
        encContext = zlib.compress(encContext)

        return f"exec((_)({encContext}))"

    def MediumObfuscate(self,context):
        context = context.encode('utf-8')
        context = zlib.compress(context)
        context = context[::-1]

        key = Fernet.generate_key()
        fernet = Fernet(key)
        encContext = fernet.encrypt(context)+self.SEPARATOR+base64.b64encode(key)

        encContext = encContext[::-1]
        encContext = zlib.compress(encContext)

        return f"exec((_)({encContext}))"

    def NormalObfuscate(self,context):
        context = context.encode('utf-8')
        context = zlib.compress(context)
        context = context[::-1]

        key = Fernet.generate_key()
        fernet = Fernet(key)
        encContext = fernet.encrypt(context)+self.SEPARATOR+key

        encContext = encContext[::-1]
        encContext = zlib.compress(encContext)

        return f"exec((_)({encContext}))"

    def LiteObfuscate(self,context):
        context = context.encode('utf-8')
        context = zlib.compress(context)
        context = context[::-1]

        encContext = base64.b64encode(context)

        encContext = encContext[::-1]
        encContext = zlib.compress(encContext)

        return f"exec((_)({encContext}))"

    def RemoveComments(self,context):
        tokens = tokenize.generate_tokens(io.StringIO(context).readline)
        filtered_tokens = (
            token for token in tokens
            if token.type != tokenize.COMMENT
        )
        return tokenize.untokenize(filtered_tokens)


if __name__ == "__main__":
    Obfuscator()