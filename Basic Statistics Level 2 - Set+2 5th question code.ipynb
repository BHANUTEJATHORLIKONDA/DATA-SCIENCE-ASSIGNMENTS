# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:30:59 2023

@author: sksha
"""

import scipy.stats as stats

# Constants
USD_to_Rupees = 45
mean_profit_1_USD = 5
variance_profit_1_USD = 32
mean_profit_2_USD = 7
variance_profit_2_USD = 42

# Calculate the mean and variance in Rupees
mean_profit_1_Rupees = mean_profit_1_USD * USD_to_Rupees
variance_profit_1_Rupees = variance_profit_1_USD * (USD_to_Rupees**2)
mean_profit_2_Rupees = mean_profit_2_USD * USD_to_Rupees
variance_profit_2_Rupees = variance_profit_2_USD * (USD_to_Rupees**2)

# A. Calculate the Rupee range containing 95% probability
total_mean_Rupees = mean_profit_1_Rupees + mean_profit_2_Rupees
total_variance_Rupees = variance_profit_1_Rupees + variance_profit_2_Rupees

# Calculate the standard deviation
std_dev_Rupees = (total_variance_Rupees) ** 0.5

# Calculate the Z-score for a 95% confidence interval
confidence_interval_Z = stats.norm.ppf(0.975)

# Calculate the lower and upper limits in Rupees
lower_limit = total_mean_Rupees - confidence_interval_Z * std_dev_Rupees
upper_limit = total_mean_Rupees + confidence_interval_Z * std_dev_Rupees

print("A. Rupee range with 95% probability:", (lower_limit, upper_limit))

# B. Calculate the 5th percentile of profit in Rupees
percentile_5_Z = stats.norm.ppf(0.05)
percentile_5_Rupees = total_mean_Rupees + percentile_5_Z * std_dev_Rupees

print("B. 5th percentile of profit in Rupees:", percentile_5_Rupees)

# C. Calculate the probability of making a loss for each division
# Define the standard normal distribution for calculations
normal_dist = stats.norm(0, 1)

# Calculate the Z-scores for each division's loss
z_score_profit_1 = (0 - mean_profit_1_USD) / (variance_profit_1_USD ** 0.5)
z_score_profit_2 = (0 - mean_profit_2_USD) / (variance_profit_2_USD ** 0.5)

# Calculate the probabilities of making a loss for each division
probability_loss_profit_1 = normal_dist.cdf(z_score_profit_1)
probability_loss_profit_2 = normal_dist.cdf(z_score_profit_2)

print("C. Probability of making a loss for Profit1:", probability_loss_profit_1)
print("   Probability of making a loss for Profit2:", probability_loss_profit_2)
