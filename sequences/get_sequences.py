import pandas as pd

def get_sequences_by_possession(df):
    sequences = []
    sequence = []
    split_events = {'Injury Stoppage', 'Half End'}
    prev_possession_team = df['possession_team'][0]
    prev_team = df['team'][0]
    prev_possesion = df['possession'][0]
    for _, row in df.iterrows():
        if row['team'] != prev_team or row['possession_team'] != prev_possession_team:
            if row['possession'] != prev_possesion or row['type'] in split_events:
                sequences.append(pd.DataFrame(sequence))
                sequence = []
        sequence.append(row)
        prev_possesion = row['possession']
        prev_possession_team = row['possession_team']
        prev_team = row['team']
    return sequences

def get_first_id(sequence):
    return sequence['index'].iloc[0]

def get_last_id(sequence):
    return sequence['index'].iloc[-1]

def get_sequence_location(sequence):
    loc = [sequence.start_x, sequence.start_y]
    locx = list()
    locy = list()

    for i in range (0,len(loc)):
        locx.append(loc.values[i][0])
        locy.append(loc.values[i][1])
    return [locx, locy]
