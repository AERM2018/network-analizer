from ast import arg
import threading
from helpers import http


class Criptography_executor():
    def __init__(self, text):
        self.text = text

    def exec_cipher(self):
        shift = 3  # defining the shift count
        encryption = ""
        for c in self.text:
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
        print('Generated cipher: ',encryption)