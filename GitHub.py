import request

URL = 'https://api.github.com/repos/YUTOKUBO2001/testbot/pulls?&state=closed'
headers = {'Authorization': 'token xxxxx'} # 取得したアクセストークン
r = requests.get(URL.format(repo), headers=headers)
