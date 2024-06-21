import os
import getpass
import base64
import secrets
import string
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class PasswordManager:
    def __init__(self, master_password):
        self.master_password = master_password
        self.salt_file = 'salt.txt'
        self.salt = self._get_or_create_salt()
        self.kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(self.kdf.derive(self.master_password.encode()))
        self.fernet = Fernet(key)

    def _get_or_create_salt(self):
        if os.path.exists(self.salt_file):
            with open(self.salt_file, 'rb') as f:
                return f.read()
        else:
            salt = os.urandom(16)
            with open(self.salt_file, 'wb') as f:
                f.write(salt)
            return salt

    def generate_password(self, length=12):
        alphabet = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        return password

    def add_password(self, service, username, password):
        encrypted_password = self.fernet.encrypt(password.encode())
        with open('passwords.txt', 'a') as f:
            f.write(f"{service}:{username}:{encrypted_password.decode()}\n")

    def get_password(self, service, username):
        if not os.path.exists('passwords.txt'):
            return None

        with open('passwords.txt', 'r') as f:
            for line in f:
                svc, usr, encrypted_password = line.strip().split(':')
                if svc == service and usr == username:
                    decrypted_password = self.fernet.decrypt(encrypted_password.encode()).decode()
                    return decrypted_password
        return None

def main():
    master_password = getpass.getpass("Enter master password: ")
    pm = PasswordManager(master_password)

    while True:
        print("1. Generate password")
        print("2. Add password")
        print("3. Get password")
        print("4. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            length = int(input("Enter password length: "))
            password = pm.generate_password(length)
            print(f"Generated password: {password}")

        elif choice == "2":
            service = input("Enter service: ")
            username = input("Enter username: ")
            password = getpass.getpass("Enter password: ")
            pm.add_password(service, username, password)
            print("Password added successfully!")

        elif choice == "3":
            service = input("Enter service: ")
            username = input("Enter username: ")
            password = pm.get_password(service, username)
            if password:
                print(f"Password: {password}")
            else:
                print("Password not found!")

        elif choice == "4":
            break

        else:
            print("Invalid option. Try again!")

if __name__ == "__main__":
    main()
