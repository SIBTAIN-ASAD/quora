'''
This file contains the common functions to encrypt and decrypt the tokens
'''
# import base64
# from django.conf import settings
# from cryptography.fernet import Fernet

# # Pad and encode key as URL-safe base64 string
# def encode_key(key: str) -> bytes:
#     padded_key = key.ljust(32, '=')  # Pad the key if needed
#     return base64.urlsafe_b64encode(padded_key.encode())

# def encrypt(cleartext: str) -> str:
#     '''
#     Function to encrypt cleartext
#     '''
#     key = settings.ENCRYPT_KEY
#     encoded_key = encode_key(key)
#     f = Fernet(encoded_key)
#     return f.encrypt(cleartext.encode()).decode()

# def decrypt(ciphertext: str) -> str:
#     '''
#     Function to decrypt ciphertext
#     '''
#     key = settings.ENCRYPT_KEY
#     encoded_key = encode_key(key)
#     f = Fernet(encoded_key)
#     return f.decrypt(ciphertext.encode()).decode()


# from django.conf import settings
# from Crypto.Cipher import AES

# def adjust_key_length(key: str) -> bytes:
#     '''
#     Function to adjust the length of the key
#     '''
#     key = key.ljust(32, '=')  # Pad the key if needed
#     return key.encode()

# def encrypt(cleartext: str) -> str:
#     '''
#     Function to encrypt cleartext
#     '''
#     key = settings.ENCRYPT_KEY
#     key = adjust_key_length(key)
#     cipher = AES.new(key, AES.MODE_EAX)
#     nonce = cipher.nonce
#     ciphertext, tag = cipher.encrypt_and_digest(cleartext.encode('utf-8'))  # Encode cleartext to bytes
#     return (nonce + ciphertext + tag).hex()

# def decrypt(ciphertext: str) -> str:
#     '''
#     Function to decrypt ciphertext
#     '''
#     key = settings.ENCRYPT_KEY
#     key = adjust_key_length(key)
#     ciphertext = bytes.fromhex(ciphertext)
#     nonce = ciphertext[:16]
#     tag = ciphertext[-16:]
#     ciphertext = ciphertext[16:-16]
#     cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
#     return cipher.decrypt_and_verify(ciphertext, tag).decode('utf-8')  # Decode decrypted bytes to string

from Crypto.Cipher import Salsa20
from django.conf import settings

def adjust_key_length(key: str) -> bytes:
    '''
    Function to adjust the length of the key
    '''
    key = key.ljust(32, '=')  # Pad the key if needed
    return key.encode()

def encrypt(cleartext: str) -> str:
    '''
    Function to encrypt cleartext
    '''
    key = settings.ENCRYPT_KEY
    key = adjust_key_length(key)
    cipher = Salsa20.new(key)
    nonce = cipher.nonce
    ciphertext = cipher.encrypt(cleartext.encode('utf-8'))  # Encode cleartext to bytes
    return (nonce + ciphertext).hex()

def decrypt(ciphertext: str) -> str:
    '''
    Function to decrypt ciphertext
    '''
    key = settings.ENCRYPT_KEY
    key = adjust_key_length(key)
    ciphertext = bytes.fromhex(ciphertext)
    nonce = ciphertext[:8]
    ciphertext = ciphertext[8:]
    cipher = Salsa20.new(key, nonce=nonce)
    return cipher.decrypt(ciphertext).decode('utf-8')  # Decode decrypted bytes to string