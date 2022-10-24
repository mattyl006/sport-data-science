from statsbombpy import sb
import pandas as pd

def get_related_events(competition_id, season_id, match_id, event_id):
    df = sb.matches(competition_id, season_id)
    #df.to_csv('matches.csv', index=False)
    
    match_events = sb.events(match_id)
    #match_events.to_csv('events.csv', index=False)
    event = match_events[match_events['id']==event_id] 
    related_events = match_events[match_events['id']==event_id]['related_events'].values[0]
    event_type = event['type']
    
    print('Your event_id type was: ' + event_type)
    
    print('Related events are: ' + str(related_events))

    return related_events


#related_events = get_related_events(38, 108, 3800107, 'f7639670-8851-4df0-846a-bceead668983')
