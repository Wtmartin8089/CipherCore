# 📜 CipherCore Changelog

## [v1.0.0] – Initial Release

### ✅ Features
- Password-based encryption using **ChaCha20-Poly1305** with Argon2id key derivation
- Secure salt generation and auto display on encryption
- Simple, polished **Tkinter GUI** with soft blue theme
- Easy file selection and encryption/decryption buttons
- Error handling for wrong passwords or corrupted files
- Smart file output names (`filename.enc`, `filename.dec`)
- Auto-copy support for salt (clipboard)
- Flat app icon integrated (64x64 PNG)
- `.desktop` launcher file for system menu integration

### ⚙ Platform Support
- Linux (.deb packaged)
- Android (.apk planned via Chaquopy)
- iOS via PWA (planned for Apple distribution)

### 🛠 Development Utilities
- `encryptor.py`, `decryptor.py`, and `gui.py` managed as core logic
- System menu integration with `ciphercore.desktop`
- GitHub-ready release folder with compiled `.deb`
