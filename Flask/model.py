import numpy as np
import pandas as pd
from sklearn.feature_selection import f_classif, SelectKBest
from xgboost import XGBClassifier
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import pickle

data = pd.read_csv("employee_promotion.csv")

for i in ['age', 'length_of_service']:
    Q1 = data[i].quantile(0.25)
    Q3 = data[i].quantile(0.75)
    IQR=Q3-Q1
    upper_limit=Q3+1.5*IQR
    lower_limit=Q1-1.5*IQR
    data[i].where(data[i] > lower_limit, lower_limit, inplace = True)
    data[i].where(data[i] < upper_limit, upper_limit, inplace = True)

data['education'].fillna(data['education'].mode()[0], inplace = True)

for i in data['department'].unique():
    data['avg_training_score'].loc[(data['department'] == i) & (data['avg_training_score'].isna())] = data.loc[data['department'] == i]['avg_training_score'].median()

for i in data.loc[data['previous_year_rating'].isnull()].index:
    if data.at[i, 'recruitment_channel'] == 'referred' or data.at[i, 'avg_training_score'] >= 90:
        data.at[i, 'previous_year_rating'] = 4.0
    else:
        data.at[i, 'previous_year_rating'] = 3.0

X = data.drop(['is_promoted', 'employee_id'], axis=1)
y = data['is_promoted']

transformer = make_column_transformer(
    (OneHotEncoder(sparse_output=False), ['region', 'gender', 'department', 'education', 'recruitment_channel']),
    (StandardScaler(), ['age', 'previous_year_rating', 'length_of_service', 'avg_training_score', 'no_of_trainings']),
    remainder='passthrough')
X = transformer.fit_transform(X)
X = pd.DataFrame(X, columns=transformer.get_feature_names_out())
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

fs = SelectKBest(f_classif, k=35)
X_fs = fs.fit_transform(X_train, y_train)

params = {'tree_method': 'approx',
 'subsample': 0.5,
 'scale_pos_weight': 1,
 'reg_lambda': 1,
 'min_child_weight': 1,
 'max_depth': 7,
 'max_delta_step': 2,
 'eta': 0.1,
 'alpha': 0}
xgb = XGBClassifier(**params)
xgb.fit(X_fs, y_train)

pickle.dump(transformer, open('transformer.pkl', 'wb'))
pickle.dump(fs, open('feature_select.pkl', 'wb'))
pickle.dump(xgb, open('model.pkl', 'wb'))