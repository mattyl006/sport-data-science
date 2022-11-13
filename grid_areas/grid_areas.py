import numpy as np
import pandas as pd
from statsbombpy import sb

grid_Xs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
grid_Ys = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

def get_area_x(loc_x, areas_x):
    for i in range (0,areas_x+1):
        if loc_x <= (120/areas_x)*i and loc_x > (120/areas_x)*(i-1):
            return grid_Xs[i-1]
    return "Error in get_area_x!"

def get_area_y(loc_y, areas_y):
    for i in range (0,areas_y+1):
        if loc_y <= (80/areas_y)*i and loc_y > (80/areas_y)*(i-1):
            return grid_Ys[i-1]
    return "Error in get_area_y!"

def get_event_area(location, areas_x, areas_y):
    x = location[0]
    y = location[1]
    return f'{get_area_x(x, areas_x)}{get_area_y(y, areas_y)}'

def add_areas_and_pos(eventDataFrame, eventName, areas_x = 12, areas_y = 8):
    try:
        event_start_locations = [[value[0], value[1]] for value in eventDataFrame['location'].values]
        event_end_locations = [[value['end_location'][0], value['end_location'][1]] for value in eventDataFrame[eventName].values]

        event_start_areas = [get_event_area(location, areas_x, areas_y) for location in event_start_locations]
        event_end_areas = [get_event_area(location, areas_x, areas_y) for location in event_end_locations]
        event_area_codes = [f'{a}{b}' for a,b in zip(event_start_areas, event_end_areas)]

        newEventDataFrame = eventDataFrame

        newEventDataFrame['start_x'] = [value[0] for value in event_start_locations]
        newEventDataFrame['start_y'] = [value[1] for value in event_start_locations]
        newEventDataFrame['end_x'] = [value[0] for value in event_end_locations]
        newEventDataFrame['end_y'] = [value[1] for value in event_end_locations]

        newEventDataFrame['start_area'] = event_start_areas
        newEventDataFrame['end_area'] = event_end_areas
        newEventDataFrame['area_code'] = event_area_codes
        
        return newEventDataFrame

    except:
        print('Error in add_grid_areas, perhaps: Bad dataframe in argument!')
        return 'Error in add_grid_areas, perhaps: Bad dataframe in argument!'