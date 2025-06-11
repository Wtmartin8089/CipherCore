import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import base64
import os
import encryptor
import decryptor

class CipherCoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CipherCore - File Encryption & Decryption")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure('TNotebook.Tab', background='#cce6ff', padding=10)
        self.style.configure('TFrame', background='#e6f2ff')
        self.style.configure('TButton', background='#99ccff', foreground='black')
        self.style.configure('TLabel', background='#e6f2ff', font=('Segoe UI', 10))
        self.style.configure('TEntry', fieldbackground='white')

        self.notebook = ttk.Notebook(self.root)
        self.encrypt_tab = ttk.Frame(self.notebook)
        self.decrypt_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.encrypt_tab, text='Encrypt')
        self.notebook.add(self.decrypt_tab, text='Decrypt')
        self.notebook.pack(expand=True, fill='both')

        self.setup_encrypt_tab()
        self.setup_decrypt_tab()

    def setup_encrypt_tab(self):
        frame = ttk.Frame(self.encrypt_tab, padding=20)
        frame.pack(expand=True, fill='both')

        ttk.Label(frame, text="File to Encrypt:").grid(row=0, column=0, sticky='w')
        self.encrypt_file_entry = ttk.Entry(frame, width=50)
        self.encrypt_file_entry.grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(frame, text="Browse", command=self.browse_encrypt_file).grid(row=1, column=1, padx=5)

        ttk.Label(frame, text="Password:").grid(row=2, column=0, sticky='w')
        self.encrypt_password_entry = ttk.Entry(frame, width=50, show='*')
        self.encrypt_password_entry.grid(row=3, column=0, padx=5, pady=5)

        ttk.Button(frame, text="Encrypt", command=self.encrypt_file).grid(row=4, column=0, columnspan=2, pady=10)

    def setup_decrypt_tab(self):
        frame = ttk.Frame(self.decrypt_tab, padding=20)
        frame.pack(expand=True, fill='both')

        ttk.Label(frame, text="Encrypted File:").grid(row=0, column=0, sticky='w')
        self.decrypt_file_entry = ttk.Entry(frame, width=50)
        self.decrypt_file_entry.grid(row=1, column=0, padx=5, pady=5)
        ttk.Button(frame, text="Browse", command=self.browse_decrypt_file).grid(row=1, column=1, padx=5)

        ttk.Label(frame, text="Password:").grid(row=2, column=0, sticky='w')
        self.decrypt_password_entry = ttk.Entry(frame, width=50, show='*')
        self.decrypt_password_entry.grid(row=3, column=0, padx=5, pady=5)

        ttk.Label(frame, text="Salt (Base64):").grid(row=4, column=0, sticky='w')
        self.decrypt_salt_entry = ttk.Entry(frame, width=50)
        self.decrypt_salt_entry.grid(row=5, column=0, padx=5, pady=5)

        ttk.Button(frame, text="Decrypt", command=self.decrypt_file).grid(row=6, column=0, columnspan=2, pady=10)

    def browse_encrypt_file(self):
        file = filedialog.askopenfilename()
        if file:
            self.encrypt_file_entry.delete(0, tk.END)
            self.encrypt_file_entry.insert(0, file)

    def browse_decrypt_file(self):
        file = filedialog.askopenfilename()
        if file:
            self.decrypt_file_entry.delete(0, tk.END)
            self.decrypt_file_entry.insert(0, file)

    def encrypt_file(self):
        filepath = self.encrypt_file_entry.get()
        password = self.encrypt_password_entry.get()
        if not filepath or not password:
            messagebox.showerror("Error", "File and password are required.")
            return
        try:
            salt = encryptor.encrypt_file(filepath, password)
            messagebox.showinfo("Success", f"File encrypted successfully!\n\nSalt (base64):\n{salt}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def decrypt_file(self):
        filepath = self.decrypt_file_entry.get()
        password = self.decrypt_password_entry.get()
        salt = self.decrypt_salt_entry.get()
        if not filepath or not password or not salt:
            messagebox.showerror("Error", "All fields are required.")
            return
        try:
            decryptor.decrypt_file(filepath, password, salt)
            messagebox.showinfo("Success", "File decrypted successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = CipherCoreApp(root)
    root.mainloop()
