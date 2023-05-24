import pandas as pd

def get_matches_team_season(df, team):
    matches = []
    for index, row in df.iterrows():
        if ((row['home_team'] == team) or (row['away_team'] == team)): 
            matches.append(row)
    return matches

def get_season_matches_ids(df):
    ids = []
    for index, row in df.iterrows():
        if row['match_status'] == 'available':
            ids.append(row['match_id'])
    return ids
