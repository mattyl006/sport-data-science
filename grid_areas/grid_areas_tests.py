import numpy as np
import pandas as pd
from statsbombpy import sb
from grid_areas import get_area_x, get_area_y, get_pass_area, add_grid_areas

def get_area_x_test():
    print('get_area_x_test')
    result = (get_area_x(0), get_area_x(5), get_area_x(6), get_area_x(10), get_area_x(11), get_area_x(60), get_area_x(61))
    print(result)
    if result == ('A', 'A', 'B', 'B', 'C', 'L', 'M'):
        print('get_area_x_test PASS\n\n')
    else:
        print('get_area_x_test FAIL\n\n')

def get_area_y_test():
    print('get_area_y_test')
    result = (get_area_y(0), get_area_y(5), get_area_y(6), get_area_y(10), get_area_y(11), get_area_y(60), get_area_y(61))
    print(result)
    if result == (1, 1, 2, 2, 3, 12, 13):
        print('get_area_y_test PASS\n\n')
    else:
        print('get_area_y_test FAIL\n\n')

def get_pass_area_test():
    print('get_pass_area_test')
    result = (get_pass_area([0, 0]), get_pass_area([1, 2]), get_pass_area([10, 60]), get_pass_area([6, 11]), get_pass_area([11, 62]))
    print(result)
    if result == ('A1', 'A1', 'B12', 'B3', 'C13'):
        print('get_pass_area_test PASS\n\n')
    else:
        print('get_pass_area_test FAIL\n\n')

def add_grid_areas_test1():
    passes = sb.events(match_id=3775648, split=True, flatten_attrs=False)["passes"]
    result1 = add_grid_areas(passes)
    result1.to_csv("passes_test.csv", encoding="utf-8", index=False)
    if result1['pass_area_code'][0] == 'M8M9':
        print('add_grid_areas_test1 PASS\n\n')
    else:
        print('add_grid_areas_test1 FAIL\n\n')

def add_grid_areas_test2():
    matches = sb.matches(competition_id=37, season_id=90)
    errorMessage = 'Error in add_grid_areas, perhaps: Bad dataframe in argument!'
    if add_grid_areas(matches) == errorMessage:
        print('add_grid_areas_test2 PASS\n\n')
    else:
        print('add_grid_areas_test2 FAIL\n\n')

def test():
    get_area_x_test()
    get_area_y_test()
    get_pass_area_test()
    add_grid_areas_test1()
    add_grid_areas_test2()

test()
