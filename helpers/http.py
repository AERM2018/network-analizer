from traceback import print_tb
import requests
def do_call(url,method=''):
    if(method.upper()=='GET'):
        requests.get(url)
        print("The attack has been successful")