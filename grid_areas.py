grid_Xs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def get_area_x(number):
    print(number)
    if number == 0:
        return grid_Xs[0]
    return grid_Xs[((number - 1) // 5)]

def get_area_y():
    pass

def get_pass_start_area(location):
    x = round(location[0])
    y = round(location[1])
    return get_area_x(x)

def add_grid_areas(passes):
    dataframe = passes
    return get_pass_start_area(dataframe['location'][0])

print(get_area_x(0))
print(get_area_x(5))
print(get_area_x(6))
print(get_area_x(60))
print(get_area_x(61))
