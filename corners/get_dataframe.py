import pandas as pd
from corners.metric import *

def get_df_row(corner):
    """Get the row to dataframe of the corner."""
    corner_df = pd.DataFrame()
    corner_df['team'] = [get_corner_team(corner)]
    # corner_df['opponent'] = [get_corner_opponent(corner)]
    corner_df['num_of_events'] = [get_corner_num_of_events(corner)]
    corner_df['duration'] = [get_corner_duration(corner)]
    corner_df['num_of_passes'] = [get_corner_num_of_passes(corner)]
    corner_df['num_of_shots'] = [get_corner_num_of_shots(corner)]
    # corner_df['score'] = [evaluate_corner(corner, params)]
    # corner_df['obv'] = [get_corner_obv(corner)]
    corner_df['xg'] = [get_corner_xg(corner)]
    return corner_df

def get_corner_obv(corner):
    obv = 0
    # sum obv_total_net for all events in corner
    for i in range(len(corner)):
        if corner.iloc[i]['obv_for_net']:
            obv += float(corner.iloc[i]['obv_for_net'])
    return obv

def get_corner_xg(corner):
    xg = 0
    for i in range(len(corner)):
        if corner.iloc[i]['type'] == 'Shot':
            if corner.iloc[i]['event'].get('statsbomb_xg') != None:
                print(corner.iloc[i]['event'].get('statsbomb_xg'))
                xg += float(corner.iloc[i]['event'].get('statsbomb_xg'))
    return xg

def get_conrner_score(corner):
    #TODO: write this function and consider how to get the final score
    return corner['score'].iloc[0]

def get_corner_num_of_events(corner):
    return len(corner)

def get_corner_team(corner):
    return corner.iloc[0]['team']

def get_corner_opponent(corner):    
    #TODO: write this function
    pass

def get_corner_duration(corner):
    return (corner.iloc[-1]['minute'] * 60 + corner.iloc[-1]['second']) - (corner.iloc[0]['minute'] * 60 - corner.iloc[0]['second'])

def get_corner_num_of_passes(corner):
    return len(corner[corner['type'] == 'Pass'])

def get_corner_num_of_carrys(corner):
    return len(corner[corner['type'] == 'Carry'])

def get_corner_num_of_duels(corner):
    return len(corner[corner['type'] == 'Duel'])

def get_corner_num_of_ball_receipt(corner):
    return len(corner[corner['type'] == 'Ball Receipt*'])

def get_corner_num_of_shots(corner):
    return len(corner[corner['type'] == 'Shot'])