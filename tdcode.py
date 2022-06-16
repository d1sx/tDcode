#!/bin/python3
import hashlib, sys

op = int(input('''
                   |dCode the planet|
|=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-|
||  ████████╗██████╗  ██████╗ ██████╗ ██████╗ ███████╗  ||
 |  ╚══██╔══╝██╔══██╗██╔════╝██╔═══██╗██╔══██╗██╔════╝  |
 |     ██║   ██║  ██║██║     ██║   ██║██║  ██║█████╗    |
 |     ██║   ██║  ██║██║     ██║   ██║██║  ██║██╔══╝    |
 |     ██║   ██████╔╝╚██████╗╚██████╔╝██████╔╝███████╗  |
 |     ╚═╝   ╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝  |
 |                                                      |
 |   [1] - decryptor                   [2] - encryptor  |
 |                      author: d1sx                    |
 |______________________________________________________|  discord: d1sx#0605

 select (1/2): '''))
print('[!] - loading wordlist...')
if op == 1:
    try:
        file = sys.argv[1]; file = open(file, "r", encoding="ISO-8859-1")
        wordlist = file.read().split(); file.close()
    except:
        print(f'[!] - [ ERRO ] - undefined wordlist!\n\tpython3 {sys.argv[0]} wordlist.txt'); exit()
    cmd = int(input('''\t[1] MD5\n\t[2] SHA1\n\t[3] SHA224\n\t[4] SHA256\n\t[5] SHA384\n\t[6] SHA512\n\t--> '''))
    if cmd == 1:
        hash0 = str(input('Hash: '))
        for password in wordlist:
            hash_d = hashlib.md5(password.encode()).hexdigest()
            if hash0 == hash_d:
                print(f'Decrypted: {password}'); exit()
    elif cmd == 2:
        hash0 = str(input('Hash: '))
        for password in wordlist:
            hash_d = hashlib.sha1(password.encode()).hexdigest()
            if hash0 == hash_d:
                print(f'Decrypted: {password}'); exit()
    elif cmd == 3:
        hash0 = str(input('Hash: '))
        for password in wordlist:
            hash_d = hashlib.sha224(password.encode()).hexdigest()
            if hash0 == hash_d:
                print(f'Decrypted: {password}'); exit()
    elif cmd == 4:
        hash0 = str(input('Hash: '))
        for password in wordlist:
            hash_d = hashlib.sha256(password.encode()).hexdigest()
            if hash0 == hash_d:
                print(f'Decrypted: {password}'); exit()
    elif cmd == 5:
        hash0 = str(input('Hash: '))
        for password in wordlist:
            hash_d = hashlib.sha384(password.encode()).hexdigest()
            if hash0 == hash_d:
                print(f'Decrypted: {password}'); exit()
    elif cmd == 6:
        hash0 = str(input('Hash: '))
        for password in wordlist:
            hash_d = hashlib.sha512(password.encode()).hexdigest()
            if hash0 == hash_d:
                print(f'Decrypted: {password}'); exit()
elif op == 2:
    try:
        xxx = str(input('Hash: '))
    except:
        print('It is necessary to define a hash to encrypt'); exit()
    print('md5: ', hashlib.md5(xxx.encode()).hexdigest())
    print('sha1: ', hashlib.sha1(xxx.encode()).hexdigest())
    print('sha224: ', hashlib.sha224(xxx.encode()).hexdigest())
    print('sha256: ', hashlib.sha256(xxx.encode()).hexdigest())
    print('sha384: ', hashlib.sha384(xxx.encode()).hexdigest())
    print('sha512: ', hashlib.sha512(xxx.encode()).hexdigest())    


# 02/10/2021
# by: d1sx
