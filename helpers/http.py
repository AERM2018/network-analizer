import requests
def do_call(url,method=''):
    if(method.upper()=='GET'):
        requests.get(url)