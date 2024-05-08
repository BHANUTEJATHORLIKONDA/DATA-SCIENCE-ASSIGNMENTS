# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 22:02:31 2023

@author: sksha
"""

#20TH QUESTION
import scipy.stats as stats

# Given data
sample_mean = 260  # Sample mean
population_mean = 270  # CEO's claimed population mean
sample_std = 90  # Sample standard deviation
sample_size = 18  # Sample size

# Calculate the t-score
t_score = (sample_mean - population_mean) / (sample_std / (sample_size ** 0.5))

# Calculate the degrees of freedom
df = sample_size - 1

# Calculate the probability using the t-distribution
probability = stats.t.cdf(t_score, df)

print("Probability that the average life is no more than 260 days:", probability)


#21ST QUESTION
# Load the dataset from "Cars.csv" into a pandas DataFrame
import pandas as pd
from scipy import stats

df = pd.read_csv("Cars.csv")
df["MPG"].hist()
df["MPG"].skew()
df["MPG"].kurt()

import seaborn as sns
sns.distplot(df["MPG"])

# Extract the "MPG" column as a pandas Series
mpg = df['MPG']

# Perform the Shapiro-Wilk test for normality
statistic, p_value = stats.shapiro(mpg)

# Set the significance level (alpha)
alpha = 0.05

# Check if the p-value is less than alpha
if p_value > alpha:
    print("MPG follows a normal distribution (Failed to reject the null hypothesis)")
else:
    print("MPG does not follow a normal distribution (Null hypothesis rejected)")
    

import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Load the dataset
data = pd.read_csv('wc-at.csv')

# Extract the 'AT' and 'Waist' columns
at_data = data['AT']
waist_data = data['Waist']

# Create histograms
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.hist(at_data, bins=15, edgecolor='k')
plt.title('Histogram of Adipose Tissue (AT)')
plt.xlabel('AT')
plt.ylabel('Frequency')

plt.subplot(1, 2, 2)
plt.hist(waist_data, bins=15, edgecolor='k')
plt.title('Histogram of Waist Circumference (Waist)')
plt.xlabel('Waist')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

# Create Q-Q plots
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
stats.probplot(at_data, dist="norm", plot=plt)
plt.title('Q-Q Plot for Adipose Tissue (AT)')

plt.subplot(1, 2, 2)
stats.probplot(waist_data, dist="norm", plot=plt)
plt.title('Q-Q Plot for Waist Circumference (Waist)')

plt.tight_layout()
plt.show()

# Perform Shapiro-Wilk normality test
shapiro_at = stats.shapiro(at_data)
shapiro_waist = stats.shapiro(waist_data)

print("Shapiro-Wilk test results for Adipose Tissue (AT):")
print("Test Statistic:", shapiro_at[0])
print("p-value:", shapiro_at[1])

print("\nShapiro-Wilk test results for Waist Circumference (Waist):")
print("Test Statistic:", shapiro_waist[0])
print("p-value:", shapiro_waist[1])

