def swap_y(df):
    new_df = df
    new_start_ys = [abs(80.0 - float(start_y)) if start_y != '' else start_y 
                    for start_y in df['start_y'].values]
    new_end_ys = [abs(80.0 - float(start_y)) if start_y != '' else start_y 
                    for start_y in df['end_y'].values]
    new_df['start_y'] = new_start_ys
    new_df['end_y'] = new_end_ys
    return new_df

def swap_x(df):
    new_df = df
    new_start_xs = [abs(120.0 - float(start_x)) if start_x != '' else start_x 
                    for start_x in df['start_x'].values]
    new_end_xs = [abs(120.0 - float(end_x)) if end_x != '' else end_x 
                    for end_x in df['end_x'].values]
    new_df['start_x'] = new_start_xs
    new_df['end_x'] = new_end_xs
    return new_df

def generalize_perspective(df, start_team):
    new_df = df
    new_start_xs = [abs(120.0 - float(start_x)) if start_x != '' and team != start_team else start_x 
                    for start_x, team in zip(df['start_x'].values, df['team'].values)]
    new_start_ys = [abs(80.0 - float(start_y)) if start_y != '' and team != start_team else start_y 
                    for start_y, team in zip(df['start_y'].values, df['team'].values)]
    new_end_xs = [abs(120.0 - float(end_x)) if end_x != '' and team != start_team else end_x 
                    for end_x, team in zip(df['end_x'].values, df['team'].values)]
    new_end_ys = [abs(80.0 - float(end_y)) if end_y != '' and team != start_team else end_y 
                    for end_y, team in zip(df['end_y'].values, df['team'].values)]
    new_df['start_x'] = new_start_xs
    new_df['start_y'] = new_start_ys
    new_df['end_x'] = new_end_xs
    new_df['end_y'] = new_end_ys
    return new_df