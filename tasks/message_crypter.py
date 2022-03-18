import os
from datetime import datetime
from cryptocode import encrypt,decrypt
class Message_crypter():
    def crypto_exec(self,text,key,crypto_opt):
        if crypto_opt:
            return encrypt(text,key)
        else:
            return decrypt(text,key)
            
    def get_crypto_key(self,host_name):
        crypto_keys_file = open('../logs/crypto_keys.txt','r')
        keys = crypto_keys_file.readlines()
        for key in keys:
            key_parts = key.split("@-@-@-@")
            if key_parts[0] == host_name:
                return key_parts[1]
        return None

    def generate_and_save_crypto_key(self,host_name):
        private_key = os.getenv('PRIVATE_KEY')
        print(private_key)
        crypto_keys_file = open('../logs/crypto_keys.txt','a')
        public_key = "{}{}{}".format(host_name,datetime.now().day,datetime.now().hour)
        encrypted_key = encrypt(public_key, private_key)
        crypto_keys_file.write(host_name+"@-@-@-@"+encrypted_key)
        crypto_keys_file.close()
        return encrypted_key
