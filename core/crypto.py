# core/crypto.py
import os
import nacl.secret
import nacl.utils
import nacl.pwhash.argon2id
import hashlib

class CipherCore:
    def __init__(self, password: str):
        self.salt = nacl.utils.random(nacl.pwhash.argon2id.SALTBYTES)
        self.key = nacl.pwhash.argon2id.kdf(
            nacl.secret.SecretBox.KEY_SIZE,
            password.encode(),
            self.salt,
            opslimit=nacl.pwhash.argon2id.OPSLIMIT_MODERATE,
            memlimit=nacl.pwhash.argon2id.MEMLIMIT_MODERATE
        )
        self.box = nacl.secret.SecretBox(self.key)

    def _hash_data(self, data: bytes) -> bytes:
        return hashlib.sha256(data).digest()

    def encrypt_file(self, input_path: str, output_path: str):
        with open(input_path, 'rb') as f:
            plaintext = f.read()
        file_hash = self._hash_data(plaintext)
        payload = file_hash + plaintext
        nonce = nacl.utils.random(nacl.secret.SecretBox.NONCE_SIZE)
        encrypted = self.box.encrypt(payload, nonce)
        with open(output_path, 'wb') as f:
            f.write(self.salt + encrypted)

    def decrypt_file(self, input_path: str, output_path: str, password: str):
        with open(input_path, 'rb') as f:
            data = f.read()
        salt = data[:nacl.pwhash.argon2id.SALTBYTES]
        encrypted = data[nacl.pwhash.argon2id.SALTBYTES:]
        key = nacl.pwhash.argon2id.kdf(
            nacl.secret.SecretBox.KEY_SIZE,
            password.encode(),
            salt,
            opslimit=nacl.pwhash.argon2id.OPSLIMIT_MODERATE,
            memlimit=nacl.pwhash.argon2id.MEMLIMIT_MODERATE
        )
        box = nacl.secret.SecretBox(key)
        decrypted = box.decrypt(encrypted)
        file_hash, plaintext = decrypted[:32], decrypted[32:]
        if file_hash != self._hash_data(plaintext):
            raise ValueError("File integrity verification failed!")
        with open(output_path, 'wb') as f:
            f.write(plaintext)

