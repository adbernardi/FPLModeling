'''
I. Preamble

After querying the API, we'll now make a python script where we attempt to organize, clean up, and start to prepare the data for FPL-related inferences. 

We'll start reading in the data from the first 3 game weeks, and then we'll start to clean up the data to hopefully see what's going on so far this season. 

'''

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 

# Reading in the data from the first 3 game weeks, called via API 
# maybe want to put in a variable for the file path name for this problem of sharing multiple machines 
# work computer file path 
filepath = r"C:\Users\adbe251\Documents\Codebase\fpl_data_big.csv" 
#filepath_2 = "/home/adbucks/Documents/Codebase/fpl_data_big.csv"
# making sure this works 
print(filepath)

df = pd.read_csv(filepath)

# Let's take a look at the data 
# we now see what we have to clean up 
# want to take out the left most index column to try and re-index
df.drop(df.columns[0], axis = 1 , inplace=True)
print(df.head(10))
print(df.tail(10))

# want to get a sense of column names 
print(df.columns)

'''
II.Basic EDA 

Now that we have the data collected from the API, we can start to parse through the data frame and start to poke around to get some transfer ideas. 
'''

# we can start by getting the columns we will only care about for FPL analysis
# see if we can do this to save time 
col_list = df.columns 
# think we can just proceed with the data frame as is, and just get to describing and understanding the data 
print(df.describe())

# want to pare down somewhat, we might want to start just looking at points scored, expected stats, and maybe a percentage selected by 
# so we can start with that 
df_x = df.loc[:,:'expected_goal_involvements']

print(df_x.head(10))
print(df_x.tail(10))

# this is going to be our dataframe of interest for this initial anlaysis
# we will probably want to start with at least some kind of minutes cutoff, we can go by percentile for this 
print(df_x['minutes'].describe())
# let's say at least 20 minutes
df_x = df_x.loc[df_x['minutes'] >= 20] 

print(df_x.head(10))
print(df_x['minutes'].describe())

# can now keep doing our analysis with our minute cutoff. Also it's important to note who is actually on our team and who we need to think about buying 

