import requests
import sys
import json
import LTCchecker
import re

def get(url, headers):
    result = requests.get(url, headers = headers)
    return result if result.ok else exit(-1)

token = f'token {sys.argv[2]}'
r = get(sys.argv[1], {'Authorization': token}).json()

issue_user = r['user']['login']

repo_url = r['repository_url']
repos = get(repo_url, {'Authorization': token}).json()

repo_contributor = repos['contributors_url']
repo_cons = get(repo_contributor, {'Authorization': token}).json()

contributors = []
for i in range(len(repo_cons)):
    contributors.append(repo_cons[0]['login'])
    
user_url = r['user']['url']
user = get(user_url, {'Authorization': token}).json()

user_events_url = user['events_url']
events_fixed = user_events_url.replace("{/privacy}","")

user_events = get(events_fixed, {'Authorization': token}).json()
length = len(user_events)

result = LTCchecker.model()[0]
result_num = int(100 * result)

if issue_user in contributors:
    output = f"{issue_user}は初めての貢献者ではありません。"
    print(f"RESULT_OUTPUT={output}")
else:
    output = f"{issue_user}は初めての貢献者です。LTCになる確率は{result_num}%です。"
    print(f"RESULT_OUTPUT={output}")
