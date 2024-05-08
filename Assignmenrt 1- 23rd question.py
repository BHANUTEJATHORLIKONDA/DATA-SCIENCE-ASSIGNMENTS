# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 15:15:26 2023

@author: sksha
"""

import scipy.stats as stats

# Sample size
n = 25

# Confidence levels (as percentages)
confidence_level_95 = 95
confidence_level_96 = 96
confidence_level_99 = 99

# Degrees of freedom (for a sample size of 25, df = n - 1)
degrees_of_freedom = n - 1

# Calculate t-scores for the specified confidence levels
t_score_95 = stats.t.ppf(1 - (1 - confidence_level_95/100) / 2, df=degrees_of_freedom)
t_score_96 = stats.t.ppf(1 - (1 - confidence_level_96/100) / 2, df=degrees_of_freedom)
t_score_99 = stats.t.ppf(1 - (1 - confidence_level_99/100) / 2, df=degrees_of_freedom)

# Print the t-scores
print("t-score for confidence_level_95 confidence interval with :",t_score_95) #2.0638
print("t-score for confidence_level_96 confidence interval with :",t_score_96) #2.1715
print("t-score for confidence_level_99 confidence interval with :",t_score_99) #2.796
