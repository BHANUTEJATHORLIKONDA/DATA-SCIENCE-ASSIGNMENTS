# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 13:55:32 2023

@author: sksha
"""

import pandas as pd
df = pd.read_csv("Cars.csv")
df
df["MPG"].mean()  #34.4220
df["MPG"].info() 
df["MPG"].describe() 
df["MPG"].hist() 
df["MPG"].kurt() #-0.6116786559430913
df["MPG"].skew() #-0.17794674747025727

#####################################################################
import pandas as pd
df = pd.read_csv("wc-at.csv")
df
df["Waist"].mean()   #91.90
df["Waist"].info()
df["Waist"].describe()
df["Waist"].hist()
df["Waist"].kurt()  #-1.1026
df["Waist"].skew()  #0.134056
