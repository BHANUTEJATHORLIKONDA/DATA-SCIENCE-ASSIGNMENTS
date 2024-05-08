# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 12:18:12 2023

@author: sksha
"""

import numpy as np

sample_count = 2000
population_count = 3000000 
sample_mean =  200
sample_std = 30

import scipy.stats as stats 
confidence_level = 0.94   #94%
z_value = stats.norm.ppf(1-(1-confidence_level)/2) 
print("Z-value:",z_value)

confidence_level1 = 0.96 #96% 
z_value1 = stats.norm.ppf(1-(1-confidence_level1)/2)
print("Z-value1:",z_value1)

confidence_level2 = 0.98  #98% 
z_value2 = stats.norm.ppf(1-(1-confidence_level2)/2)
print("Z-value2:",z_value2)

#calculating confidence Levels
#94% ---> 
confidence_level_94 = (sample_mean - z_value * (sample_std /(sample_count** 0.5)),
                       sample_mean + z_value * (sample_std /(sample_count** 0.5))) 
print("Confidence Interval at 45%:",confidence_level_94) 
#96% -->
confidence_level_96 = (sample_mean - z_value1 * (sample_std /(sample_count** 0.5)),
                       sample_mean + z_value1 * (sample_std /(sample_count** 0.5)))
print("Confidence Interval at 96%:", confidence_level_96)
#98% -->
confidence_level_98 = (sample_mean - z_value2 * (sample_std /(sample_count** 0.5)),
                       sample_mean + z_value2 *(sample_std /(sample_count** 0.5)))
print("Confidence Interval at 92%:", confidence_level_98)