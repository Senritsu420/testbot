import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier #決定木
from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import RandomForestClassifier # ランダムフォレスト
import pickle
import warnings

def model():
  warnings.simplefilter('ignore', UserWarning)

  test = pd.DataFrame({ 'before_user_commits':[0,1,2],
                        'before_user_issues':[0,1,2],
                        'before_user_pull_requests':[0,1,2],
                        'before_user_comment_issue':[0,1,2],
                        'before_user_comment_pull_request':[0,1,2]})

  test = np.array([[10,8,7,7,7]])

  dt = pickle.load(open('LTC_prediction_model.binaryfile','rb'))
  predict = dt.predict_proba(test)
  return predict[:,1]
