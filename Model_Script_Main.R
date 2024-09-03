##################
# FPL Modeling Script
##################

# testing if I have dplyr on this machine already 
library(dplyr)

### 1 -- Reading in the Data 

# We'll start by reading in the data with the big statistics, the data 
# with the team ID's, and then matching

df_big_main <- read.csv('/home/adbucks/Documents/Codebase/fpl_data_big.csv')

head(df_big_main)

# Reading in the team script for a later matching 

df_teams <- read.csv('/home/adbucks/Documents/Codebase/fpl_teams_2324.csv')
head(df_teams)

# left join, left column is 'team', right column is 'id'
# can select the actual team name from the right able and add onto our big table 
# going to try the version with dplyr

merge_df_test <- left_join(df_big_main, df_teams, by = c("team" = "id"))
print(merge_df_test)

colnames(merge_df_test)

write.csv(merge_df_test , '/home/adbucks/Documents/Codebase/merge_df_fpl_test.csv')

# merge works, now just need to select our target columns and have a more tailored/smaller dataframe in a given order 

# THEN we can do actual modeling 


