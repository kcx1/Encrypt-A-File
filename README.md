# Admin Management
These scripts provide an easy way to manage various parts of the project.

###Encryption
- decrypt.py
- encrypt.py

These allow admins to quickly encrypt or decrypt the contents of a file.

######Encrypt.py
    usage: [OPTIONS] encrypt a string

    positional arguments:
      input_string      write the file that you wish to encrypt

    options:
      -k, --key   Specify a file to use for the key 

######Decrypt.py
    usage: [OPTIONS] encrypt a string

    positional arguments:
      key                   Provide encryption key
      encrypted_string      Prove string or file to decrypt


    options:
      -f, --file_path       Specify an output file

**Warning!** If the output file is not specified then it the string will only be returned in the terminal. 
