import pandas as pd

def get_event_locations(df, event, team=None):
    df_event = df.loc[df['type'] == event]
    if team is not None:
        df_event = df_event.loc[df['possession_team'] == team]
    location_xy = df_event.location.apply(pd.Series)
    location_xy.columns = ['x', 'y']
    return location_xy