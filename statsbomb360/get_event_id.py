from statsbombpy import sb
import pandas as pd

def get_event(match_id, event_id):  
    match_events=sb.events(match_id)
    event = match_events[match_events['id']==event_id] 

    loc = event['location']
    x = loc.iloc[0][0]
    y = loc.iloc[0][1]

    return x,y

