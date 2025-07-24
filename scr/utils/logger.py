import os

class Color:
    HEADER = '\033[95m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    SUCCESS = '\033[92m'
    INFO = '\33[90m'
    NORMAL = '\033[0m'
    QUESTION = '\033[96m'
    INPUT = '\033[94m'

class Format:
    NORMAL = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Log:
    logFile = ""
    quiet = False
    colored = True

    @staticmethod
    def Info(message, bypassQuiet=False):
        Log.WriteLog("[i] "+message)
        if Log.quiet and not bypassQuiet:
            return
        
        if Log.colored:
            print(f"{Color.INFO}[i] {Format.NORMAL}{message}")
        else:
            print("[i] "+ message)

    @staticmethod
    def Warning(message, pause=False):
        Log.WriteLog("[!] "+message)
        if Log.quiet and not pause:
            return
        
        if Log.colored:
            print(f"{Color.WARNING}[!] {Format.NORMAL}{message}")
        else:
            print("[!] "+ message)
    
    @staticmethod
    def Fail(message, fatal=False):
        Log.WriteLog("[x] "+message)
        
        if Log.colored:
            print(f"{Color.FAIL}[x] {Format.NORMAL}{message}")
        else:
            print("[x] "+ message)
        
        if fatal:
            os.exit(-1)

    @staticmethod
    def Success(message):
        Log.WriteLog("[+] "+message)
        
        if Log.colored:
            print(f"{Color.SUCCESS}[+] {Format.NORMAL}{message}")
        else:
            print("[+] "+ message)
    
    @staticmethod
    def Question(message) -> str:
        Log.WriteLog("[?] "+message)
        
        if Log.colored:
            print(f"{Color.QUESTION}[?] {Format.NORMAL}{message}")
            responce = input(f"{Color.INPUT}>>> {Format.NORMAL}")
        else:
            print("[?] "+ message)
            responce = input(f">>> ")
        
        Log.WriteLog(">>> "+responce)
        return responce
    
    @staticmethod
    def Custom(message, color):
        Log.WriteLog(message)
        if Log.quiet:
            return
        
        if Log.colored:
            print(f"{color}{message}{Format.NORMAL}")
        else:
            print(message)

    @staticmethod
    def WriteLog(message):
        if Log.logFile:
            try:
                with open(Log.logFile, "a") as file:
                    file.write(f"{message}\n")

            except Exception as error:
                Log.Warning(error.__context__, True)
