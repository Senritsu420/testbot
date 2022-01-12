import requests
import json

url = input()
r = requests.get(url, headers= headers)
r_json = r.json
print(r_json)
