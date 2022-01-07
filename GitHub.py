import requests
url = input()
r = requests.get(url, headers= headers)

output = r
print(r)
