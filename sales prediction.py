
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
data =pd.read_csv(r"C:\Users\kr981\Downloads\archive (5)\sales data file.csv")
data.head()
data.shape
data.info()
data.describe
fig, axs = plt.subplots(3, figsize = (5,5))
plt1 = sns.boxplot(data['TV'], ax = axs[0])
plt2 = sns.boxplot(data['Newspaper'], ax = axs[1])
plt3 = sns.boxplot(data['Radio'], ax = axs[2])
plt.tight_layout()
sns.boxplot(data['Sales'])
plt.show()
sns.pairplot(data, x_vars=['TV', 'Newspaper', 'Radio'], y_vars='Sales', height=4, aspect=1, kind='scatter')
plt.show()
sns.heatmap(data.corr(), cmap="YlGnBu", annot = True)
plt.show()
X = data['TV']
y =data['Sales']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.7, test_size = 0.3, random_state = 100)
X_train.head()
y_train.head()
