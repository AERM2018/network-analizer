from ast import arg
from random import randint
import threading
from helpers import http
from cryptocode import encrypt, decrypt
import hashlib
import colorama


class Criptography_executor():
    def __init__(self):
        colorama.init()
        self.letters = 'abcdefghijklmnopqrstuvwxyz'
        self.numbers = '0123456789'

    def exec_cipher(self,text):
        shift = 3  # defining the shift count
        encryption = ""
        for c in text:
            # check if character is an uppercase letter
            if c.isupper():
                # find the position in 0-25
                c_unicode = ord(c)
                c_index = ord(c) - ord("A")
            # perform the shift
                new_index = (c_index + shift) % 26
            # convert to new character
                new_unicode = new_index + ord("A")
                new_character = chr(new_unicode)
            # append to encrypted string
                encryption = encryption + new_character
            else:
                # since character is not uppercase, leave it as it is
                encryption += c
        print(colorama.Fore.WHITE+'Generated cipher: ',encryption)

    def generate_key(self):
        key = ''
        for i in range(16):
            if i in (4, 8, 12, 16): key += '-'
            if randint(0,1) == 0:
                l = list(self.letters)
                key += l[randint(0,len(l)-1)]
            else:
                n = list(self.numbers)
                key += n[randint(0,len(n)-1)]
        print(colorama.Fore.WHITE+'Generated key: {}'.format(key.upper()))

    def generate_md5(self,text,return_value=False):
        md5 = hashlib.md5()
        md5.update(text.encode('utf-8'))
        text_digest = md5.hexdigest()
        if return_value:
            return text_digest
        else:
            print(colorama.Fore.WHITE+text,'---->',text_digest)


