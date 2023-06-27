# FPL API Code for Python (and later R)

import requests 
import pandas as pd 
import numpy as np 

url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

r = requests.get(url)

json = r.json()

# look at the keys 

json.keys() # elements, element_type , teams 

# building a dataframe and reorienting/mapping based on the API request 

elements_df = pd.DataFrame(json['elements'])
elements_types_df = pd.DataFrame(json['element_types'])
teams_df = pd.DataFrame(json['teams'])

# previewing 
elements_df.head()

elements_df.columns 

# a way of slicing this data frame, although obviously not the only way 

slim_elements_df = elements_df[[
	'second_name' 
	, 'team' 
	, 'element_type' 
	,'selected_by_percent' 
	, 'now_cost'
	, 'minutes'
	, 'transfers_in'
	, 'value_season'
	, 'total_points']]

slim_elements_df.head() # verifying this works and is palatable

# using map, we'll see if this is useful or not 

slim_elements_df['position'] =
	slim_elements_df.element_type.map(elements_types_df.set_index('id').singular_name)

# checking this 
slim_elements_df.head() # should add position as an effective column

# doing the same for team/club

slim_elements_df['team'] =
	slim_elements_df.team.map(teams_df.set_index('id').name)

# inconsistent data types in the API pull - fixing this 
slim_elements_df['value'] = slim_elements_df.value_season.astype(float)

# sorting by highest value, defined as points / cost 

# looking at our most valuable players 
slim_elements_df.sort_values('value', ascending = False).head(10)

# grouping value by position, there's definitely a better way to do this, but 
# marking for posterity 

pivot =
	slim_elements_df.pivot_table(index = 'position'
		, values = 'value'
		, aggfunc = np.mean).reset_index()

pivot.sort_values('value' , ascending = False)

# gives us a value calculation grouped by position 

# looking at distributions of value might give us an idea of how 
# "replaceable" players are 

# trying to filter out those that don't play, as that skews the value 
# calculation 

slim_elements_df = slim_elements_df.loc[slim_elements_df.value > 0]

# can run the same calculation as above with the zeros taken out 

pivot =
	slim_elements_df.pivot_table(index = 'position'
		, values = 'value'
		, aggfunc = np.mean).reset_index()

pivot.sort_values('value' , ascending = False)

# can do the same grouping but by team, rather than position 

team_pivot = slim_elements_df.pivot_table(index = 'team'
	, values = 'value'
	, aggfunc = np.mean).reset_index()

team_pivot.sort_values('value' , ascending = False)

# histogram for value by position 
# at this point, just export csv and start doing density plots and pdf's in R

# breaking the df by position and then analyzing the pdf/spread 

fwd_df = slim_elements_df.loc[slim_elements_df.position == 'Forward']
mid_df = slim_elements_df.loc[slim_elements_df.position == 'Midfielder']
def_df = slim_elements_df.loc[slim_elements_df.position == 'Defender']
goal_df = slim_elements_df.loc[slim_elements_df.position == 'Goalkeeper']

# looking at the shapes of the value calculation by position 

fwd_df.value.hist()
# done for each position DF

# you could do this for xP and cost to provide a prescriptive value
# xP / cost = xValue
# would want to do this based on xP over certain GW intervals 
# i.e. GW 1-6 xValue, by position 

# this value model would be used in conjunction with an xP and 
# optimizer model for team selection decisions 

# broader ensemble framework

# Value and xValue will factor into the model and the broader ensemble 
# framework, but remember...the game is about points :) 

# exporting the finished product to csv for further work

slim_elements_df.to_csv('~/Desktop/Codebase/fpl_data.csv')

# done!

