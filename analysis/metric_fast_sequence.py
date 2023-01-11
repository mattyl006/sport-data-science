from analysis.distance_from_line import distance_from_line

def metric_fast_sequence(df, team, start_team, half):
    counterattack_pass = None
    scores = []
    enemy_locations = []
    if team == start_team and half == 1:
        team_half = {'A', 'B', 'C', 'D', 'E', 'F'}
    elif team != start_team and half == 2:
        team_half = {'A', 'B', 'C', 'D', 'E', 'F'}
    else:
        team_half = {'G', 'H', 'I', 'J', 'K', 'L'}
    for event_id, event_type, end_area in zip(df['id'].values, df['type'].values, df['end_area'].values):
        if event_type == 'Pass' and end_area[0] not in team_half:
            counterattack_pass = df.loc[df['id'] == event_id]
            break;
    if counterattack_pass is not None:
        context_locations = counterattack_pass['context_locations'].values[0]
        teammate_locations = counterattack_pass['teammate_locations'].values[0]

        enemy_locations = [location if not teammate else '' for location, teammate 
                            in zip(context_locations, teammate_locations)]
        enemy_locations = list(filter(lambda a: a != '', enemy_locations))

        counterattack_pass_path = [(counterattack_pass.start_x.values[0], counterattack_pass.start_y.values[0]),
        (counterattack_pass.end_x.values[0], counterattack_pass.end_y.values[0])]

        enemy_locations = [location if distance_from_line(counterattack_pass_path[0], 
        counterattack_pass_path[1], location) < 20 else '' for location in enemy_locations]
        enemy_locations = list(filter(lambda a: a != '', enemy_locations))

        distances = [distance_from_line(counterattack_pass_path[0], counterattack_pass_path[1], location)
            for location in enemy_locations]
        print(distances)
        scores = [round(1/distance, 6) for distance in distances]
    if scores is None:
        scores = []
    if enemy_locations is None:
        enemy_locations = []
    return scores, enemy_locations

# nie <20 tylko uzależnić od długości podania np. połowa długości podania
# zrobić odcinek nie prostą