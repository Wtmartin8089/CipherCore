# ui/gui.py
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.filechooser import FileChooserIconView
from kivy.core.window import Window
from core.crypto import CipherCore

# Stealth mode visuals
Window.clearcolor = (0.1, 0.1, 0.1, 1)  # Dark mode background

class CipherScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)

        self.file_chooser = FileChooserIconView(filters=["*.*"])
        self.add_widget(self.file_chooser)

        self.password_input = TextInput(hint_text='Enter Password', password=True, multiline=False)
        self.add_widget(self.password_input)

        self.output_label = Label(text='Select a file, enter password, then choose Encrypt or Decrypt.', size_hint_y=0.1)
        self.add_widget(self.output_label)

        btn_layout = BoxLayout(size_hint_y=0.2, spacing=10)
        encrypt_btn = Button(text='Encrypt')
        decrypt_btn = Button(text='Decrypt')
        encrypt_btn.bind(on_press=self.encrypt_file)
        decrypt_btn.bind(on_press=self.decrypt_file)
        btn_layout.add_widget(encrypt_btn)
        btn_layout.add_widget(decrypt_btn)
        self.add_widget(btn_layout)

    def encrypt_file(self, instance):
        files = self.file_chooser.selection
        if not files:
            self.output_label.text = "[!] No file selected."
            return
        password = self.password_input.text
        if not password:
            self.output_label.text = "[!] Enter a password."
            return
        try:
            core = CipherCore(password)
            input_path = files[0]
            output_path = input_path + ".cph"
            core.encrypt_file(input_path, output_path)
            self.output_label.text = f"[+] Encrypted: {output_path}"
        except Exception as e:
            self.output_label.text = f"[!] Encryption failed: {e}"

    def decrypt_file(self, instance):
        files = self.file_chooser.selection
        if not files:
            self.output_label.text = "[!] No file selected."
            return
        password = self.password_input.text
        if not password:
            self.output_label.text = "[!] Enter a password."
            return
        try:
            core = CipherCore(password)
            input_path = files[0]
            output_path = input_path.replace(".cph", ".dec")
            core.decrypt_file(input_path, output_path, password)
            self.output_label.text = f"[+] Decrypted: {output_path}"
        except Exception as e:
            self.output_label.text = f"[!] Decryption failed: {e}"

class CipherApp(App):
    def build(self):
        return CipherScreen()

if __name__ == '__main__':
    CipherApp().run()

