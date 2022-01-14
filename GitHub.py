import requests
import sys
import json

def get(url, headers):
    result = requests.get(url, headers = headers)
    return result if result.ok else exit(-1)

token = f'token {sys.argv[2]}'
r = get(sys.argv[3], {'Authorization': token}).json()
num_issue = r['comments']
print(num_issue)

output = 'BOOK OFFなのに本ねえじゃん！'
print(f"RESULT_OUTPUT={output}")
