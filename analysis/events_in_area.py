from dataframe_modify.grid_areas import add_areas_and_pos

def events_in_area(events_df, team, event, areas_x=12, areas_y=8):
    df = events_df[events_df['possession_team'] == team]
    df = df[events_df['type'] == event]
    df = add_areas_and_pos(df)

    start_areas = [area for area in df['start_area'].values]
    start_areas_count = [(area, str(round((start_areas.count(area) / len(start_areas)) * 100, 2)) + '%') for area in start_areas]
    start_areas_count = list(set(start_areas_count))
    start_areas_count.sort(key=lambda y: y[0])

    return supply_empty_areas(start_areas_count, get_area_codes(areas_x, areas_y))


def get_area_codes(x, y):
    grid_Xs = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    result = []
    i = 1
    for area in grid_Xs:
        i += 1
        for k in range(y):
            result.append(area + str(k+1))
            if k > y:
                k = 1
                i += 1
        if i > x:
            break
    return result

def supply_empty_areas(start_areas_count, area_codes):
    areas = [item[0] for item in start_areas_count]

    for code in area_codes:
        if code not in areas:
            start_areas_count.append((code, '0%'))
            
    start_areas_count.sort(key=lambda y: y[0])
    return start_areas_count