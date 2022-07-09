from grid_areas import get_area_x, get_area_y

def get_area_x_test():
    result = (get_area_x(0), get_area_x(5), get_area_x(6), get_area_x(10), get_area_x(11), get_area_x(60), get_area_x(61))
    if result == ('A', 'A', 'B', 'B', 'C', 'L', 'M'):
        return 'get_area_x_test PASS'
    return 'get_area_x_test FAIL'

def get_area_y_test():
    result = (get_area_y(0), get_area_y(5), get_area_y(6), get_area_y(10), get_area_y(11), get_area_y(60), get_area_y(61))
    if result == (1, 1, 2, 2, 3, 12, 13):
        return 'get_area_y_test PASS'
    return 'get_area_y_test FAIL'

print(get_area_x_test())
print(get_area_y_test())
