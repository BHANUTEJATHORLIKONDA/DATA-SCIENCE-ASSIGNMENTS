# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 17:46:43 2023

@author: sksha
"""
# Data
import numpy as np
import pandas as pd
import seaborn as sns
df = np.array([[24.23],[25.53],[25.41],[24.14],[29.62],[28.25],[25.81],[24.39],[40.26],[32.95],[91.36],[25.99],[39.42],[26.71],[35.00]])
df = pd.DataFrame(df)
df
df.describe()
df.hist()
sns.distplot(df)
df.skew()
df.kurt()
df
# Plot the data
import matplotlib.pyplot as plt
plt.figure(figsize=(5, 5))
plt.boxplot(df)
plt.title("Boxplot of Measure X")
plt.ylabel("Value")
plt.show()

# Calculating mean
mean = np.mean(df)

# Calculating standard deviation 
std_dev = np.std(df)

# Calculating variance 
variance = np.var(df)

print("Mean :", mean)                      #33.271333 (MEAN)
print("Standard Deviation :", std_dev)     #16.370813 (Standard deviation)
print("Variance :", variance)              #268.003505  (Variance)







































