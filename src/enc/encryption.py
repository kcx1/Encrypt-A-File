import sys
from datetime import datetime
from pathlib import PurePath

from cryptography.fernet import Fernet, InvalidToken


class Locker:
    """
    Encrypt and decrypt files using a common key
    """

    def __init__(self, key_name=None, in_mem=False):
        """
        Parameters
        ----------
        key_name : str
            pathlike string or name for generating an encryption key.
        in_mem : bool
            Whether to store key in memory or as a file. If not
            specified, then it will store as a file. If True, a
            file will not be generated.
        """
        self._key_name = key_name  # Name of key / filepath
        self.in_mem = in_mem  # Store in memory - bool
        self._key = self._check_keys()  # Key string
        self._cipher = Fernet(self._key)  # Fernet obj using key string

    def _create_key(self):
        new_key = Fernet.generate_key()
        if not self.in_mem:
            with open(self._key_name, "wb") as key:
                key.write(new_key)
        return new_key

    def _read_key(self):
        with open(self._key_name, "rb") as key:
            return key.read()

    def _check_keys(self):
        if self.in_mem and self._key_name:
            return self._key_name
        if self.in_mem:
            return self._create_key()
        try:
            return self._read_key()
        except FileNotFoundError:
            return self._create_key()

    def set_cipher(self, key):
        """
        Used to set the encryption / decryption key

        Parameters
        ----------

            key : str
                pathlike string used to set the key.
        """
        self._cipher = Fernet(key)

    def encrypt_string(self, input_string, out_file=None):
        # Encrypted String
        result = self._cipher.encrypt(input_string.encode())
        # If an out file was specified
        if out_file:
            _path = PurePath(out_file)
            if _path.suffix:
                _dir, file = str(_path.parent), str(_path.name)
            else:
                now = str(datetime.now)
                _dir, file = str(_path), "encrypted_string" + now
            with open(_dir + file, "wb") as _file:
                _file.writelines((b"Key: " + self._key, b"Encrypted String: " + result))

        return self._key, result

    def encrypt_file(self, file, out_file=True):
        with open(file, "rb") as _file:
            encrypted = self._cipher.encrypt(_file.read())
        if out_file:
            with open(file, "wb") as _file:
                _file.write(encrypted)
        return encrypted.decode("utf-8")  # Return for programtic useage

    def decrypt_string(self, input_string, out_file=None):
        result = self._cipher.decrypt(input_string.encode())
        if out_file:
            with open(out_file, "wb") as _file:
                _file.write(result)
        return result

    def decrypt_file(self, file, out_file=False):
        with open(file, "rb") as _file:
            try:
                decrypted = self._cipher.decrypt(_file.read())
            except InvalidToken as err:
                sys.exit(err, self._key)

        if out_file:
            with open(file, "wb") as _file:
                _file.write(decrypted)

        try:
            return decrypted.decode("utf-8")
        except UnicodeDecodeError as err:
            print("WARNING:", err)
            print("Returning Object as Bytes")
        return decrypted


if __name__ == "__main__":
    # # Example on how to run this module directly #
    #
    # # Create Object
    # e = Locker("Creds/db_creds.key")
    #
    # # Encrypt an existing file
    # e.encrypt_file('/Creds/db_creds', out_file=True)
    #
    # # Decrypt a previosly encrypted file
    # e.decrypt_file('../../Creds/db_creds', out_file=True)
    pass
