def swap_condition(start_team, possession_team, team, event_type):
    if event_type == 'Duel':
        if  team != start_team:
            return True
        else:
            return False 
    elif possession_team != start_team:
        return True
    elif team != start_team:
        return True
    else:
        return False

def generalize_perspective(eventDataFrame):
    start_team = [team for team in eventDataFrame['possession_team'].values][0]
    new_start_locations = [
        [abs(120.0 - float(location[0])), abs(80.0 - float(location[1]))] 
            if swap_condition(start_team, possession_team, team, event_type) and location != '' else location 
            for location, possession_team, event_type, team
            in zip(eventDataFrame['location'].values, eventDataFrame['possession_team'].values, eventDataFrame['type'].values, eventDataFrame['team'].values)
    ]   
    newEventDataFrame = eventDataFrame
    newEventDataFrame['location'] = new_start_locations
    return newEventDataFrame

# def swap_perspective(sequence, start_team):
#     seq_team = [team for team in sequence['possession_team'].values][0]
#     if start_team != seq_team:
#         new_start_locations = [
#             [abs(120.0 - float(location[0])), abs(80.0 - float(location[1]))] 
#                 for location in sequence['location'].values]
#     newSequence = sequence
#     newSequence['location'] = new_start_locations
#     return newSequence