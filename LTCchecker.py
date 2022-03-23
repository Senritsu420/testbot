import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier #決定木
from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import RandomForestClassifier # ランダムフォレスト
import pickle
import warnings
import requests
import sys
import json
import re

def get(url, headers):
  result = requests.get(url, headers = headers)
  return result if result.ok else exit(-1)

def model():
  warnings.simplefilter('ignore', UserWarning)

  test = pd.DataFrame({ 'before_user_commits':[0,1,2],
                        'before_user_issues':[0,1,2],
                        'before_user_pull_requests':[0,1,2],
                        'before_user_comment_issue':[0,1,2],
                        'before_user_comment_pull_request':[0,1,2]})

  token = f'token {sys.argv[2]}'
  r = get(sys.argv[1], {'Authorization': token}).json()
  
  issue_user = r['user']['url']
  user = get(issue_user, {'Authorization': token}).json()
  
  events = user['events_url']
  events_fixed = events.replace("{/privacy}","")
  user_events = get(events_fixed, {'Authorization': token}).json()
  
  commits = 0
  create_is = 0
  pr = 0
  for event in user_events:
    if event['type'] == 'PushEvent':
      commits = commits + 1
    elif event['type'] == 'CreateEvent':
      create_is = create_is + 1
    elif event['type'] == 'PullRequestEvent':
      pr = pr + 1

  test = np.array([[commits,create_is,pr,7,7]])

  dt = pickle.load(open('LTC_prediction_model.binaryfile 2','rb'))
  predict = dt.predict_proba(test)
  return predict[:,1]
