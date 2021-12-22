import requests

URL = 'https://api.github.com/repos/YUTOKUBO2001/testbot/contributors'
r = requests.get(URL)
output = r.json()
print(f"RESULT_OUTPUT={output}")
