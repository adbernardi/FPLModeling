# re-running the FPL API to get updated teams

import requests
import pandas as pd

url = 'https://fantasy.premierleague.com/api/bootstrap-static/'

r = requests.get(url)

json = r.json()

# want to just focus on the teams for the script

teams_df = pd.DataFrame(json['teams'])

# this might be it, let's see if it works

teams_df.to_csv('~/Documents/Codebase/fpl_teams_2324.csv')




