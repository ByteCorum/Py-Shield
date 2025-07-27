from cryptography.fernet import Fernet
from zlib import compress, decompress
from base64 import b64encode, b64decode
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from os import urandom

class FernetAlgos:
    @staticmethod
    def GenKey() -> bytes:
        return Fernet.generate_key()

    @staticmethod
    def Encrypt(key: bytes, content: str) -> bytes:
        fernet = Fernet(key)
        return fernet.encrypt(content.encode("utf-8"))

    @staticmethod
    def Decrypt(key: bytes, content: bytes) -> str:
        fernet = Fernet(key)
        return fernet.decrypt(content).decode("utf-8")

class AesAlgos:
    @staticmethod
    def GenKey(length=256) -> bytes:
        if length not in (128, 192, 256):
            raise Exception("AES-GCM: Bit length must be 128, 192, or 256")
        return urandom(length // 8)

    @staticmethod
    def Encrypt(key: bytes, content: str) -> bytes:
        aes = AESGCM(key)
        nonce = urandom(12)
        return nonce + aes.encrypt(nonce, content.encode("utf-8"), associated_data=None)


    @staticmethod
    def Decrypt(key: bytes, content: bytes) -> str:
        aes = AESGCM(key)
        nonce = content[:12]
        ciphertext = content[12:]
        return aes.decrypt(
        nonce,
        ciphertext,
        associated_data=None
        ).decode("utf-8")

class RsaAlgos:
    @staticmethod
    def GenKeyPair() -> tuple[rsa.RSAPrivateKey, rsa.RSAPublicKey]:
        privateKey = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        publicKey = privateKey.public_key()
        return privateKey, publicKey

    @staticmethod
    def SerializePublicKey(publicKey: rsa.RSAPublicKey) -> bytes:
        return publicKey.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
            )

    @staticmethod
    def SerializePrivateKey(privateKey: rsa.RSAPrivateKey, password: bytes = None) -> bytes:
        encryptionAlgo = (
            serialization.BestAvailableEncryption(password) if password else serialization.NoEncryption()
        )

        return privateKey.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=encryptionAlgo
        )

    @staticmethod
    def DeserializePublicKey(serializedKey: bytes) -> rsa.RSAPublicKey:
        return serialization.load_pem_public_key(serializedKey)

    @staticmethod
    def DeserializePrivateKey(serializedKey: bytes, password: bytes = None) -> rsa.RSAPrivateKey:
        return serialization.load_pem_private_key(serializedKey, password=password)

    @staticmethod
    def Encrypt(publicKey: rsa.RSAPublicKey, content: str) -> bytes:
        return publicKey.encrypt(
            content.encode("utf-8"),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None))

    @staticmethod
    def Decrypt(privateKey: rsa.RSAPrivateKey, content: bytes) -> str:
        return privateKey.decrypt(
            content,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None)).decode("utf-8")