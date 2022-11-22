def generalize_perspective(eventDataFrame):
    start_team = [team for team in eventDataFrame['possession_team'].values][0]
    new_start_locations = [[abs(120.0 - float(location[0])), abs(80.0 - float(location[1]))] if team != start_team and location != '' else location for location,team in zip(eventDataFrame['location'].values, eventDataFrame['possession_team'].values)]
    
    newEventDataFrame = eventDataFrame
    newEventDataFrame['location'] = new_start_locations
    return newEventDataFrame