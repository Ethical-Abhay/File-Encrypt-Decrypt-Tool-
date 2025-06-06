from cryptography.fernet import Fernet

# Load key from file
def load_key():
    return open("key.key", "rb").read()

# Encrypt file
def encrypt_file(file_name):
    key = load_key()
    fernet = Fernet(key)

    with open(file_name, "rb") as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(file_name, "wb") as file:
        file.write(encrypted)
    print(f"{file_name} encrypted successfully!")

# Decrypt file
def decrypt_file(file_name):
    key = load_key()
    fernet = Fernet(key)

    with open(file_name, "rb") as file:
        encrypted = file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(file_name, "wb") as file:
        file.write(decrypted)
    print(f"{file_name} decrypted successfully!")

# Driver code
if __name__ == "__main__":
    print("1. Encrypt\n2. Decrypt")
    choice = input("Enter your choice: ")

    file_name = input("Enter file name (with extension): ")

    if choice == "1":
        encrypt_file(file_name)
    elif choice == "2":
        decrypt_file(file_name)
    else:
        print("Invalid choice")
