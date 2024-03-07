#Importing the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#reading the data set
dataset=pd.read_csv("advertising.csv")

dataset.head()

#checking for missing values
dataset.isna().sum()

#checking for duplicate rows
dataset.duplicated().any()

#checking for outliers
fig, axs=plt.subplots(3, figsize=(5,5))
plt1=sns.boxplot(dataset['TV'],ax=axs[0])
plt2=sns.boxplot(dataset['Newspaper'],ax=axs[1])
plt3=sns.boxplot(dataset['Radio'],ax=axs[2])
plt.tight_layout()

#Data Pre-Processing
dataset.shape

sns.displot(dataset['Sales'])

sns.pairplot(dataset,x_vars=['TV','Radio','Newspaper'],y_vars='Sales',height=4,aspect=1,kind='scatter')
plt.show()

#HeatMap
sns.heatmap(dataset.corr(),annot=True)
plt.show()

'''Model Building
Prediction using:
 1.Simple Linear Regression
 2.Multiple Linear Regression'''

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

#Setting the value for X & Y
x=dataset[['TV']]
y=dataset[['Sales']]

x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.3,random_state=100)

slr=LinearRegression()
slr.fit(x_train,y_train)

# Printing model coefficients
print('Intercept: ', slr.intercept_)
print('Coefficent: ',slr.coef_)

print('Regression Equation: Sales= 6.948+0.054*TV')

#lINE OF BEST FIT
plt.scatter(x_train,y_train)
plt.plot(x_train,6.948+0.054*x_train, 'r')
plt.show()

#Prediction of Test & Training Set result
y_pred_slr=slr.predict(x_test)
x_pred_slr=slr.predict(x_train)

print("Prediction for test set: {}".format(y_pred_slr))
