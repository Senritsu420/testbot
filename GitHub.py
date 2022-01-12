import requests
import sys
import json

def get(url, headers):
    result = requests.get(url, headers = headers)
    return result if result.ok else exit(-1)

r = requests.get(url, headers= headers)
r_json = r.json
print(r_json)
