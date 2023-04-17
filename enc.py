from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

def encrypt(text, key):
    f = Fernet(key)
    token = f.encrypt(text)
    return token

def isValidKey(key):
    try:
        f = Fernet(key)
        return True
    except Exception as e:
        return False

def decrypt(text, key):
    key = generateKey(key)
    if isValidKey(key):
        pass
    else:
        return 1
    f = Fernet(key)
    token = f.decrypt(text)
    return token

def generateKey(password):
    password_bytes = password.encode('utf-8')
    salt = b'salt'
    kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length = 32,
            salt = salt,
            iterations = 100000
            )
    key = kdf.derive(password_bytes)
    encoded_key = base64.urlsafe_b64encode(key)
    return encoded_key.decode('utf-8')

if __name__ == "__main__":
    print("Run Encrypter from main.py")
