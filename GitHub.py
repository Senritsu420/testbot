import requests

r = requests.get(input()).json()

output = r
print(f"RESULT_OUTPUT={output}")
