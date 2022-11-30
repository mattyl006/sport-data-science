def swap_perspective(sequence, start_team):
    new_sequence = sequence
    new_start_xs = [abs(120.0 - float(start_x)) if start_x != '' and team != start_team else start_x 
                    for start_x, team in zip(sequence['start_x'].values, sequence['team'].values)]
    new_start_ys = [abs(80.0 - float(start_y)) if start_y != '' and team != start_team else start_y 
                    for start_y, team in zip(sequence['start_y'].values, sequence['team'].values)]
    new_end_xs = [abs(120.0 - float(end_x)) if end_x != '' and team != start_team else end_x 
                    for end_x, team in zip(sequence['end_x'].values, sequence['team'].values)]
    new_end_ys = [abs(80.0 - float(end_y)) if end_y != '' and team != start_team else end_y 
                    for end_y, team in zip(sequence['end_y'].values, sequence['team'].values)]
    new_sequence['start_x'] = new_start_xs
    new_sequence['start_y'] = new_start_ys
    new_sequence['end_x'] = new_end_xs
    new_sequence['end_y'] = new_end_ys
    return new_sequence

def generalize_perspective(sequences):
    start_team = [team for team in sequences[0]['possession_team'].values][0]
    new_sequences = [swap_perspective(sequence, start_team) for sequence in sequences]
    return new_sequences