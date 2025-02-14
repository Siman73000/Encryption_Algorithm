import os
from cryptography.fernet import Fernet

def create_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()

def encrypt_file(file_path):
    key = load_key()
    cipher = Fernet(key)

    # Read the original file content
    with open(file_path, "rb") as file:
        plaintext = file.read()

    # Encrypt the file content
    encrypted_text = cipher.encrypt(plaintext)

    # Construct the new file path with "encrypted_" prefix in the same directory
    directory, original_filename = os.path.split(file_path)
    encrypted_file_path = os.path.join(directory, "encrypted_" + original_filename)

    # Write the encrypted content to the new file path
    with open(encrypted_file_path, "wb") as file:
        file.write(encrypted_text)

    print(f"{file_path} encrypted successfully as {encrypted_file_path}")

def decrypt_file(file_path):
    key = load_key()
    cipher = Fernet(key)

    # Read the encrypted file content
    with open(file_path, "rb") as file:
        encrypted_text = file.read()

    # Decrypt the content
    decrypted_text = cipher.decrypt(encrypted_text)

    # Construct the new file path with "decrypted_" prefix in the same directory
    directory, original_filename = os.path.split(file_path)
    decrypted_file_path = os.path.join(directory, "decrypted_" + original_filename)

    # Write the decrypted content to the new file path
    with open(decrypted_file_path, "wb") as file:
        file.write(decrypted_text)

    print(f"{file_path} decrypted successfully as {decrypted_file_path}")

# Usage
create_key()

encrypt_file(r"plainPassword.txt")
decrypt_file(r"encryptedPassword.txt")
