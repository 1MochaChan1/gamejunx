import hashlib

def encode_password(text:str)->str:
    encrypted_string:str= hashlib.md5(text.encode('utf')).hexdigest()
    return encrypted_string