from cryptography.fernet import Fernet

def encrypt(text):
    key = Fernet.generate_key()
    f = Fernet(key)
    text = text
    token = f.encrypt(text)
    return [token, key]

def isValidKey(key):
    try:
        f = Fernet(key)
        return True
    except Exception as e:
        return False

def decrypt(text, key):
    if isValidKey(key):
        pass
    else:
        return 1
    f = Fernet(key)
    token = f.decrypt(text)
    return token

if __name__ == "__main__":
    print("Run Encrypter from main.py")
