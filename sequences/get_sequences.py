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
