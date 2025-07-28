from hashlib import sha256
from os import path, getcwd
from Crypto.Cipher import ChaCha20
from Crypto.Cipher import Salsa20
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.fernet import Fernet

from base64 import b64decode, b64encode
from zlib import decompress
from sys import exit

class PyShield:
    def __init__(self, code, file):
        try:
            self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4 = code
            self.__fileb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4 = file
            code = None
            file = None

            self.__CheckHashb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4()
            self.__Decryptb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4()
        except Exception as runTimeError:
            print("Runtime error occurred, error: " + str(runTimeError))
            exit(-1)

    def __CheckHashb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4(self):
        try:
            self.__fileb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4 = path.relpath(self.__fileb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4, getcwd())

            with open(self.__fileb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4, 'rb') as file:
                fileHash = sha256(file.read()).hexdigest()

            for file in [['test.py', 'da66eb3a9ee240e3657c2503c738ad645cf2418edd06b0a52cd1bf4a10668747']]:
                if path.samefile(self.__fileb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4, file[0]) and fileHash == file[1]:
                    self.__fileb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4 = None
                    return

            raise Exception("Invalid file hash")
        except Exception as runTimeError:
            print("Runtime error occurred, error: " + str(runTimeError))
            exit(-1)

    def __Decryptb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4(self):
        try:
            self.__Base64b408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4()
            self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4 = self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4[::-1]
            self.__Recursiveb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4()
            self.__Salsab408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4()
            self.__ChaChab408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4()
            self.__Aesb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4()
            self.__Fernetb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4()
            self.__Base64b408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4()

            self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4 = self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4[::-1]
            self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4 = decompress(self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4)
            self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4 = self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4.decode('utf-8')

            self.__ReturnVariablesb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4()
            self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4 = b64encode(self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4.encode('utf-8'))

        except Exception as runTimeError:
            print("Runtime error occurred, error: " + str(runTimeError))
            exit(-1)

    @property
    def _(self):
        return compile(b64decode(self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4).decode('utf-8'), '<string>', 'exec')

    def __Recursiveb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4(self):
        for i in range(4):
            self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4 = decompress(self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4)
            self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4 = self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4[::-1]
            self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4 = b64decode(self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4)

    def __Salsab408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4(self):
        self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4 = decompress(self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4)
        self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4 = b64decode(self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4)
        nonce = self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4[:8]
        self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4 = self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4[8:]
        self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4 = Salsa20.new(key=b'\xde\xccY\xb0\xd5\x93\xf5\xc9\xf9!h\x9eM\xc9\xf2)9\xe5\xe2\xb5d3\xd7`\xf5\xd4K>,F\xe9\x90', nonce=nonce).decrypt(self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4)

    def __ChaChab408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4(self):
        self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4 = decompress(self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4)
        self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4 = b64decode(self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4)
        nonce = self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4[:8]
        self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4 = self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4[8:]
        self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4 = ChaCha20.new(key=b'S>\x83\xac#Y\x87\xc6\xfc\xd6\x95m\xc3\xb4x\x91x\x9d\xd3z\x06#w\xe7\xe0s\xebd7\xac\xd1@', nonce=nonce).decrypt(self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4)

    def __Aesb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4(self):
        self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4 = decompress(self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4)
        aes = AESGCM(b"\xaa\xa2\xb0R\xfb\xb3,'\x9e\xb2q\xe9_[\xfd\xe7Z^ie\x00\x9e\xabW\x11\x18\x87R\xa4Zzy")
        self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4 = b64decode(self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4)
        nonce = self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4[:12]
        self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4 = self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4[12:]
        self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4 = aes.decrypt(nonce, self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4, associated_data=None)

    def __Fernetb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4(self):
        self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4 = decompress(self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4)
        fernet = Fernet(b'GsRXAkQd-CbPKV8Qht2_kJ37CbtEdSXMpXsWqNEIYk4=')
        self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4 = fernet.decrypt(self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4)

    def __Base64b408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4(self):
        self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4 = decompress(self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4)
        self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4 = b64decode(self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4)

    def __ReturnVariablesb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4(self):
        for raw in [['2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', b'x\x9c\xcbH\xcd\xc9\xc9\x07\x00\x06,\x02\x15']]:
            string = decompress(raw[1]).decode("utf-8")
            self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4 = self.__codeb408a470d503d60636e8f875a2f3776ae51a9bf9cd0822a9faa1a20846b248d4.replace(raw[0], string)
