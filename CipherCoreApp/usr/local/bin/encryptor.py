import os
import base64
import getpass
from nacl.secret import SecretBox
from nacl.utils import random as nacl_random
from nacl.pwhash import argon2id

def derive_key(password: str, salt: bytes) -> bytes:
    return argon2id.kdf(
        SecretBox.KEY_SIZE,
        password.encode(),
        salt,
        opslimit=argon2id.OPSLIMIT_MODERATE,
        memlimit=argon2id.MEMLIMIT_MODERATE
    )

def encrypt_file(filename):
    password = getpass.getpass("🔐 Enter a password to encrypt: ")
    salt = nacl_random(argon2id.SALTBYTES)
    key = derive_key(password, salt)

    box = SecretBox(key)
    nonce = nacl_random(SecretBox.NONCE_SIZE)

    with open(filename, 'rb') as f:
        plaintext = f.read()

    ciphertext = box.encrypt(plaintext, nonce)

    out_filename = f"{filename}.enc"
    with open(out_filename, 'wb') as f:
        f.write(salt + ciphertext.nonce + ciphertext.ciphertext)

    print(f"[SUCCESS] Encrypted '{filename}' ➔ '{out_filename}'")
    print(f"[INFO] Store this salt to decrypt: {base64.b64encode(salt).decode()}")

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Usage: python encryptor.py <filename>")
    else:
        encrypt_file(sys.argv[1])

