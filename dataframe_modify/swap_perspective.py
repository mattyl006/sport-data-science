import math

def swap_y(df, sb360=True):
    new_df = df
    new_start_ys = [(80.0 - float(start_y)) if start_y != '' else start_y 
                    for start_y in df['start_y'].values]
    new_end_ys = [(80.0 - float(start_y)) if start_y != '' else start_y 
                    for start_y in df['end_y'].values]
    if sb360:
        new_context_locations = [[[location[0], (80.0 - location[1])] 
            if location != '' else location for location in context_locations] 
            for context_locations in df['context_locations'].values]
        new_df['context_locations'] = new_context_locations
    new_df['start_y'] = new_start_ys
    new_df['end_y'] = new_end_ys
    return new_df

def swap_x(df, sb360=True):
    new_df = df
    new_start_xs = [(120.0 - float(start_x)) if start_x != '' else start_x 
                    for start_x in df['start_x'].values]
    new_end_xs = [(120.0 - float(end_x)) if end_x != '' else end_x 
                    for end_x in df['end_x'].values]
    if sb360:
        new_context_locations = [[[(120.0 - location[0]), location[1]] 
            if location != '' else location for location in context_locations] 
            for context_locations in df['context_locations'].values]
        new_df['context_locations'] = new_context_locations
    new_df['start_x'] = new_start_xs
    new_df['end_x'] = new_end_xs
    return new_df

def swap_perspective_sb360(event):
    new_context_locations = [[120.0 - float(c[0]), 80.0 - float(c[1]), 'swaped'] for c in event['context_locations']]
    event['context_locations'] = new_context_locations    
    return event

def swap_perspective(event):
    if event['start_x'] !='':
        event['start_x'] = 120.0 - float(event['start_x'])
        event['start_y'] = 80.0 - float(event['start_y'])
    if event['end_x'] != '':
        event['end_x'] = 120.0 - float(event['end_x'])
        event['end_y'] = 80.0 - float(event['end_y'])
    return event

def is_swap_required(event, start_team):
    swap_event_list = []
    event_type = event['type']
    team = event['team']
    return event_type in swap_event_list or \
        start_team != team and event_type not in swap_event_list

def is_swap_required_sb360(event):
    start_loc = None
    if event['start_x'] != '':
        start_loc = [event['start_x'], event['start_y']]
    end_loc = None
    if event['end_x'] != '':
        end_loc = [event['end_x'], event['end_y']]
    context_locations = event['context_locations']
    actor_locations = event['actor_locations']
    try:
        actor_loc = context_locations[actor_locations.tolist().index(True)]
    except:
        actor_loc = None
    if actor_loc is not None:
        actor_start_distance = None
        actor_end_distance = None
        if start_loc is not None:
            actor_start_distance = math.dist(actor_loc, start_loc)
        if end_loc is not None:
            actor_end_distance = math.dist(actor_loc, end_loc)
        if actor_end_distance is None:
            if actor_start_distance < 10.0:
                return False
        if actor_start_distance is None:
            if actor_end_distance < 10.0:
                return False
        if (actor_start_distance is not None) and (actor_end_distance is not None):
            if (actor_end_distance < 10.0) or (actor_start_distance < 10.0):
                return False
        return True
    return False

def generalize_perspective_sb360(df):
    return df.apply((lambda event: swap_perspective_sb360(event) 
                     if is_swap_required_sb360(event) 
                        else event), axis=1)

def generalize_perspective(df, start_team):
    return df.apply((lambda event: swap_perspective(event) 
                     if is_swap_required(event, start_team) 
                        else event), axis=1)