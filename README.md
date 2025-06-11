# 🔐 CipherCore

**CipherCore** is a cross-platform file encryption app forged for serious security and silky simplicity. Built using military-grade ciphers and a clean blue GUI, it lets anyone encrypt or decrypt files with total control — no tech degree required.

![CipherCore](https://raw.githubusercontent.com/WTMartin8089/CipherCore/main/icon/ciphercore.png)

---

## 🚀 Features

- 🔒 **ChaCha20-Poly1305 Encryption** with Argon2id password-based key derivation
- 🧂 Secure salt generation + clipboard copy for smooth decryption
- 🎨 Polished Tkinter GUI with a soft blue theme
- 📁 Encrypt/decrypt any file type — no size restrictions
- ❌ Handles wrong passwords and corrupt files gracefully
- 🧠 Auto-renames output files: `file.enc`, `file.dec`
- 🖼 Integrated desktop launcher + icon (Linux)
- 📦 Distributed as `.deb`, `.apk`, and web-hosted PWA (in progress)

---

## 🖥 Platform Support

| Platform     | Status             |
|--------------|--------------------|
| 🐧 Linux      | ✅ `.deb` complete |
| 🤖 Android    | 🔄 Building via Chaquopy |
| 🍎 iOS (Safari) | 🔜 PWA delivery |
| 💻 Desktop     | ✅ Fully supported |
| 🌐 Web         | 🔄 GitHub Pages landing site in progress |

---

## 📸 Screenshots

Coming soon: UI screenshots, encryption preview, and more.

---

## ⚙ How to Use

1. Run `gui.py`
2. Choose a file to encrypt or decrypt
3. Enter a password
4. On encryption, copy the salt string displayed
5. Use that salt + password for decryption later

---

## 📂 Project Structure

```bash
├── gui.py             # GUI entrypoint (Tkinter)
├── encryptor.py       # File encryption logic
├── decryptor.py       # File decryption logic
├── ciphercore.desktop # Linux desktop entry
├── CHANGELOG.md
├── README.md
└── icon/

