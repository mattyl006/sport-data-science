import pandas as pd
from corners.metric import *

events_to_analize = ['Pass', 'Carry', 'Miscontrol', 'Dribble', 'Error', 'Duel', 'Ball Receipt*', 
'Clearance', 'Ball Recovery', 'Dispossessed', 'Interception', 'Block', 'Shot']

def get_fast_action_row(df):
    new_df = pd.DataFrame()
    new_df['id'] = [get_sequence_id(df)]
    new_df['team'] = [get_fast_action_team(df)]
    new_df['duration'] = [get_fast_action_duration(df)]
    for event_type in events_to_analize:
        event_type_str = event_type.replace(' ', '_').lower()
        new_df[f'num_of_{event_type_str}'] = [get_df_num_of_event_type(df, event_type)]
    new_df['num_of_events'] = [get_df_num_of_events(df)]
    new_df['path'] = [get_df_path(df)]
    new_df['start_area'] = [get_df_start(df)]
    new_df['end_area'] = [get_df_end(df)]
    return new_df

def get_sequence_id(df):
    start_id = df.iloc[0]['id']
    end_id = df.iloc[-1]['id']
    return f'{start_id}-{end_id}'

def get_df_num_of_event_type(df, event_type):
    return len(df[df['type'] == event_type])

def get_fast_action_obv(corner):
    obv = 0
    for i in range(len(corner)):
        if corner.iloc[i]['obv_for_net']:
            obv += float(corner.iloc[i]['obv_for_net'])
    return obv

def get_fast_action__xg(corner):
    xg = 0
    for i in range(len(corner)):
        if corner.iloc[i]['type'] == 'Shot':
            if corner.iloc[i]['event'].get('statsbomb_xg') != None:
                print(corner.iloc[i]['event'].get('statsbomb_xg'))
                xg += float(corner.iloc[i]['event'].get('statsbomb_xg'))
    return xg

def get_df_num_of_events(df):
    n = 0
    for event_type in events_to_analize:
        n += get_df_num_of_event_type(df, event_type)
    return n

def get_fast_action_team(df):
    return df.iloc[0]['team']

def get_fast_action_duration(df):
    return (df.iloc[-1]['minute'] * 60 + df.iloc[-1]['second']) - (df.iloc[0]['minute'] * 60 - df.iloc[0]['second'])

def get_df_path(df):
    path = []
    for start_area, end_area in zip(df['start_area'].values, df['end_area'].values):
        if len(path) == 0:
            if start_area != '':
                path.append(start_area)
                if end_area != '' and end_area != start_area:
                    path.append(end_area)
        else:
            if start_area != '' and start_area != path[-1]:
                path.append(start_area)
            if end_area != '' and end_area != path[-1]:
                path.append(end_area)
    return path

def get_df_start(df):
    for start_area in df['start_area'].values:
        if start_area != '':
            return start_area

def get_df_end(df):
    start_areas = df['start_area'].values[::-1]
    end_areas = df['end_area'].values[::-1]
    for start_area, end_area in zip(start_areas, end_areas):
        if end_area != '':
            return end_area
        if start_area != '':
            return start_area

def get_opponent_distances(df):
    pass

def get_key_pass_len(df):
    pass