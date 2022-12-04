def add_positions(df):
    event_start_positions = [[value[0], value[1]] if value != '' else '' for value in df['location'].values]
    event_end_positions = [[value['end_location'][0], value['end_location'][1]] 
                           if value != '' and 'end_location' in value.keys() else '' for value in df['event'].values]
    df['start_x'] = [value[0] if value != '' else '' for value in event_start_positions]
    df['start_y'] = [value[1] if value != '' else '' for value in event_start_positions]
    df['end_x'] = [value[0] if value != '' else '' for value in event_end_positions]
    df['end_y'] = [value[1] if value != '' else '' for value in event_end_positions]
    return df