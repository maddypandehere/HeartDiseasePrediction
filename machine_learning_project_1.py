# -*- coding: utf-8 -*-
"""Machine Learning Project-1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1jfxeg-Cz3fEfkwUuTDfEdMO6tTd3uQiQ
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""Data collection and Preprocessing"""

heart_data=pd.read_csv('/content/heart_disease_data.csv')
head_data.head()

heart_data.tail()

heart_data.shape

heart_data.info()

heart_data.describe()

#number of rows and columns in the dataset

#statistical measure about the data

#checking the distribution of target variable
heart_data['target'].value_counts()

"""Defective_heart---->1
Healthy heart---->0

Splitting the Features and Target variables
"""

X= heart_data.drop(columns='target',axis=1)
Y= heart_data['target']

print(X)

print(Y)

"""Splitting the data into training data and testing data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

print(X.shape,X_train.shape,X_test.shape)

print(Y_train.shape,Y_test.shape)

"""Logistic Regression"""

model = LogisticRegression()

model = LogisticRegression()
model.fit(X_train, Y_train) # Train the model using the training data

X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

"""model Evaluation"""

X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print("accuracy on training data:,",training_data_accuracy)

model = LogisticRegression()
model.fit(X_train, Y_train) # Train the model using the training data

"""Accuracy score"""

X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print("accuracy on test data:,",test_data_accuracy)

"""Building the predictive system"""

input_data = (41,0,1,130,204,0,0,172,0,1.4,2,0,2)
#change the input data to numpy array

input_data_as_numpy_array= np.asarray(input_data)

input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction=model.predict(input_data_reshaped)
print(prediction)

if(prediction[0]==0):
  print("The person does not have a heart disease")
else:
  print("The person has heart disease")

input_data = (62,0,0,140,268,0,0,160,0,3.6,0,2,2)
input_data_as_numpy_array= np.asarray(input_data)
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
prediction=model.predict(input_data_reshaped)
print(prediction)