import pandas as pd

def get_event_sequences(events):
    sequences = []
    sequence = []
    team = events['possession_team'][0]
    for index, row in events.iterrows():
        if team != row['possession_team']:
            sequences.append(pd.DataFrame(sequence))
            sequence = []
        sequence.append(row)
        team = row['possession_team']
    return sequences

def get_sequences_by_possession(events):
    sequences = []
    sequence = []
    for i in range(0,len(events)):
        if (events['possession'] == i).any():
            sequence = events.loc[events['possession'] == i]
            sequences.append(pd.DataFrame(sequence))
    return sequences

def get_first_id(sequence):
    return sequence['index'].iloc[0]

def get_last_id(sequence):
    return sequence['index'].iloc[-1]

def get_additional_sequence(events, sequence):
    first_id = get_first_id(sequence)
    last_id = get_last_id(sequence)
    sequence = []
    for index, row in events.iterrows():
        if row['index'] > first_id and row['index'] < last_id:
            sequence.append(row)
    return(pd.DataFrame(sequence))

def get_additional_sequences(events_name, sequences):
    all_sequences = []
    for i, seq in enumerate(sequences):
        additional_sequence = get_additional_sequence(events_name, seq)
        all_sequences.append(pd.DataFrame(additional_sequence))
    return all_sequences

def get_sequence_location(sequence):
    loc = sequence.location
    locx = list()
    locy = list()

    for i in range (0,len(loc)):
        locx.append(loc.values[i][0])
        locy.append(loc.values[i][1])
    return [locx, locy]
