import zlib
import base64
import tokenize
import hashlib
import ast  
import io
from cryptography.fernet import Fernet
import random
from Crypto.Cipher import AES
import os
import secrets
from Crypto.Util.Padding import pad
import shutil

class Obfuscator:
    def __init__(self, mode: list, output: str,  loops: int = 0) -> None:
        self.hash = False
        self.crypt = False
        self.aes = False
        self.loop = False
        self.hashed_strings = None
        self.farnetKey = None
        self.aesKey = None
        self.iv = None

        if "hashstr" in mode:
            self.hashed_strings = []
            self.hash = True
        if "crypt" in mode:
            self.farnetKey = Fernet.generate_key()
            self.crypt = True
        if "aes" in mode:
            self.aesKey = secrets.token_bytes(32)
            self.aesKey = hashlib.sha256(self.aesKey).digest()
            self.aes = True
        if "looping" in mode:
            self.loop = True
        
        self.loops = loops
        self.output = output
        self.number = random.randint(10000000,99999999)
    
    def Obfuscate(self, context):
        context = self.RemoveComments(context)

        if self.hash:
            print("HashVars")
            context = self.HashVars(context)
        
        print("Misc")
        context = context[::-1]
        context = context.encode('utf-8')
        context = context[::-1]
        context = zlib.compress(context)
        context = base64.b64encode(context)
        context = context[::-1]
        context = zlib.compress(context)

        if self.crypt:
            print("FernetEncrypt")
            context = self.FernetEncrypt(context)
        if self.aes:
            print("AesEncrypt")
            context, self.iv = self.AesEncrypt(context, self.aesKey)
        if self.loop:
            print("LoopEncrypt")
            context = self.LoopEncrypt(context)
        
        return context

    def RemoveComments(self,context):
        tokens = tokenize.generate_tokens(io.StringIO(context).readline)
        filtered_tokens = (
            token for token in tokens
            if token.type != tokenize.COMMENT
        )
        return tokenize.untokenize(filtered_tokens)

    def HashVars(self, context: str):
        tree = ast.parse(context)
        hashedContext == None

        for node in ast.walk(tree):
            if isinstance(node, ast.Constant):
                string = base64.b64encode(node.s.encode('utf-8'))
                string = string[::-1]
                string = zlib.compress(string)
                hashstr = hashlib.sha256(node.s.encode('utf-8')).hexdigest()

                if not [hashstr,string] in self.hashed_strings:
                    self.hashed_strings.append([hashstr,string])
                    hashedContext = context.replace(node.s , hashstr)
                    print(node.s, end="  ===>  ")
                    print(hashstr)
            
        if hashedContext != None:
            context = hashedContext
        return context

    def FernetEncrypt(self, context):
        fernet = Fernet(self.farnetKey)
        context = fernet.encrypt(context)
        context = zlib.compress(context)
        return context

    def AesEncrypt(self, context: bytes, key: bytes):
        cipher = AES.new(key, AES.MODE_CBC)
        iv = cipher.iv 
        context = pad(context, AES.block_size)
        context = cipher.encrypt(context)
        context = zlib.compress(context)
        return context, iv
    
    def LoopEncrypt(self, context):
        for i in range (self.loops):
            context = base64.b64encode(context)
            context = context[::-1]
            context = zlib.compress(context)
        return context
    
    #def OldObfuscation(self, context):
        #for i in range(6):
            #context = context.encode('utf-8')
            #context = zlib.compress(context)
            #context = context[::-1]

            #key = Fernet.generate_key()
            #fernet = Fernet(key)
            #context = fernet.encrypt(context)+b"%[0(#^@%&*)$##)9]%"+base64.b64encode(key)

            #context = context[::-1]
            #context = zlib.compress(context)
            #context = f"exec((_)({context}))"
    
        #return "_=lambda __:__import__('zlib').decompress(__import__('cryptography.fernet').fernet.Fernet(__import__('base64').b64decode(((__import__('zlib').decompress(__))[::-1].split(b'/%p@K^(Y#C/_/jUEIakSX%/'))[1])).decrypt(((__import__('zlib').decompress(__))[::-1].split(b'/%p@K^(Y#C/_/jUEIakSX%/'))[0])[::-1]);"+context
    
    def SaveContext(self, context ,fileProp = ["name", "path"], imports =[]):
        imp = ""
        for module in imports:
            imp+="import "+str(module)+"\n"
            
        context = f'''#Obfuscated by Py-Sheild v1.0.0.0
{imp}
from PySheild.script_{self.number} import PySheild
PySheild({context})'''

        dirPath = self.output+"\\"+fileProp[1]
        os.makedirs(dirPath, exist_ok=True)
                
        with open(f"{dirPath}\\{fileProp[0]}", "w", encoding="utf-8") as file:
            file.write(context)
            print(f"[i] code was saved as {dirPath}\\{fileProp[0]}")
    
    def CreateExecutor(self):
        context = '''import base64
#[fernetimport]
#[aesimport]
import zlib
class PySheild:
    def __init__(self, code):
        self.code = code
        #[hashvar]
        #[fernetvar]
        #[aesvar]
        #[loopsvar]
        self.DeObfuscate()
    def DeObfuscate(self):
        try:
            #[callloops]
            #[callaes]
            #[callfernet]
            self.BaseDecrypt()
            #[callhash]
            exec(self.code)
        except Exception as runTimeError:
            print("Runtime error occurred, error: ",end='')
            print(runTimeError)
#[loopsfunc]
#[aesfunc]
#[fernetfunc]
    def BaseDecrypt(self):
        self.code = zlib.decompress(self.code)
        self.code = self.code[::-1]
        self.code = base64.b64decode(self.code)
        self.code = zlib.decompress(self.code)
        self.code = self.code[::-1]
        self.code = self.code.decode('utf-8')
        self.code = self.code[::-1]        
#[hashfunc]
'''
        fernetImport = "from cryptography.fernet import Fernet"
        aesImport = '''from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad''' 

        hashVar = f"self.hashed_strings = {self.hashed_strings}"
        fernetVar = f"self.farnetKey = {self.farnetKey}"
        aesVar = f'''self.aesKey = {self.aesKey}
        self.iv = {self.iv}'''
        loopsVar = f"self.loops = {self.loops}"

        callLoops = "self.DecryptLoop()"   
        callAes = "self.DecryptAes()"
        callFernet = "self.DecryptFernet()"
        callHash = "self.DeHashStr()"

        loopsFunc = '''    def DecryptLoop(self):
        for i in range (self.loops):
            self.code = zlib.decompress(self.code)
            self.code = self.code[::-1]
            self.code = base64.b64decode(self.code)'''
        aesFunc = '''    def DecryptAes(self):
        self.code = zlib.decompress(self.code)
        cipher = AES.new(self.aesKey, AES.MODE_CBC, self.iv)
        self.code = cipher.decrypt(self.code)
        self.code = unpad(self.code, AES.block_size)'''
        fernetFunc = '''    def DecryptFernet(self):
        self.code = zlib.decompress(self.code)
        fernet = Fernet(self.farnetKey)
        self.code = fernet.decrypt(self.code)'''
        hashFunc = '''    def DeHashStr(self):
        for raw in self.hashed_strings:
            string = zlib.decompress(raw[1])
            string = string[::-1]
            string = base64.b64decode(string).decode('utf-8')
            self.code = self.code.replace(raw[0], string)'''
    
        if self.hash:
            context = context.replace("#[hashvar]",hashVar)
            context = context.replace("#[callhash]",callHash)
            context = context.replace("#[hashfunc]",hashFunc)
        
        if self.crypt:
            context = context.replace("#[fernetimport]",fernetImport)
            context = context.replace("#[fernetvar]",fernetVar)
            context = context.replace("#[callfernet]",callFernet)
            context = context.replace("#[fernetfunc]",fernetFunc)
        
        if self.aes:
            context = context.replace("#[aesimport]",aesImport)
            context = context.replace("#[aesvar]",aesVar)
            context = context.replace("#[callaes]",callAes)
            context = context.replace("#[aesfunc]",aesFunc)
        
        if self.loop:
            context = context.replace("#[loopsvar]",loopsVar)
            context = context.replace("#[callloops]",callLoops)
            context = context.replace("#[loopsfunc]",loopsFunc)


        #context = self.OldObfuscation(context)

        dirPath = self.output+"\\"+"PySheild"
        os.makedirs(dirPath, exist_ok=True)

        with open(f"{dirPath}\\script_{self.number}.py", "w", encoding="utf-8") as file:
            file.write(context)
        
        #self.AssembleExecutor(dirPath)
        print(f"[i] execurot created as {dirPath}\\script_{self.number}")
    
    def AssembleExecutor(self, dirPath):
        code = f'''from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
ext_modules = [
    Extension("script_{self.number}",  ["script_{self.number}.py"]),
]
setup(
    name = 'PySheild',
    cmdclass = #[stub]#,
    ext_modules = ext_modules
)   
'''
        code = code.replace("#[stub]#","{'build_ext': build_ext}")

        with open(f"{dirPath}\\assembler.py", "w", encoding="utf-8") as file:
            file.write(code)

        curPath = os.getcwd()
        os.chdir(dirPath)
        os.system('python assembler.py build_ext --inplace >/dev/null 2>&1')#,stdout=subprocess.PIPE,stderr=subprocess.STDOUT
        os.chdir(curPath)
        shutil.rmtree(f"{dirPath}\\build",ignore_errors=True)
        os.remove(f"{dirPath}\\assembler.py")
        os.remove(f"{dirPath}\\script_{self.number}.py")
        os.remove(f"{dirPath}\\script_{self.number}.c")

        for dirpath, dirnames, filenames in os.walk(dirPath):
            for filename in filenames:
                if filename.endswith(".pyd"):
                    os.rename(dirPath+os.sep+filename, f'{dirPath}\\script_{self.number}.pyd')