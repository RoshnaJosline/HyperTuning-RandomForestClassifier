# -*- coding: utf-8 -*-
"""M5-Assignment level-2(2)(data preprocessing & decision boundary models).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RBameUxGLBGZYBwo2aXwgnKcWUJYs70-
"""

import numpy as np
import pandas as pd

from google.colab import files
files.upload()

df=pd.read_csv('/content/Social_Network_Ads (1).csv')

df

df.info()

df.isnull().sum()

df['Gender'].unique()

df['Gender'].replace({'Male':0,'Female':1},inplace=True)

df

X=df.drop('Purchased',axis=1)
y=df.Purchased

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.30,random_state=0)

from sklearn.preprocessing import StandardScaler

sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)

from sklearn.neighbors import KNeighborsClassifier  
classifier= KNeighborsClassifier(n_neighbors=5, metric='minkowski', p=2 )  
classifier.fit(X_train, y_train)

y_pred=classifier.predict(X_test)

from sklearn.metrics import accuracy_score

print('Accuracy_Score: ',accuracy_score(y_test,y_pred))

from sklearn.svm import SVC
classifier=SVC(kernel='linear',random_state=0)
classifier.fit(X_train,y_train)

y_pred=classifier.predict(X_test)

from sklearn.metrics import accuracy_score

print('Accuracy_Score: ',accuracy_score(y_test,y_pred))