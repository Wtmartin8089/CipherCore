# 🔐 CipherCore

**CipherCore** is your no-nonsense, ultra-secure file encryption app — engineered for everyday warriors who value **privacy, simplicity, and power**.

---

## 🚀 Features

- 🔒 Military-grade encryption with **ChaCha20-Poly1305**
- 🧠 Password-to-key protection via **Argon2id**
- 🎨 Clean GUI with soft blue theme (built with Tkinter)
- 💾 Secure encryption & decryption for any file type
- ✂️ Auto-generates smart file names (.enc / .dec)
- 📋 Salt displayed *and* copied automatically on encryption
- 📁 Cross-platform packaging: Linux, Android, iOS (PWA)

---

## 🖥 Platform Support

| Platform | Status    |
|----------|-----------|
| Linux    | ✅ Packaged as `.deb` installer |
| Android  | ✅ Buildable via [Chaquopy] integration |
| iOS      | 🔜 Launching via PWA for full Apple support |

---

## ⚙ How to Use

1. **Launch** the GUI (`gui.py`)
2. Select a file → Choose to encrypt or decrypt
3. Enter password + copy the salt when encrypting
4. Use the salt & password combo to decrypt later

---

## 📂 File Structure

- `encryptor.py` – Handles encryption logic
- `decryptor.py` – Handles decryption logic
- `gui.py` – Full GUI interface
- `ciphercore.desktop` – Adds CipherCore to Linux system menu
- `CHANGELOG.md` – Detailed changelog
- `README.md` – This file

---

## 🤝 Credits

Built with ❤️ by **Wayne Martin**  
GitHub: [WTMartin8089](https://github.com/WTMartin8089)

