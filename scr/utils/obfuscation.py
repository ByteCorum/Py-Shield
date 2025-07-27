from random import choice, randint
from string import ascii_letters, digits, punctuation
from utils.crypto import FernetCipher, AesCipher, ChaCha20Cipher, Salsa20Cipher, compress, b64encode
from ast import parse, walk, Constant
from hashlib import sha256

class MainObfuscation:
    def __init__(self, hashdata: bool, fernet: bool, aes: bool, chacha20: bool, salsa20: bool, base64: bool, recursive: int) -> None:
        self.hashdata = hashdata
        self.fernet = fernet
        self.aes = aes
        self.chacha20 = chacha20
        self.salsa20 = salsa20
        self.base64 = base64
        self.recursive = recursive
        if self.recursive < 0:
            raise Exception("Invalid recursive value.")

        self.PrepareKeys()

    def PrepareKeys(self) -> None:
        self.number = randint(10000000,99999999)

        if self.hashdata:
            self.hashedVariables = []
        if self.fernet:
            self.fernetKey = FernetCipher.GenKey()
        if self.aes:
            self.aesKey = AesCipher.GenKey(256)
        if self.chacha20:
            self.chacha20Key = ChaCha20Cipher.GenKey()
        if self.salsa20:
            self.salsa20Key = Salsa20Cipher.GenKey()

    def Obfuscate(self, content: str) -> str:
        if self.hashdata:
            content = self.HashVariables(content)

        content = content.encode('utf-8')
        content = compress(content)
        content = content[::-1]
        if self.base64:
            content = b64encode(content)
            content = compress(content)

        if self.fernet:
            content = FernetCipher.Encrypt(self.fernetKey, content)
            content = compress(content)

        if self.aes:
            content = AesCipher.Encrypt(self.aesKey, content)
            content = compress(content)

        if self.chacha20:
            content = ChaCha20Cipher.Encrypt(self.chacha20Key, content)
            content = compress(content)

        if self.salsa20:
            content = Salsa20Cipher.Encrypt(self.salsa20Key, content)
            content = compress(content)

        for i in range(self.recursive):
            content = b64encode(content)
            content = content[::-1]
            content = compress(content)

        content = content[::-1]
        if self.base64:
            content = b64encode(content)
            content = compress(content)

        return content

    def HashVariables(self, content: str) -> str:
        tree = parse(content)
        for node in walk(tree):
            if isinstance(node, Constant) and isinstance(node.value, str):
                string = node.value

                if len(string) > 1 and (any(char in ascii_letters for char in string) or any(char in digits for char in string)):
                    hashstr = compress(string.encode('utf-8'))
                    hashstr = hashstr[::-1]
                    hashstr = sha256(hashstr).hexdigest()

                    if [hashstr,string] not in self.hashedVariables:
                        self.hashedVariables.append([hashstr,string])
                    content = content.replace(string, hashstr,1)

        return content


class LegacyObfuscation:
    def __init__(self, mode, loops, separator: str):
        if mode < 1 or mode > 4:
            raise Exception("Invalid mode value.")
        if loops < 1:
            raise Exception("Invalid loops value.")

        self.mode = mode
        self.loops = loops
        self.separator = separator

    def Encrypt(self, content) -> str:
        for i in range(self.loops):
            match self.mode:
                case 1:
                    content = self.LiteObfuscation(content)
                case 2:
                    content = self.NormalObfuscation(content)
                case 3:
                    content = self.MediumObfuscation(content)
                case 4:
                    content = self.PowerObfuscateion(content)
                case _:
                    raise Exception("Invalid mode value.")

        return content

    def Wrap(self, content) -> str:
        match self.mode:
            case 1:
                return "_=lambda __:__import__('zlib').decompress(__import__('base64').b64decode((__import__('zlib').decompress(__))[::-1])[::-1]);"+content
            case 2:
                return f"_=lambda __:__import__('zlib').decompress(__import__('cryptography.fernet').fernet.Fernet(((__import__('zlib').decompress(__))[::-1].split(b'{self.separator}'))[1]).decrypt(((__import__('zlib').decompress(__))[::-1].split(b'{self.separator}'))[0])[::-1]);"+content
            case 3:
                return f"_=lambda __:__import__('zlib').decompress(__import__('cryptography.fernet').fernet.Fernet(__import__('base64').b64decode(((__import__('zlib').decompress(__))[::-1].split(b'{self.separator}'))[1])).decrypt(((__import__('zlib').decompress(__))[::-1].split(b'{self.separator}'))[0])[::-1]);"+content
            case 4:
                return f"_=lambda __:__import__('zlib').decompress(__import__('base64').b64decode(__import__('zlib').decompress((__import__('cryptography.fernet').fernet.Fernet(__import__('base64').b64decode(((__import__('zlib').decompress(__))[::-1].split(b'{self.separator}'))[1])).decrypt(((__import__('zlib').decompress(__))[::-1].split(b'{self.separator}'))[0])))[::-1]));"+content
            case _:
                raise Exception("Invalid mode value.")

    def PowerObfuscateion(self, content):
        content = content.encode('utf-8')
        content = compress(content)
        enccontent = b64encode(content)
        enccontent = enccontent[::-1]
        enccontent = compress(enccontent)

        key = FernetCipher.GenKey()
        enccontent = FernetCipher.Encrypt(key,enccontent)+self.separator.encode("utf-8")+b64encode(key)

        enccontent = enccontent[::-1]
        enccontent = compress(enccontent)

        return f"exec((_)({enccontent}))"

    def MediumObfuscation(self,content):
        content = content.encode('utf-8')
        content = compress(content)
        content = content[::-1]

        key = FernetCipher.GenKey()
        enccontent = FernetCipher.Encrypt(key, content)+self.separator.encode("utf-8")+b64encode(key)

        enccontent = enccontent[::-1]
        enccontent = compress(enccontent)

        return f"exec((_)({enccontent}))"

    def NormalObfuscation(self,content):
        content = content.encode('utf-8')
        content = compress(content)
        content = content[::-1]

        key = FernetCipher.GenKey()
        enccontent = FernetCipher.Encrypt(key, content)+self.separator.encode("utf-8")+key

        enccontent = enccontent[::-1]
        enccontent = compress(enccontent)

        return f"exec((_)({enccontent}))"

    def LiteObfuscation(self,content):
        content = content.encode('utf-8')
        content = compress(content)
        content = content[::-1]

        enccontent = b64encode(content)

        enccontent = enccontent[::-1]
        enccontent = compress(enccontent)

        return f"exec((_)({enccontent}))"

    @staticmethod
    def GenSeperator(length):
        return ''.join(choice(ascii_letters+digits+punctuation) for _ in range(length))