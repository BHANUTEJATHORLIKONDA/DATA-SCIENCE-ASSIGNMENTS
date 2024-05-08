# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 21:15:50 2023

@author: sksha
"""

import pandas as pd
df = pd.read_csv("LabTAT.csv")
df
df.corr()
df["Laboratory 1"].mean()
df["Laboratory 2"].mean()
df["Laboratory 3"].mean()
df["Laboratory 4"].mean()

df["Laboratory 1"].value_counts()
df["Laboratory 2"].value_counts()
df["Laboratory 3"].value_counts()
df["Laboratory 4"].value_counts()

# Visualisation
# Boxplot 
import seaborn as sns
import matplotlib.pyplot as plt

# Create a boxplot
sns.boxplot(data=df)
plt.title('Turnaround Time Distribution by Laboratory')
plt.show()

# Pairwise comparison plot
import seaborn as sns
import matplotlib.pyplot as plt
sns.pairplot(df)
plt.suptitle('Pairwise Comparison of Laboratories', y=1.02)
plt.show()


# Histograms for each laboratory
import matplotlib.pyplot as plt
df.hist(column=df.columns, bins=20, figsize=(12, 8))
plt.suptitle('Histograms of Turnaround Time by Laboratory')
plt.show()

# one-way ANOVA (Analysis of Variance)
from scipy import stats
f_statistic, pval = stats.f_oneway(df["Laboratory 1"], df["Laboratory 2"], df["Laboratory 3"], df["Laboratory 4"])

print("f_statistic value:",f_statistic.round(3))
print("p-value:",pval)

alpha =0.5
if pval<alpha:
    print("H0 is rejected,H1 is accepted")
else:
    print("H1 is rejected,H0 is accepted")  
    
# The calculated F-statistic is 118.704 with an extremely low p-value (2.1156708949992414e-57), which is less than the significance level (alpha) of 0.5. This indicates strong evidence to reject the null hypothesis (H0) that there is no significant difference in average TAT among the laboratories.
# The mean TAT for Laboratory 3 (199.91) is noticeably higher than the means for Laboratories 1, 2, and 4 (178.36, 178.90, 163.68, respectively).
# The correlation matrix shows the relationships between the laboratories. 
# All correlations are relatively low, suggesting that the TAT values are not highly correlated among the laboratories.
    