import requests
import sys
import json

def get(url, headers):
    result = requests.get(url, headers = headers)
    return result if result.ok else exit(-1)

token = f'token {sys.argv[1]}'
r = get(sys.argv[2], {'Authorization': token}).json

print(r)
