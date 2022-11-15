from dataframe_modify.grid_areas import add_areas_and_pos

def events_in_area(events_df, team, event):
    df = events_df[events_df['possession_team'] == team]
    df = df[events_df['type'] == event]
    df = add_areas_and_pos(df)

    start_areas = [area for area in df['start_area'].values]
    start_areas_count = [(area, str(round((start_areas.count(area) / len(start_areas)) * 100, 2)) + '%') for area in start_areas]
    start_areas_count = list(set(start_areas_count))
    start_areas_count.sort(key=lambda y: y[0])

    return supply_empty_areas(start_areas_count)


def supply_empty_areas(start_areas_count):
    zero_area_count = []
    i = 1
    for area_count in start_areas_count:
        if int(area_count[0][1]) != i:
            zero_area_count.append(area_count[0][0] + str(i))
            i = int(area_count[0][1])
        i += 1
        if i > 8:
            i = 1

    for item in zero_area_count:
        start_areas_count.append((item, '0%'))

    start_areas_count.sort(key=lambda y: y[0])

    return start_areas_count