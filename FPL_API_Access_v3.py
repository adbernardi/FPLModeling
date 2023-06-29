import requests
import pandas as pd
import json

# request to get the data from the original API
url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
r  = requests.get(url)

# converting the JSON data to a python object
json = r.json()
json.keys()

# manipulating and working with this somewhat

elements_df_2 = pd.DataFrame(json['elements'])

real_elements_df = elements_df_2[['team', 'id', 'first_name', 'second_name', 'web_name', 'element_type'
                                  , 'cost_change_start', 'now_cost', 'selected_by_percent', 'transfers_in'
                                  , 'transfers_out', 'total_points', 'bonus', 'minutes', 'goals_scored'
                                  , 'assists', 'clean_sheets', 'status', 'form' , 'ep_next', 'ep_this'
                                  , 'event_points', 'points_per_game', 'value_form', 'value_season'
                                  , 'penalties_saved', 'penalties_missed', 'yellow_cards', 'red_cards'
                                  , 'bps', 'influence', 'creativity', 'threat', 'ict_index', 'influence_rank'
                                  , 'influence_rank_type', 'creativity_rank', 'creativity_rank_type'
                                  , 'threat_rank', 'threat_rank_type', 'ict_index_rank'
                                  , 'ict_index_rank_type']]

# Just going to export the API output and then move on to peripheral statistics

real_elements_df.to_csv('~/Documents/Codebase/fpl_data_big.csv')




