import pandas as pd

def get_pass_sequences(passes):
    sequences = []
    sequence = []
    team = passes['possession_team'][0]
    for index, row in passes.iterrows():
        if team != row['possession_team']:
            sequences.append(pd.DataFrame(sequence))
            sequence = []
        sequence.append(row)
        team = row['possession_team']
    return sequences

def get_first_id(sequence):
    return sequence['index'][0]

def get_last_id(sequence):
    return sequence['index'].iloc[-1]

def get_additional_sequence(events, pass_sequence):
    first_id = get_first_id(pass_sequence)
    last_id = get_last_id(pass_sequence)
    sequence = []
    for index, row in events.iterrows():
        if row['index'] > first_id and row['index'] < last_id:
            sequence.append(row)
    return(pd.DataFrame(sequence))

def get_additional_sequences(events, pass_sequences):
    sequences = []
    for i, s in enumerate(pass_sequences):
        sequence = get_additional_sequence(events, pass_sequences[i])
        sequences.append(sequence)
    return sequences
