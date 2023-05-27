#資料分析的工作流程中，在不考慮準確度情況下有哪些必備的環節？
#資料清洗
#資料轉換
#資料標準化
#資料切分
#資料建模
#資料評估

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/aniruddhachoudhury/Red-Wine-Quality/master/winequality-red.csv')
df.head()
#資料清洗
df.isnull().sum()
#資料轉換
df['quality'] = df['quality'].apply(lambda x: 1 if x >= 7 else 0)

#資料切分
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
X = df.drop('quality', axis = 1)
y = df['quality']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
rfc = RandomForestClassifier(n_estimators=200)
rfc_eval = cross_val_score(estimator = rfc, X = X_train, y = y_train, cv = 5)
print(rfc_eval)

