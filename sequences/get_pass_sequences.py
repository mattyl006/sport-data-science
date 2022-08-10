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