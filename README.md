# File Lock
A command line utility for encrypting and decrypting files.

Instead of being password drvien, FileLock uses a URL-safe base64-encoded key that gets stored in the user's home directory. By default the key is stored at ```~/.keys/Default.key``` However, this can be changed by specifying the deisred file location when using FileLock.

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



## Useage

- ##### __Encryption__
This is the default behavior, and only expects 1 arguemnt - The file that you wish to encrypt. By defualt, FileLock will add the extension '.enc' to the file after encrption.


- ##### __Decryption__
To decrypt a file pass the ``` --unlock ``` option along witht the fle that you wish to decrypt. If your file has the '.enc' extention, the unlock option will remove it.
```
filelock
    usage: [OPTIONS] File to encrypt/decrypt

    Quick command line utility to encrypt or decrypt files; Default behavior is to encrypt.

    positional arguments:
      input_file         Specify a file that you wish to encrypt

    options:
      -h, --help         show this help message and exit
      -u, --unlock       Use this option to decrypt the file.
      -k KEY, --key KEY  Specify a specific key to use
      --hide_extension   Do not use the '.enc' extention

