import requests

r = requests.get(input()).json()

output = r.text
print(f"RESULT_OUTPUT={output}")
