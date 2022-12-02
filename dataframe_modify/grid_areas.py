grid_Xs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
grid_Ys = [i+1 for i in range(20)]

def get_area_x(loc_x, areas_x):
    for i in range (0,areas_x+1):
        if loc_x <= (120/areas_x)*i and loc_x > (120/areas_x)*(i-1):
            return grid_Xs[i-1]
    return "Error in get_area_x!"

def get_area_y(loc_y, areas_y):
    for i in range (0, areas_y+1):
        if loc_y <= (areas_y*10) - (i * 10) and loc_y > ((areas_y*10) -10) - (i * 10):
            return grid_Ys[i]
    return "Error in get_area_y!"

def get_event_area(location, areas_x, areas_y):
    x = location[0]
    y = location[1]
    return f'{get_area_x(x, areas_x)}{get_area_y(y, areas_y)}'

def add_grid_areas(df, x_areas = 12, y_areas = 8):
    event_start_areas = [get_event_area([start_x, start_y], x_areas, y_areas) 
                         if start_x != '' or start_y != '' else '' for start_x, start_y in zip(df['start_x'].values, df['start_y'].values)]
    event_end_areas = [get_event_area([end_x, end_y], x_areas, y_areas) 
                       if end_x != '' or end_y != '' else '' for end_x, end_y in zip(df['end_x'].values, df['end_y'].values)]
    event_area_codes = [f'{x}{y}' for x,y in zip(event_start_areas, event_end_areas)]
    df['start_area'] = event_start_areas
    df['end_area'] = event_end_areas
    df['area_code'] = event_area_codes
    return df