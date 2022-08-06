# Importing libraries
import numpy as np
from sklearn import datasets
import pandas as pd
from sklearn.model_selection import train_test_split

# Fetching the dataset
breast_cancer = datasets.load_breast_cancer()
# print(breast_cancer)  # printing the dataset to check whether is has been loaded or not.

X = breast_cancer.data
Y = breast_cancer.target

# Printing the Data and Target of the Dataset
# print(X)
# print(Y)

# printing the shape of X and Y or the instances of X and Y
# print(X.shape, Y.shape)

"""Import data to the Pandas Data Frame"""
data = pd.DataFrame(breast_cancer.data, columns = breast_cancer.feature_names)

data['class'] =  breast_cancer.target

# print(data.head())    # print some data samples

# print(data.describe())    # prints statistical data

# print(data['class'].value_counts())   # prints the number of cases for malignant and benign

# print(breast_cancer.target_names)     # Displays the target names, i.e., Malignant and Benign

# data.groupby('class').mean()  # printing the mean feature values for each of the targets
#0 = malignant
#1 = benign

"""Train and Test Data Split"""

X_train, X_test, Y_train, Y_test = train_test_split(X,Y)

print(Y.shape, Y_train.shape, Y_test.shape)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1)
#test_size --> to specify the percentage of test data needed

print(Y.shape, Y_train.shape, Y_test.shape)

print(Y.mean(), Y_train.mean(), Y_test.mean())

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, stratify=Y)
#stratify --> for correct distribution of data as of the original data

print(Y.mean(), Y_train.mean(), Y_test.mean())

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=1)
#random_state --> specific split of data, each value of random_state splits the data differently

print(X_train.mean(), X_test.mean(), X.mean())

print(X_train)

"""**Logistic Regression**"""

#import logistic regression from sklearn
from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression()   #loading the logistic regression model to the variable "classifier"

#training the model on training data
classifier.fit(X_train, Y_train)

"""**Evaluation of the Model**"""

#import accuracy_score
from sklearn.metrics import accuracy_score

prediction_on_training_data = classifier.predict(X_train)
accuracy_on_training_data = accuracy_score(Y_train, prediction_on_training_data)

print('Accuracy on training data :', accuracy_on_training_data)

#prediction on test_data
prediction_on_test_data = classifier.predict(X_test)
accuracy_on_test_data = accuracy_score(Y_test, prediction_on_test_data)

print('Accuracy on test data :', accuracy_on_test_data)

"""Detecting whether the Patient has Breast Cancer in Benign or Malignant Stage"""

input_data = (17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189)
#change the input_data to numpy_array to make prediction
input_data_as_numpy_array = np.array(input_data)
print(input_data)

#reshape the array we are predicting the output for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

#prediction
prediction = classifier.predict(input_data_reshaped)
print(prediction)   #returns a list with elements 0 [if Malignant] and 1 [if Benign]

if (prediction[0]==0):
    print("The Breast Cancer is at Malignant Stage.")
else:
    print("The Breast Cancer is at Benign Stage.")