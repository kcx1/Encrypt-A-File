# File Lock
A command line utility for encrypting and decrypting files.

Instead of being password drvien, FileLock uses a URL-safe base64-encoded 32 byte key that gets stored in the user's home directory. This allows the user to "lock" and "unlock" files without having to use a password. Similar to how ssh keys work (except this is symmetric encryption). 

The goal is to provide secure and fast encryptions that are quick and easy to manage. 

By default the key is stored at ```~/.keys/Default.key``` However, this can be changed by specifying the deisred file location when using FileLock. Additionally, you can set an environmental variable ``` $KEY ``` to use an alternative key persistently. 

## Installation

Even though FileLock is not yet available on pypi, you can still isntall it using pip. 

```bash
pip install git+https://github.com/kcx1/FileLock
```
This will install both the FileLock package and the required dependencies. (Which are very few) Depending on how you have your environment you may need to add it to your $PATH 

In my case it was installed to ``` ~/.local/bin/filelock ```

You can do this by adding this to your shell's rc file i.e *.bashrc* or *.zshrc*

```bash
export PATH=$PATH:$HOME/.local/bin/filelock
```

> **💡 TIP:** Here's a oneliner if you use a basic zsh config
> ```bash
> echo  "export PATH=$PATH:$HOME/.local/bin/filelock" >> ~/.zshrc
> ```



## Usage

- ##### __Encryption__
This is the default behavior, and only expects 1 arguemnt - The file that you wish to encrypt. However you can specify mulitple files as long as they seperated by a space. Alternatively, you can encrypt a directory recursively by passing the ``` --recursive ``` option. By defualt, FileLock will add the extension '.enc' to the file after encrption.


- ##### __Decryption__
To decrypt a file pass the ``` --unlock ``` option along witht the fle that you wish to decrypt. Just like when encrypting, you can pass multiple files or use the ``` --recursive ``` option to iterate through entire directories. If your file has the '.enc' extention, then the ``` --unlock ``` option will remove it.
```
filelock
    Usage: [OPTIONS] File to encrypt/decrypt

    Quick command line utility to encrypt or decrypt files; Default behavior is to encrypt.

    positional arguments:
      input_file         Specify a file that you wish to encrypt

    options:
      -h, --help         show this help message and exit
      -r, --recursive    Recursively encrypt or decrypt the contents of a directory.
      -u, --unlock       Use this option to decrypt the file.
      -k KEY, --key KEY  Specify a specific key to use
      --hide_extension   Do not use the '.enc' extention

