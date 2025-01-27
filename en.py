import os
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
from PIL import Image

# ----------------------------- Caesar Cipher (codebykalvin) -----------------------------
def caesar_cipher_encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            # Encrypt uppercase characters
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            # Encrypt lowercase characters
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Leave non-alphabet characters as-is
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    # Decrypt by using a negative shift
    return caesar_cipher_encrypt(text, -shift)

# ----------------------------- AES Encryption (codebykalvin) -----------------------------
def aes_encrypt(plaintext, key):
    iv = get_random_bytes(16)  # Generate a random IV
    cipher = AES.new(key, AES.MODE_CBC, iv)  # AES-CBC mode
    padded_plaintext = pad(plaintext.encode('utf-8'), AES.block_size)  # Add padding
    ciphertext = cipher.encrypt(padded_plaintext)
    return base64.b64encode(iv + ciphertext).decode('utf-8')

def aes_decrypt(ciphertext, key):
    ciphertext = base64.b64decode(ciphertext)
    iv = ciphertext[:16]  # Extract IV from the beginning
    ciphertext = ciphertext[16:]  # Actual encrypted content
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext = cipher.decrypt(ciphertext)
    return unpad(padded_plaintext, AES.block_size).decode('utf-8')

# ----------------------------- Image Encryption (codebykalvin) -----------------------------
def image_to_bytes(image_path):
    # Open the image and convert it to bytes
    with open(image_path, 'rb') as f:
        return f.read()

def bytes_to_image(data, output_path):
    # Write bytes to an image file
    with open(output_path, 'wb') as f:
        f.write(data)

def aes_encrypt_image(image_path, key, output_path):
    # Read image bytes
    image_data = image_to_bytes(image_path)
    iv = get_random_bytes(16)  # Generate a random IV
    cipher = AES.new(key, AES.MODE_CBC, iv)  # AES-CBC mode
    padded_image_data = pad(image_data, AES.block_size)  # Pad the image data
    encrypted_data = cipher.encrypt(padded_image_data)
    # Save the encrypted image with the IV prepended
    bytes_to_image(iv + encrypted_data, output_path)

# ----------------------------- Updated Image Decryption (codebykalvin) -----------------------------
def aes_decrypt_image(encrypted_image_path, key, output_path):
    encrypted_data = image_to_bytes(encrypted_image_path)

    # Extract the IV (initialization vector) from the first 16 bytes
    iv = encrypted_data[:16]
    
    # The rest is the actual encrypted data
    encrypted_data = encrypted_data[16:]

    # Decrypt with the same key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    try:
        decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
        # Save decrypted image
        bytes_to_image(decrypted_data, output_path)
        print(f"Image decrypted successfully! Output file: {output_path}")
    except ValueError as e:
        print(f"Decryption failed: {e}")

# ----------------------------- Simple CLI (codebykalvin) -----------------------------
def main():
    print("Welcome to the Encryption/Decryption App! (by codebykalvin)")
    print("Choose an option:")
    print("1. Caesar Cipher (Text)")
    print("2. AES Encryption (Text)")
    print("3. AES Encryption (Image)")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        caesar_cli()
    elif choice == "2":
        aes_cli()
    elif choice == "3":
        image_cli()
    else:
        print("Invalid choice!")

# ----------------------------- Caesar Cipher CLI (codebykalvin) -----------------------------
def caesar_cli():
    action = input("Do you want to (E)ncrypt or (D)ecrypt? ").lower()
    text = input("Enter the text: ")

    # Input validation for the shift value
    while True:
        try:
            shift = int(input("Enter the shift value (an integer): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for the shift value.")

    if action == 'e':
        encrypted_text = caesar_cipher_encrypt(text, shift)
        print(f"Encrypted Text: {encrypted_text}")
    elif action == 'd':
        decrypted_text = caesar_cipher_decrypt(text, shift)
        print(f"Decrypted Text: {decrypted_text}")
    else:
        print("Invalid option!")

# ----------------------------- AES Text CLI (codebykalvin) -----------------------------
def aes_cli():
    action = input("Do you want to (E)ncrypt or (D)ecrypt? ").lower()
    text = input("Enter the text: ")
    key = input("Enter a 32-byte key (or press Enter to generate a random one): ")

    if not key:
        key = get_random_bytes(32)  # Generate a random 32-byte key for AES-256
        print(f"Generated Key (base64): {base64.b64encode(key).decode('utf-8')}")
    else:
        key = base64.b64decode(key)

    if len(key) != 32:
        print("Invalid key length. Key must be 32 bytes.")
        return

    if action == 'e':
        encrypted_text = aes_encrypt(text, key)
        print(f"Encrypted Text: {encrypted_text}")
    elif action == 'd':
        decrypted_text = aes_decrypt(text, key)
        print(f"Decrypted Text: {decrypted_text}")
    else:
        print("Invalid option!")

# ----------------------------- AES Image CLI (codebykalvin) -----------------------------
def image_cli():
    action = input("Do you want to (E)ncrypt or (D)ecrypt an image? ").lower()
    image_path = input("Enter the image file path: ")
    output_path = input("Enter the output file path: ")
    key = input("Enter a 32-byte key (or press Enter to generate a random one): ")

    if not key:
        key = get_random_bytes(32)  # Generate a random AES-256 key
        print(f"Generated Key (base64): {base64.b64encode(key).decode('utf-8')}")
    else:
        key = base64.b64decode(key)

    if len(key) != 32:
        print("Invalid key length. Key must be 32 bytes.")
        return

    if action == 'e':
        aes_encrypt_image(image_path, key, output_path)
        print(f"Image encrypted successfully! Output file: {output_path}")
    elif action == 'd':
        aes_decrypt_image(image_path, key, output_path)
    else:
        print("Invalid option!")

if __name__ == "__main__":
    main()
