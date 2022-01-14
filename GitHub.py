import requests
import sys
import json

def get(url, headers):
    result = requests.get(url, headers = headers)
    return result if result.ok else exit(-1)

token = f'token {sys.argv[2]}'
r = get(sys.argv[1], {'Authorization': token}).json()
output = r
print(f"RESULT_OUTPUT={output}")
