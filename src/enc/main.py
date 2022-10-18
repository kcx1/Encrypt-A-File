#!/usr/bin/env python3
import argparse
import os
from pathlib import PurePath, Path
from sys import exit
from enc.Encryption import Locker


# Constants
HOME = Path.home()
DEFAULT_KEY = os.environ.get("$KEY") or f"{HOME}/.keys/Default.key"


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
    nargs="*",
    help="Specify a file that you wish to encrypt"
)

parser.add_argument(
    "-r",
    "--recursive",
    action="store_true",
    help="Recursively encrypt or decrypt the contents of a directory.",
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


opts = parser.parse_args()


# Exception Handling
def is_file(file):
    if not Path(file).is_file():
        raise Exception(
            f"{file} is either a directory or does not exist. Please check file and try again."
        )
    return True


# Encrytion


def create_lock():
    if not os.path.exists(f"{HOME}/.keys/"):
        os.mkdir(f"{HOME}/.keys")
    return Locker(key_name=opts.key or DEFAULT_KEY)


def encrypt(lock, file):
    is_file(file)  # Exception handling to make sure a file is provided.
    lock.encrypt_file(file, out_file=True)  # Encrypts in place
    if opts.hide_extension:
        os.rename(file, file + ".enc")
    print(f"Encrypting File: {file} \t with key: {opts.key or DEFAULT_KEY}")


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

    is_file(file)  # Exception handling to make sure a file is provided.

    key_name = opts.key or DEFAULT_KEY

    lock.decrypt_file(file, out_file=True)
    if PurePath(file).suffix == ".enc":
        os.rename(file, file[: -len(".enc")])
    print(f"Decrypting File: {file} \t with key: {key_name}")


# Recursive Walk
def recursive(file_dir):
    if opts.recursive and Path(file_dir).is_dir():
        for (dirpath, dirs, files) in os.walk(file_dir, topdown=True):
            if len(files) > 0:
                for file in files:
                    file = os.path.join(dirpath, file)
                    yield file
    yield file_dir


# Main Program
def main():
    for f in opts.input_file:
        for file in recursive(f):
            if opts.unlock:
                decrypt(create_unlock(), file)
            else:
                encrypt(create_lock(), file)


if __name__ == "__main__":
    main()
