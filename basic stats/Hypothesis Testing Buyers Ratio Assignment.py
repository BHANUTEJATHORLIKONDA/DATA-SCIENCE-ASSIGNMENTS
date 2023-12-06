# -*- coding: utf-8 -*-
"""
@author: sksha
"""

# Importing necessary libraries
import pandas as pd
from scipy.stats import chi2_contingency

# Importing the data
df = pd.read_csv("BuyerRatio.csv")

# Display basic information about the dataset
print(df.shape)
print(df.info())
print(list(df))

# Data Visualisation
import matplotlib.pyplot as plt
df.set_index('Observed Values').T.plot(kind='bar', stacked=True)
plt.title('Distribution of Observed Values Across Regions')
plt.xlabel('Regions')
plt.ylabel('Count')
plt.legend(title='Observed Values')
plt.show()

# Creating a contingency table
contingency_table = pd.crosstab(df['Observed Values'], [df['East'], df['West'], df['North'], df['South']])

# Map string labels to numeric values (0 and 1)
df['Observed Values'] = df['Observed Values'].apply(lambda x: 0 if x == 'Males' else 1)

# Performing the chi-squared test
chi2, p, dof, expected = chi2_contingency(contingency_table)

print("Chi-squared statistic:", chi2)
print("Degrees of freedom:", dof)
print("P-value:", p)
print("Expected frequencies:\n", expected)

# Significance level (alpha)
alpha = 0.05

# Comparing p-value with alpha
if p < alpha:
    print("Reject the null hypothesis. There is a significant difference in proportions.")
else:
    print("Fail to reject the null hypothesis. Proportions are not significantly different.")
    
    
# Based on the chi-squared test results, with a p-value of 1.0, we fail to reject the null hypothesis. 
# This means that there is no significant difference in proportions between the observed values (Males and Females) and the regions (East, West, North, South). 
# The chi-squared statistic of 0.0 indicates perfect agreement between the observed and expected values.
