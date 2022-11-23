def generalize_perspective(eventDataFrame):
    start_team = [team for team in eventDataFrame['possession_team'].values][0]
    print(eventDataFrame['type'].values)
    new_start_locations = [
        [abs(120.0 - float(location[0])), abs(80.0 - float(location[1]))] 
            if ((event_type != 'Duel' and possession_team != start_team) or (event_type == 'Duel' and team != start_team)) and location != '' else location 
            for location, possession_team, event_type, team
            in zip(eventDataFrame['location'].values, eventDataFrame['possession_team'].values, eventDataFrame['type'].values, eventDataFrame['team'].values)
    ]
    
    newEventDataFrame = eventDataFrame
    newEventDataFrame['location'] = new_start_locations
    return newEventDataFrame