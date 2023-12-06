# -*- coding: utf-8 -*-
"""

@author: sksha
"""
import numpy as np
import pandas as pd 
df  =pd.read_csv("Cutlets.csv")
df.head()

# Sample data for cutlet diameter from two units
df["Unit A"].mean()
df["Unit B"].mean()
df["Unit A"].value_counts()
df["Unit B"].value_counts()

# Visualisation
import seaborn as sns
import matplotlib.pyplot as plt

# Create a boxplot
sns.boxplot(x="variable", y="value", data=pd.melt(df))
plt.title("Comparison of Cutlet Diameter Between Unit A and Unit B")
plt.xlabel("Unit")
plt.ylabel("Cutlet Diameter")
plt.show()

# Perform a two-sample t-test
from scipy import stats
tcal,pval=stats.ttest_ind(df["Unit A"],df["Unit B"])
print("t-calculated value:",tcal.round(3))           # Display the test statistics and p-value
print("p-value:",pval.round(3))

# Define the significance level
alpha =0.5
if pval<alpha:     # Check if the p-value is less than the significance level
    print("H0 is rejected,H1 is accepted")
else:
    print("H1 is rejected,H0 is accepted")
    
# Test Result: The p-value of 0.472 is greater than the significance level of 0.05.
# Decision: As a result, you fail to reject the null hypothesis (H0).
# Conclusion: There is not enough evidence to conclude that there is a significant difference in the mean cutlet diameter between Unit A and Unit B.
