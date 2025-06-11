# decryptor.py
import sys
import base64
from getpass import getpass
from nacl.secret import SecretBox
from nacl.exceptions import CryptoError
from nacl.pwhash import argon2id

def main():
    if len(sys.argv) < 2:
        print("Usage: python decryptor.py <file_to_decrypt>")
        sys.exit(1)

    enc_file = sys.argv[1]

    password = getpass("🔑 Enter the decryption password: ").encode()
    salt_b64 = input("🧂 Enter the salt (base64): ")
    salt = base64.b64decode(salt_b64)

    key = argon2id.kdf(
        SecretBox.KEY_SIZE, password, salt,
        opslimit=argon2id.OPSLIMIT_MODERATE,
        memlimit=argon2id.MEMLIMIT_MODERATE
    )

    box = SecretBox(key)

    with open(enc_file, "rb") as f:
        blob = f.read()

    try:
        salt_size = argon2id.SALTBYTES
        nonce_size = SecretBox.NONCE_SIZE

        nonce = blob[salt_size : salt_size + nonce_size]
        ciphertext = blob[salt_size + nonce_size:]

        decrypted = box.decrypt(ciphertext, nonce)
        output_file = enc_file.replace(".enc", ".dec")

        with open(output_file, "wb") as f:
            f.write(decrypted)

        print(f"[SUCCESS] Decrypted ➜ '{output_file}'")
    except CryptoError:
        print("[ERROR] Decryption failed. Wrong password or corrupt file.")

if __name__ == "__main__":
    main()

