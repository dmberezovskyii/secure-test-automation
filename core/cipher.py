import secrets
import string
import pathlib
from typing import Optional, Literal
from cryptography.fernet import Fernet, InvalidToken
import logging


class Cipher:
    def __init__(
        self,
        base_path: Optional[pathlib.Path] = None,
        key_file_name: str = "key.properties",
        vault_type: Literal["vault", "local", "vault_local"] = "vault_local",
    ):
        """
        Initialize the Cipher class with key management and password encryption/decryption functionality.

        Args:
            base_path (Optional[pathlib.Path]): The directory where the key file is located.
                                                 Defaults to the "config" directory adjacent to this script.
            key_file_name (str): The name of the key file. Defaults to "key.properties".
            vault_type (Literal["vault", "local", "vault_local"]): Determines the type of vault for storing keys.
                                                                  Currently supports only "local" for file-based keys.

        """
        self.base_path = (
            base_path or pathlib.Path(__file__).resolve().parent.parent / "config"
        )
        self.key_file_path = self.base_path / key_file_name
        self.vault_type = vault_type

        # Initialize the fernet key if needed
        if vault_type == "local":
            self.fernet = Fernet(self._load_key())
        else:
            self.fernet = None  # Placeholder for other vault types
            # TODO: Add logic for other vault types

    def _load_key(self) -> bytes:
        """
        Read the encryption key from the key file.

        Returns:
            bytes: The encryption key.

        Raises:
            FileNotFoundError: If the key file does not exist.
            ValueError: If the key file is empty.
            RuntimeError: If there is any other issue reading the key.
        """
        if not self.key_file_path.exists():
            raise FileNotFoundError(f"Key file not found at {self.key_file_path}")
        if self.key_file_path.stat().st_size == 0:
            raise ValueError(f"The key file at {self.key_file_path} is empty.")

        try:
            with open(self.key_file_path, "rb") as key_file:
                return key_file.read()
        except Exception as e:
            raise RuntimeError(f"An error occurred while loading the key: {e}")

    def _create_key(self) -> bytes:
        """
        Generate and return a new encryption key.

        Returns:
            bytes: The newly generated encryption key.
        """
        return Fernet.generate_key()

    def _save_key(self, key: Optional[bytes] = None) -> bytes:
        """
        Save the encryption key to the key file.

        Args:
            key (Optional[bytes]): The key to save. If None, a new key is generated.

        Returns:
            bytes: The saved encryption key.
        """
        self.key_file_path.parent.mkdir(parents=True, exist_ok=True)
        key = key or self._create_key()

        with open(self.key_file_path, "wb") as key_file:
            key_file.write(key)
        return key

    def delete_key(self):
        """
        Delete the encryption key file.

        Raises:
            FileNotFoundError: If the key file does not exist.
        """
        try:
            if self.key_file_path.exists():
                self.key_file_path.unlink()
                self.key_file_path.touch()  # Recreate an empty file to maintain structure
            else:
                raise FileNotFoundError(
                    f"Key file not found at {self.key_file_path}"
                )
        except Exception as e:
            logging.error(f"Failed to delete key: {e}")
            raise

    def encrypt(self, password: str) -> bytes:
        """
        Encrypt a password using the fernet key.

        Args:
            password (str): The password to encrypt.

        Returns:
            bytes: The encrypted password.

        Raises:
            ValueError: If the password is an empty string.
        """
        if not password:
            raise ValueError("Password must be a non-empty string.")
        return self.fernet.encrypt(password.encode("utf-8"))

    def decrypt(self, encrypted_pass: bytes) -> str:
        """
        Decrypt an encrypted password.

        Args:
            encrypted_pass (bytes): The encrypted password.

        Returns:
            str: The decrypted password.

        Raises:
            ValueError: If the password is invalid or corrupted.
        """
        try:
            return self.fernet.decrypt(encrypted_pass).decode("utf-8")
        except InvalidToken:
            raise ValueError("Invalid or corrupted encrypted password.")

    def generate_password(self, length: int = 12) -> str:
        """
        Generate a random password of a specified length.

        Args:
            length (int): The length of the generated password. Defaults to 12.

        Returns:
            str: A randomly generated password.

        Raises:
            ValueError: If the length is non-positive.
        """
        if length <= 0:
            raise ValueError("Password length must be a positive integer.")
        return "".join(
            secrets.choice(string.ascii_letters + string.digits)
            for _ in range(length)
        )
