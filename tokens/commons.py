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
#     # Encode cleartext to bytes
#     ciphertext, tag = cipher.encrypt_and_digest(cleartext.encode('utf-8'))
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
#     # Decode decrypted bytes to string
#     return cipher.decrypt_and_verify(ciphertext, tag).decode('utf-8')





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






# import base64
# from Crypto.Cipher import AES
# from Crypto.Util.Padding import pad,unpad
# from Crypto.Random import get_random_bytes
# from django.conf import settings

# #CBC mode with random IV

# def encrypt(data):
#         '''
#         Function to encrypt data
#         '''
#         key = settings.ENCRYPT_KEY
#         #Random IV more secure
#         iv =  get_random_bytes(16) #16 char for AES128

#         data = pad(data.encode(),16)
#         cipher = AES.new(key.encode('utf-8'),AES.MODE_CBC,iv)
#         print('random IV : ' , base64.b64encode(cipher.iv).decode('utf-8'))
#         return base64.b64encode(cipher.encrypt(data)),base64.b64encode(cipher.iv).decode('utf-8')

# def decrypt(enc):
#         '''
#         Function to decrypt data
#         '''
#         #Random IV more secure
#         iv =  get_random_bytes(16) #16 char for AES128
#         key = settings.ENCRYPT_KEY

#         enc = base64.b64decode(enc)
#         cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, base64.b64decode(iv))
#         return unpad(cipher.decrypt(enc),16)
