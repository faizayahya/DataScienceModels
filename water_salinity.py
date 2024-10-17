# -*- coding: utf-8 -*-
"""water-salinity.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/170ZUMi2nvJcTHyNU2yL_TY7ytLSWFTqq

linear regression

Create a model, and plot the data as well as the prediction.

Does salinity affect temp?
"""

#1) import libraries that are useful
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""2. Importing dataset from kaggle, file is too big so have uploaded onto colab"""

ocean_dataset = pd.read_csv('bottle.csv')

#3) Exploratory data analysis (EDA). Getting familiar with the data
#see the first five lines
ocean_dataset.head(5)

ocean_dataset.info()

"""Only interested in salinity and temperature, so will need to edit our dataset.

Pandas - how do we keep certain columns:
df[['col', 'col2']
"""

#only keeping required columns
training_data = ocean_dataset[['T_degC', 'Salnty']]

training_data.head()

#representing the dimensionality of the DataFrame.
training_data.shape

#checking how many nan values
training_data.isna().sum()

training_data.count()

training_data.head()

#4) when i drop na I need to store it somewhere new
training_data_nan = training_data.dropna()

#confirming we have no missing values
training_data_nan.isna().sum()

training_data_nan

#Plot the data
# Continous data = scattar graph
#However cause the data is so much, we will need to sample the data
#Doing the last 750 points to see the pattern properly
training_data_750 = training_data_nan[:][:750]
plt.scatter(training_data_750['Salnty'], training_data_750['T_degC'])
plt.title(' Temperature vs Salnty ')
plt.xlabel('Salnty')
plt.ylabel('Temperature')
plt.show()

training_data__nan_random_750 = training_data_nan.sample(n=750, random_state=50)

plt.scatter(training_data__nan_random_750['Salnty'], training_data__nan_random_750['T_degC'])
plt.title(' Temperature vs Salnty ')
plt.xlabel('Salnty')
plt.ylabel('Temperature')
plt.show()

"""With this dataset, the accurancy of linear regression model will decrease in comparison to a sample dataset. So we'll rerun with a sample set to train our model. The full dataset might contain more outliers or noisy data and can skew the model."""

#separate features from the targets, supervised learning
#separate features from the targets, supervised learning
X = training_data__nan_random_750['Salnty'].values.reshape(-1,1)

y = training_data__nan_random_750['T_degC'].values.reshape(-1,1)

len(X)

len(y)

# 80/20 train/test split
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

len(X_train)

len(X_test)

"""6) Implement Algorithm"""

# 6: Training our Model
#Adding linear models to library, linear regression is used for fitting a linear model to data.
from sklearn.linear_model import LinearRegression
#sklearn.metrics provides functions to evaluate the performance of the model.
from sklearn.metrics import mean_absolute_error,r2_score


#.fit(X_train, y_train): This method fits the model to the training data. X_train is the input features (independent variables), and y_train is the target variable (dependent variable) we are trying to predict.
model = LinearRegression().fit(X_train, y_train)
y_prediction = model.predict(X_test)

len(y_prediction)

#the average absolute difference between the actual values (y_test) and the predicted values (y_prediction)
print("mean absolute error:",mean_absolute_error(y_test,y_prediction))
print("r2 score:",r2_score(y_test,y_prediction))
print("score:",model.score(X_train,y_train))

import matplotlib.pyplot as plt
plt.scatter(X_test,y_test,color='r')
plt.plot(X_test,y_prediction,color='g')
plt.show()

#try testing
salinity=33.5
print("when salinity=",salinity,", temp is",model.predict(np.array([[salinity]])))