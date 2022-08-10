import numpy as np
import pandas as pd
from statsbombpy import sb

grid_Xs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def get_area_x(number):
    if number == 0:
        return grid_Xs[0]
    return grid_Xs[((number - 1) // 5)]

def get_area_y(number):
    if number == 0:
        return 1
    return ((number - 1) // 5) + 1

def get_pass_area(location):
    x = round(location[0])
    y = round(location[1])
    return f'{get_area_x(x)}{get_area_y(y)}'

def add_areas_and_pos(passesDataFrame):
    try:
        pass_start_locations = [[value[0], value[1]] for value in passesDataFrame['location'].values]
        pass_end_locations = [[value['end_location'][0], value['end_location'][1]] for value in passesDataFrame["pass"].values]

        pass_start_areas = [get_pass_area(location) for location in pass_start_locations]
        pass_end_areas = [get_pass_area(location) for location in pass_end_locations]
        pass_area_codes = [f'{a}{b}' for a,b in zip(pass_start_areas, pass_end_areas)]

        newPassesDataFrame = passesDataFrame

        newPassesDataFrame['pass_start_x'] = [value[0] for value in pass_start_locations]
        newPassesDataFrame['pass_start_y'] = [value[1] for value in pass_start_locations]
        newPassesDataFrame['pass_end_x'] = [value[0] for value in pass_end_locations]
        newPassesDataFrame['pass_end_y'] = [value[1] for value in pass_end_locations]

        newPassesDataFrame['pass_start_area'] = pass_start_areas
        newPassesDataFrame['pass_end_area'] = pass_end_areas
        newPassesDataFrame['pass_area_code'] = pass_area_codes
        
        return newPassesDataFrame

    except:
        print('Error in add_grid_areas, perhaps: Bad dataframe in argument!')
        return 'Error in add_grid_areas, perhaps: Bad dataframe in argument!'
