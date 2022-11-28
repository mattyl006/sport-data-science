import pandas as pd

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

def get_sequence_location(sequence):
    loc = sequence.location
    locx = list()
    locy = list()

    for i in range (0,len(loc)):
        locx.append(loc.values[i][0])
        locy.append(loc.values[i][1])
    return [locx, locy]
