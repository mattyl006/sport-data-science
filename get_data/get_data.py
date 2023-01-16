from statsbombpy import sb
import pandas as pd

def get_competitions():
    return sb.competitions()

def get_matches(c_id, s_id):
    matches = sb.matches(competition_id=c_id, season_id=s_id)
    return matches

def get_events(event_types, m_id):
    df = []
    events = sb.events(match_id=m_id, split=True, flatten_attrs=False)

    for event_type in event_types:
        if len(events[event_type]):
            df.append(events[event_type])

    return df

def get_event_json_col_name(event_type):
    return event_type.lower().replace(' ', '_').replace('*', '')

def get_types_without_json_column(events_dfs):
    types_without_json_column = set()
    for event_df in events_dfs:
        event_type = event_df['type'][0]
        try:
            # check if event_df has json event column
            event_df[get_event_json_col_name(event_type)][0]
        except:
            # if not add type to set
            types_without_json_column.add(event_type)
    return types_without_json_column

def get_merged_events(events_types, match_id):
    events_dfs = get_events(events_types, match_id)

    types_without_json_column = get_types_without_json_column(events_dfs)
    
    events_dfs_renamed = []

    for event_df in events_dfs:
        event_type = event_df['type'][0]
        if event_type not in types_without_json_column:
            events_dfs_renamed.append(event_df.rename(columns={get_event_json_col_name(event_type) : 'event'}))
        else:
            events_dfs_renamed.append(event_df)

    events = pd.concat(events_dfs_renamed, ignore_index=True)
    events = events.fillna('')

    return events.sort_values('index', ignore_index=True)

# def get_merged_events(events_types, match_id):
#     events_dfs = []
#     for event_type in events_types:
#         df = get_events(event_type, match_id)
#         if len(df) != 0: 
#             events_dfs.append(get_events(event_type, match_id))

#     types_without_json_column = get_types_without_json_column(events_dfs)
    
#     events_dfs_renamed = []

#     for event_df in events_dfs:
#         event_type = event_df['type'][0]
#         if event_type not in types_without_json_column:
#             events_dfs_renamed.append(event_df.rename(columns={get_event_json_col_name(event_type) : 'event'}))
#         else:
#             events_dfs_renamed.append(event_df)

#     events = pd.concat(events_dfs_renamed, ignore_index=True)
#     events = events.fillna('')

#     return events.sort_values('index', ignore_index=True)

def get_sb360(match_id):
    return sb.frames(match_id, fmt='dataframe')