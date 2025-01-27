## Encryption and Decryption App

A Python-based encryption and decryption application that supports multiple encryption methods, including:
- **Caesar Cipher** (text-based encryption)
- **AES (Advanced Encryption Standard) Encryption** (text-based and image-based encryption)
- **Image Encryption** using AES-256

This application allows you to securely encrypt and decrypt text and image files using different encryption algorithms through a simple command-line interface (CLI).

### Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
  - [Caesar Cipher](#caesar-cipher)
  - [AES Text Encryption](#aes-text-encryption)
  - [AES Image Encryption](#aes-image-encryption)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

---

### Features

- **Caesar Cipher**: A simple shift cipher for encrypting and decrypting text with a specified shift value.
- **AES Text Encryption**: Secure encryption and decryption of text using the AES-256 encryption algorithm.
- **AES Image Encryption**: Encrypt and decrypt image files using AES-256 encryption.
- **Error Handling**: Proper error handling, especially during decryption (e.g., invalid padding, wrong keys).
- **Random Key Generation**: Option to generate random keys for AES encryption.

---

### Installation

To run this app locally, follow these steps:

#### 1. Clone the Repository

```bash
git clone https://github.com/CodeByKalvin/Encodr.git
cd encryption-app
```

#### 2. Install Dependencies

Make sure you have **Python 3** installed. Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

The `requirements.txt` should contain the following:
```txt
pycryptodome
Pillow
```

---

### Usage

Once installed, you can run the application from the command line using:

```bash
python en.py
```

This will launch the CLI, where you can choose to encrypt or decrypt text or images.

---

#### Caesar Cipher

1. **Encryption**: Encrypts text using a shift value.
   - Enter the text you want to encrypt.
   - Provide the shift value (integer).
   
2. **Decryption**: Decrypts text that was encrypted using the Caesar Cipher.
   - Enter the encrypted text.
   - Provide the shift value (integer) used for encryption.

Example:

```bash
Do you want to (E)ncrypt or (D)ecrypt? e
Enter the text: Hello World
Enter the shift value (an integer): 3
Encrypted Text: Khoor Zruog
```

---

#### AES Text Encryption

1. **Encryption**: Encrypts text using AES-256.
   - Enter the text you want to encrypt.
   - Provide a 32-byte key (or generate one randomly).
   
2. **Decryption**: Decrypts text that was encrypted using AES-256.
   - Enter the encrypted text.
   - Provide the same 32-byte key used for encryption.

Example:

```bash
Do you want to (E)ncrypt or (D)ecrypt? e
Enter the text: This is a secret message!
Enter a 32-byte key (or press Enter to generate a random one): 
Generated Key (base64): m1vQ6+wWhh5U6gEJHaYF/O29pFmzF50Na4zCwCBOVH4=
Encrypted Text: KLMtGTANuKZ4Wu1jX7bXOxM8KMDI5F6BpVzAmFDgKaDo/OZNHdxF9Q==
```

---

#### AES Image Encryption

1. **Encryption**: Encrypts image files using AES-256.
   - Provide the path to the image file.
   - Provide a 32-byte key (or generate one randomly).
   - The encrypted image will be saved to the specified output path.

2. **Decryption**: Decrypts an encrypted image file using AES-256.
   - Provide the path to the encrypted image.
   - Provide the same 32-byte key used for encryption.
   - The decrypted image will be saved to the specified output path.

Example:

```bash
Do you want to (E)ncrypt or (D)ecrypt an image? e
Enter the image file path: input_image.png
Enter the output file path: encrypted_image.png
Enter a 32-byte key (or press Enter to generate a random one): 
Generated Key (base64): KDyGxb2b8GujDfeLDvHgzZbI5EqPf+42OLNZJxTNeZs=
Image encrypted successfully! Output file: encrypted_image.png
```

---

### Project Structure

```
encryption-app/
│
├── en.py                   # Main Python script for running the CLI app
├── README.md                # This README file
├── requirements.txt         # List of dependencies
└── images/                  # Folder for testing images (optional)
```

---

### Requirements

- **Python 3** or higher
- **Pip** to install dependencies
- Required Python libraries (in `requirements.txt`):
  - `pycryptodome`: Provides AES encryption and decryption.
  - `Pillow`: To handle image file operations.

To install the dependencies:

```bash
pip install -r requirements.txt
```

---

### Contributing

If you want to contribute to this project, feel free to submit a pull request or create an issue with a detailed description of the feature or bug you're addressing.

#### Steps to Contribute:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Make your changes.
4. Test your changes.
5. Commit your changes (`git commit -m 'Add some feature'`).
6. Push to your branch (`git push origin feature-name`).
7. Create a pull request.

---

### License

This project is open-source and available under the [MIT License](LICENSE).

---

### Future Improvements

- Add support for more encryption algorithms (e.g., RSA).
- Add file-based encryption for documents and other types of files.
- Develop a GUI for non-command-line users.

---

### Authors

- **CodeByKalvin** - *Initial work* - [GitHub Profile](https://github.com/codebykalvin)
