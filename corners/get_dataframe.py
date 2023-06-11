import pandas as pd
from corners.metric import *
import os

def prepare_matches_from_pkl(pkl_path):
    pkl_preprocessed_path = pkl_path[:-4] + '_preprocessed.pkl'
    if not os.path.exists(pkl_preprocessed_path):
        matches = pd.read_pickle(pkl_path)
        matches = add_positions(matches)
        matches, matches_without_sb360 = swap_y(matches)
        for match_id in matches_without_sb360:
            matches = matches[matches['match_id'] != match_id]
        matches = generalize_perspective_sb360(matches)
        matches = add_grid_areas(matches)
        matches.to_pickle(pkl_preprocessed_path)
        return matches
    return pd.read_pickle(pkl_preprocessed_path)

default_events_to_analize = ['Pass', 'Carry', 'Miscontrol', 'Dribble', 'Error', 'Duel', 'Ball Receipt*', 
'Clearance', 'Ball Recovery', 'Dispossessed', 'Interception', 'Block', 'Shot']

def get_df_row(corner, events_to_analize=default_events_to_analize, end_pass_zones = False, shot_on_goal = False):
    """Get the row to dataframe of the corner."""
    corner_df = pd.DataFrame()
    corner_df['id'] = [get_sequence_id(corner)]
    corner_df['team'] = [get_corner_team(corner)]
    # corner_df['opponent'] = [get_corner_opponent(corner)]
    corner_df['num_of_events'] = [get_corner_num_of_events(corner)]
    corner_df['duration'] = [get_corner_duration(corner)]
    
    for event_type in events_to_analize:
        event_type_str = event_type.replace(' ', '_').lower()
        corner_df[f'num_of_{event_type_str}'] = [get_df_num_of_event_type(corner, event_type)]
    
    #TODO: consider adding num of passes to the zones

    corner_df['corner_score'] = [get_conrner_score(corner)]
    corner_df['obv'] = [get_corner_obv(corner)]
    corner_df['xg'] = [get_corner_xg(corner)]

    if end_pass_zones:
        for zone in ['I', 'II', 'LZ', 'RZ', 'LO', 'CO', 'RO', 'LP', 'RP', 'CP']:
            corner_df[f'num_of_passes_to_{zone}'] = 0
        for i in range(len(corner)):
            if corner.iloc[i]['type'] == 'Pass':
                zone = get_end_zone(corner.iloc[i]['end_x'], corner.iloc[i]['end_y'])
                corner_df[f'num_of_passes_to_{zone}'] += 1
    
    if shot_on_goal:
        corner_df['shot_on_goal'] = [get_shot_on_goal(corner)]

    return corner_df

def get_sequence_id(df):
    start_id = df.iloc[0]['id']
    end_id = df.iloc[-1]['id']
    return f'{start_id}#{end_id}'

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
                xg += float(corner.iloc[i]['event'].get('statsbomb_xg'))
    return xg

def get_conrner_score(corner):
    cs = 0
    for i in range(len(corner)):
        if corner.iloc[i]['corner_score']:
            cs += float(corner.iloc[i]['corner_score'])
    return cs

def get_corner_num_of_events(corner):
    return len(corner)

def get_corner_team(corner):
    return corner.iloc[0]['team']

def get_corner_opponent(corner):    
    #TODO: write this function
    pass

def get_corner_duration(corner):
    return (corner.iloc[-1]['minute'] * 60 + corner.iloc[-1]['second']) - (corner.iloc[0]['minute'] * 60 - corner.iloc[0]['second'])

def get_df_num_of_events(df):
    n = 0
    for event_type in events_to_analize:
        n += get_df_num_of_event_type(df, event_type)
    return n

def get_df_num_of_event_type(df, event_type):
    return len(df[df['type'] == event_type])

def get_shot_on_goal(corner):
    for i in range(len(corner)):
        if corner.iloc[i]['type'] == 'Shot':
            if corner.iloc[i]['event'].get('outcome') != None:
                outcome = corner.iloc[i]['event'].get('outcome', {}).get('name')
                if outcome not in ['Blocked', 'Off T']:
                    return 1
    return 0