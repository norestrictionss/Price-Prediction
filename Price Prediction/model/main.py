import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso

dataset = pd.read_csv('Housing.csv')
dataset = dataset.sample(frac=1)
dataset = dataset[['price', 'area', 'bedrooms', 'bathrooms']]
k_folds = KFold(n_splits=3)
x = dataset[['area', 'bedrooms', 'bathrooms']]
y = dataset['price']
scaler = MinMaxScaler()
x_train, x_test, y_train, y_test = train_test_split(x, y)

def linear_regression(x_train, y_train, x_test):

    # Model Building Part with Linear Regression
    lr = LinearRegression()
    lr.fit(x_train, y_train)

    result = lr.predict(x_test)
    result = pd.DataFrame(data=result)
    return result

def lasso():

    # L1 Regularization
    lasso = Lasso()
    lasso.fit(x_train, y_train)
    print(pd.DataFrame(data=lasso.predict(x_test)))
    scores = cross_val_score(LinearRegression(), x, y, cv=k_folds)
    print(scores)

    # Next will come later on.
