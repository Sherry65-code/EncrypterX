from enc import encrypt, decrypt, isValidKey, generateKey
from sys import exit
from dynamics import printEquals, clear
from random import randint
from pyperclip import copy

try:
    from colorama import init, Fore, Back, Style
except Exception as e:
    print("colorama not avaliable.\nInstall using - \npip install colorama")
    exit(1)

init()

clear()

while True:
    try:
        rnum = randint(1,4)
        if rnum == 1:
            print(Back.GREEN, end="")
        elif rnum == 2:
            print(Back.RED, end="")
        elif rnum == 3:
            print(Back.MAGENTA, end="")
        elif rnum == 4:
            print(Back.BLUE, end="")
        print(Style.BRIGHT, end="")
        printEquals(10)
        print("ENCRYPTERX", end="")
        printEquals(10)
        print(Style.RESET_ALL, end="")
        print()
        print(f"CHOOSE ONE OPTION\n{Fore.GREEN}{Style.BRIGHT}1{Style.RESET_ALL} - Encrypt\n{Fore.RED}{Style.BRIGHT}2{Style.RESET_ALL} - Decrypt")
        op = input(f"{Fore.GREEN}{Style.BRIGHT}>>{Style.RESET_ALL}")
        if op == "1":
            txt = input("Type text to Encrypt:")
            password = input("Type key for encryption:")
            print(f"{Fore.GREEN}{Style.BRIGHT}ENCRYPTED TEXT{Style.RESET_ALL}")
            if password == "":
                print(f"{Fore.RED}{Style.BRIGHT}WARNING: No password entered{Style.RESET_ALL}")
            else:
                key = generateKey(password)
            txt2 = txt.encode()
            enc = encrypt(txt2, key)
            print(enc.decode())
            copy(enc.decode())
            input()
            clear()
        elif op == "2":
            txt = input("Type text to decode:")
            key = input("Type key for decoding:")
            txt2 = txt.encode()
            enc = decrypt(txt2, key)
            print(f"{Fore.GREEN}{Style.BRIGHT}DECRYPTED TEXT{Style.RESET_ALL}")
            print(enc.decode())
            copy(enc.decode())
            input()
            clear()
        else:
            print(f"{Fore.RED}{Style.BRIGHT}Wrong Option{Style.RESET_ALL}")
        clear()
    except KeyboardInterrupt:
        clear()
        exit(0)
    except Exception as e:
        #clear()
        print(e)
        exit(0)
