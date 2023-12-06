# -*- coding: utf-8 -*-
"""

@author: sksha
"""

import pandas as pd
import scipy.stats as stats
df = pd.read_csv("Costomer+OrderForm.csv")
df.info()
df["Phillippines"].value_counts()
df["Indonesia"].value_counts()
df["Malta"].value_counts()
df["India"].value_counts()

# Data Visualisation
import matplotlib.pyplot as plt

def plot_stacked_bar(df):
    df_plot = df.apply(lambda x: x.value_counts()).T
    df_plot.plot(kind="bar", stacked=True)
    plt.title("Distribution of Error Free and Defective Products by Country")
    plt.xlabel("Country")
    plt.ylabel("Count")
    plt.show()

plot_stacked_bar(df)


# Creating a contingency table
# Create a contingency table

df = df.applymap(lambda x: 0 if x == 'Defective' else 1)
df

# Performing the chi-squared test
from scipy.stats import chi2_contingency
chi2, p, dof, expected = stats.chi2_contingency(df)

print("Chi-squared statistic :",chi2)
print("Degrees of freedom:",dof)
print("P-value:",p)
print("expected:",expected)

#significance level (alpha)
alpha = 0.05

# Comparing p-value with alpha
if p < alpha:
    print("Reject the null hypothesis. There is a significant difference in proportions.")
else:
    print("Fail to reject the null hypothesis. Proportions are not significantly different.")
    

# The chi-squared test we performed indicates that there is not a significant difference in proportions among the countries (Phillippines, Indonesia, Malta, India) in terms of being "Error Free" or "Defective." 
# The p-value (1.0) is greater than the significance level (alpha) of 0.05, so we fail to reject the null hypothesis. 
# This suggests that the observed frequencies in the contingency table are consistent with what would be expected under the assumption of independence between the two categorical variables (country and defect status)