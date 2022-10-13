# File Lock
A command line utility for encrypting and decrypting files.

Instead of being password drvien, FileLock uses a URL-safe base64-encoded key that gets stored in the user's home directory. By default the key is stored at ```~/.keys/Default.key``` However, this can be changed by specifying the deisred file location when using FileLock.

### Encryption
This is the default behavior, and only expects 1 arguemnt - The file that you wish to encrypt. 

These allow admins to quickly encrypt or decrypt the contents of a file.

###### Encrypt.py
    usage: [OPTIONS] encrypt a string

    positional arguments:
      input_string      write the file that you wish to encrypt

    options:
      -k, --key   Specify a file to use for the key 

###### Decrypt.py
    usage: [OPTIONS] encrypt a string

    positional arguments:
      key                   Provide encryption key
      encrypted_string      Prove string or file to decrypt


    options:
      -f, --file_path       Specify an output file

**Warning!** If the output file is not specified then it the string will only be returned in the terminal. 
