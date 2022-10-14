#!/usr/bin/env python3
import argparse
import os
from pathlib import PurePath, Path
from sys import exit
from FileLock.Encryption import Locker


# Constants
HOME = Path.home()
DEFAULT_KEY = f"{HOME}/.keys/Default.key"


parser = argparse.ArgumentParser(
    prog="File Encryption Tool",
    usage="[OPTIONS] File to encrypt/decrypt",
    description="""
        Quick command line utility to encrypt or decrypt files;
        Default behavior is to encrypt.
        """,
)

parser.add_argument(
    "input_file",
    action="store",
    type=str,
    help="Specify a file that you wish to encrypt"
    # TODO: Make sure that any number of files can be passed
)

parser.add_argument(
    "-u", "--unlock", action="store_true", help="Use this option to decrypt the file."
)

parser.add_argument(
    "-k", "--key", type=str, action="store", help="Specify a specific key to use"
)

parser.add_argument(
    "--hide_extension", action="store_false", help="Do not use the '.enc' extention"
)

parser.add_argument(
    "-r",
    "--recursive",
    action="store_true",
    help="Recursively encrypt or decrypt the contents of a directory.",
)

opts = parser.parse_args()


# Encrytion


def create_lock():
    if not os.path.exists(f"{HOME}/.keys/"):
        os.mkdir(f"{HOME}/.keys")
    return Locker(key_name=opts.key or DEFAULT_KEY)


def encrypt(lock, file):
    lock.encrypt_file(file, out_file=True)  # Encrypts in place
    if opts.hide_extension:
        os.rename(file, file + ".enc")
    print(f"File {file} has been encrypted using {opts.key or DEFAULT_KEY}")


# Decryption


def create_unlock():
    if not opts.key and not os.path.exists(DEFAULT_KEY):
        print(
            """
            No encryption keys found.
            Please create a key or specify the key using the '--key' option
            """
        )
        exit("No key found")
    return Locker(key_name=opts.key or f"{HOME}/.keys/Default.key")


def decrypt(lock, file):

    key_name = opts.key or DEFAULT_KEY

    # with open(key_name, "rb") as f:
    #     key = f.read()
    #     lock.set_cipher(key)

    lock.decrypt_file(file, out_file=True)
    if PurePath(file).suffix == ".enc":
        os.rename(file, file[: -len(".enc")])
    print(f"File {file} has been decrypted using {key_name}")


# Recursive Walk


# Main Program


def main():
    if opts.unlock:
        decrypt(create_unlock(), opts.input_file)
    else:
        encrypt(create_lock(), opts.input_file)


if __name__ == "__main__":
    main()
