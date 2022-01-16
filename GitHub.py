import requests
import sys
import json

def get(url, headers):
    result = requests.get(url, headers = headers)
    return result if result.ok else exit(-1)

token = f'token {sys.argv[2]}'
r = get(sys.argv[1], {'Authorization': token}).json()

repo_url = r['repository_url']
repos = get(repo_url, {'Authorization': token}).json()

open_issues = repos['open_issues']

output = f"このリポジトリ内でopen中のIssue数は{open_issues}です．"
print(f"RESULT_OUTPUT={output}")
