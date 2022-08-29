# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 11:25:10 2020

@author: Ahmed Sharshar
"""

import numpy as np
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestRegressor



#problem A
"""
        you can chande the degree of regression by changing the variable degree
        """
poly=PolynomialFeatures(degree=1,include_bias=True)
Data=datasets.load_diabetes(return_X_y=False)
x=Data["data"]
y=Data["target"]
diabetes = datasets.load_diabetes()
z=poly.fit_transform(x)
print(z.shape)
print(z)
model = LinearRegression()
model.fit(z, y)
r_sq = model.score(z, y)
y_pred=model.predict(z)
print("mean_squared_error:",mean_squared_error(y_pred,y))
print('coefficient of determination:', r_sq)


#problem b
Data=datasets.load_iris(return_X_y=False)
x=Data["data"]
y=Data["target"]
#KNN

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.20,random_state=0)
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
w = scaler.transform(x)
X_test = scaler.transform(X_test)
classifier = KNeighborsClassifier(n_neighbors=1)
classifier.fit(X_train, y_train)
y_pred = classifier.predict(w)
print("confusion_matrix:",confusion_matrix(y, y_pred))
print("classification_report:",classification_report(y, y_pred))

#random forest
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)
regressor = RandomForestRegressor(n_estimators=22, random_state=0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
y_pred=np.round(y_pred)
y_pred=[int(i) for i in y_pred]
print(y_pred)
print(y_test)
print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))
print(accuracy_score(y_test, y_pred))




