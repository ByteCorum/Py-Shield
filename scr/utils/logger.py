import os

class Color:
    HEADER = '\033[95m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    SUCCESS = '\033[92m'
    INFO = '\033[90m'
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
    def Show(prefix, message, color_code):
        if Log.colored:
            print(f"{color_code}{prefix} {Color.NORMAL}{message}")
        else:
            print(f"{prefix} {message}")

    @staticmethod
    def WriteLog(message):
        if Log.logFile:
            try:
                with open(Log.logFile, "a") as file:
                    file.write(f"{message}\n")
            except Exception as error:
                Log.Warning(error.__context__, True)

    @staticmethod
    def Info(message, bypassQuiet=False):
        Log.WriteLog(f"[i] {message}")
        if Log.quiet and not bypassQuiet:
            return
        Log.Show("[i]", message, Color.INFO)

    @staticmethod
    def Warning(message, pause=False):
        Log.WriteLog(f"[!] {message}")
        if Log.quiet and not pause:
            return
        Log.Show("[!]", message, Color.WARNING)

        if pause:
            input("Press Enter to continue...")

    @staticmethod
    def Fail(message, fatal=False):
        Log.WriteLog(f"[x] {message}")
        Log.Show("[x]", message, Color.FAIL)
        if fatal:
            os._exit(-1)

    @staticmethod
    def Success(message):
        Log.WriteLog(f"[+] {message}")
        Log.Show("[+]", message, Color.SUCCESS)

    @staticmethod
    def Question(message) -> str:
        Log.WriteLog(f"[?] {message}")
        
        if Log.colored:
            print(f"{Color.QUESTION}[?] {Color.NORMAL}{message}")
            response = input(f"{Color.INPUT}>>> {Color.NORMAL}")
        else:
            print(f"[?] {message}")
            response = input(f">>> ")
        
        Log.WriteLog(f">>> {response}")
        return response

    @staticmethod
    def Custom(message, color = Color.NORMAL):
        Log.WriteLog(message)
        if Log.quiet:
            return
        Log.Show("", message, color)