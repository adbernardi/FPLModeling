'''
After querying the API, we'll now make a python script where we attempt to organize, clean up, and start to prepare the data for FPL-related inferences. 

We'll start reading in the data from the first 3 game weeks, and then we'll start to clean up the data to hopefully see what's going on so far this season. 
'''

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

# Reading in the data from the first 3 game weeks, called via API 
df = pd.read_csv("/home/adbucks/Documents/Codebase/fpl_data_big.csv")

# Let's take a look at the data 
print(df.head()) 
 
# we now see what we have to clean up 

