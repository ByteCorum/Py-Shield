from random import choice
from string import ascii_letters, digits, punctuation
from base64 import b64encode
from cryptography.fernet import Fernet
from zlib import compress

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

        key = Fernet.generate_key()
        fernet = Fernet(key)
        enccontent = fernet.encrypt(enccontent)+self.separator.encode("utf-8")+b64encode(key)

        enccontent = enccontent[::-1]
        enccontent = compress(enccontent)

        return f"exec((_)({enccontent}))"

    def MediumObfuscation(self,content):
        content = content.encode('utf-8')
        content = compress(content)
        content = content[::-1]

        key = Fernet.generate_key()
        fernet = Fernet(key)
        enccontent = fernet.encrypt(content)+self.separator.encode("utf-8")+b64encode(key)

        enccontent = enccontent[::-1]
        enccontent = compress(enccontent)

        return f"exec((_)({enccontent}))"

    def NormalObfuscation(self,content):
        content = content.encode('utf-8')
        content = compress(content)
        content = content[::-1]

        key = Fernet.generate_key()
        fernet = Fernet(key)
        enccontent = fernet.encrypt(content)+self.separator.encode("utf-8")+key

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

