import pandas as pd

def get_sequences_by_possession(df):
    sequences = []
    sequence = []
    split_events = {'Injury Stoppage', 'Half End', 'Foul Committed'}
    prev_team = df['team'][0]
    prev_possession_team = df['possession_team'][0]
    # prev_possesion = df['possession'][0]

    for _, row in df.iterrows():
        if row['type'] in split_events:
            if len(sequence) != 0:
                sequence.append(row)
                sequences.append(pd.DataFrame(sequence))
                sequence = []
            continue
        #  and row['possession'] != prev_possesion
        elif (row['possession_team'] != prev_possession_team or row['team'] != prev_team):
            if len(sequence) != 0:
                sequences.append(pd.DataFrame(sequence))
                sequence = []
        sequence.append(row)
        prev_team = row['team']
        # prev_possesion = row['possession']
        prev_possession_team = row['possession_team']

    return sequences

def get_corners_sequences(sequences):
    # return [sequence for sequence in sequences if (sequence['play_pattern'] == 'From Corner').any()]
    arr = []
    # print(len(sequences))
    for i, sequence in enumerate(sequences):
        try:
            if (sequence['play_pattern'] == 'From Corner').any():
                arr.append(sequence)
        except:
            print(sequence)
            print(i)
        
    return arr



# def get_corners_sequences(df):
#     sequences = []
#     sequence = []
#     for i in range(0,len(df)):
#         if ((df['possession'] == i) & (df['play_pattern'] == 'From Corner')).any():
#             sequence = df.loc[df['possession'] == i]        
#             sequences.append(pd.DataFrame(sequence))
#     return sequences


def get_sequence_by_time(sequences, period, minute, second):
    for i in range (0,len(sequences)):
        if ((sequences[i]['period'] == period) & (sequences[i]['minute'] >= minute) & (sequences[i]['second'] >= second)).any():
            return sequences[i]
    print('Exception in get_sequence_by_time! Bad timestamp probably!')

        

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
