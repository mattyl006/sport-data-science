import pandas as pd
import math

events_to_analize = ['Pass', 'Carry', 'Miscontrol', 'Dribble', 'Error', 'Duel', 'Ball Receipt*', 
'Clearance', 'Ball Recovery', 'Dispossessed', 'Interception', 'Block', 'Shot']

def get_fast_action_row(seq):
    new_df = pd.DataFrame()
    new_df['id'] = [get_sequence_id(seq)]
    new_df['team'] = [get_fast_action_team(seq)]
    new_df['duration'] = [get_fast_action_duration(seq)]
    for event_type in events_to_analize:
        event_type_str = event_type.replace(' ', '_').lower()
        new_df[f'num_of_{event_type_str}'] = [get_seq_num_of_event_type(seq, event_type)]
    new_df['num_of_events'] = [get_seq_num_of_events(seq)]
    new_df['path'] = [get_seq_path(seq)]
    new_df['start_area'] = [get_seq_start_area(seq)]
    new_df['end_area'] = [get_seq_end_area(seq)]
    new_df['start_x'] = [get_seq_start_loc(seq, 'start_x')]
    new_df['start_y'] = [get_seq_start_loc(seq, 'start_y')]
    new_df['end_x'] = [get_seq_end_loc(seq, 'x')]
    new_df['end_y'] = [get_seq_end_loc(seq, 'y')]
    new_df['key_pass_len'] = [get_key_pass_len(seq)]
    new_df['opponent_distances'] = [get_opponent_distances(seq)]
    new_df['obv_for'] = [get_fast_action_obv_for(seq)]
    new_df['obv_total'] = [get_fast_action_obv_for(seq)]
    new_df['xg'] = [get_fast_action__xg(seq)]
    return new_df

def get_sequence_id(seq):
    start_id = seq.iloc[0]['id']
    end_id = seq.iloc[-1]['id']
    return f'{start_id}#{end_id}'

def get_seq_num_of_event_type(seq, event_type):
    return len(seq[seq['type'] == event_type])

def get_fast_action_obv_for(seq):
    obv = 0
    for i in range(len(seq)):
        if seq.iloc[i]['obv_for_net']:
            obv += float(seq.iloc[i]['obv_for_net'])
    return obv

def get_fast_action_obv_total(seq):
    obv = 0
    for i in range(len(seq)):
        if seq.iloc[i]['obv_total_net']:
            obv += float(seq.iloc[i]['obv_total_net'])
    return obv

def get_fast_action__xg(seq):
    xg = 0
    for i in range(len(seq)):
        if seq.iloc[i]['type'] == 'Shot':
            if seq.iloc[i]['event'].get('statsbomb_xg') != None:
                print(seq.iloc[i]['event'].get('statsbomb_xg'))
                xg += float(seq.iloc[i]['event'].get('statsbomb_xg'))
    return xg

def get_seq_num_of_events(seq):
    n = 0
    for event_type in events_to_analize:
        n += get_seq_num_of_event_type(seq, event_type)
    return n

def get_fast_action_team(seq):
    return seq.iloc[0]['team']

def get_fast_action_duration(seq):
    return (seq.iloc[-1]['minute'] * 60 + seq.iloc[-1]['second']) - (seq.iloc[0]['minute'] * 60 - seq.iloc[0]['second'])

def get_seq_path(seq):
    path = []
    for start_area, end_area in zip(seq['start_area'].values, seq['end_area'].values):
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

def get_seq_start_area(seq):
    for start_area in seq['start_area'].values:
        if start_area != '':
            return start_area

def get_seq_end_area(seq):
    start_areas = seq['start_area'].values[::-1]
    end_areas = seq['end_area'].values[::-1]
    for start_area, end_area in zip(start_areas, end_areas):
        if end_area != '':
            return end_area
        if start_area != '':
            return start_area

def get_seq_start_loc(seq, loc):
    for loc in seq[loc].values:
        if loc != '':
            return loc

def get_seq_end_loc(seq, corrdinate):
    start_locations = seq[f'start_{corrdinate}'].values[::-1]
    end_locations = seq[f'end_{corrdinate}'].values[::-1]
    for start_loc, end_loc in zip(start_locations, end_locations):
        if end_loc != '':
            return end_loc
        if start_loc != '':
            return start_loc

def get_opponent_distances(seq):
    start_locations = [[start_x, start_y] for start_x, start_y in zip(seq['start_x'].values, seq['start_y'].values)]
    enemies_locations = []
    for context_locations, teammate_locations in zip(seq['context_locations'].values, seq['teammate_locations'].values):
        enemy_locations = [location if not teammate else '' for location, teammate in zip(context_locations, teammate_locations)]
        enemy_locations = list(filter(lambda a: a != '', enemy_locations))
        enemies_locations.append(enemy_locations)
    enemy_distances = 0
    n = 0
    for start_location, enemy_locations in zip(start_locations, enemies_locations):
        for enemy_location in enemy_locations:
            enemy_distances += math.dist(start_location, [enemy_location[0], enemy_location[1]])
            n += 1
    if n != 0:
        return enemy_distances / n
    return 0

def get_key_pass_len(seq):
    team_half = {'A', 'B', 'C', 'D', 'E', 'F'}
    for event_id, event_type, end_area in zip(seq['id'].values, seq['type'].values, seq['end_area'].values):
        if event_type == 'Pass' and end_area[0] not in team_half:
            key_pass = seq.loc[seq['id'] == event_id]
            start_x = key_pass['start_x'].values[0]
            start_y = key_pass['start_y'].values[0]
            end_x = key_pass['end_x'].values[0]
            end_y = key_pass['end_y'].values[0]
            return math.dist([start_x, start_y], [end_x, end_y])
    return 0