import pandas as pd


def get_sequences_from_list(list, name):
    arr = []
    for seq in range(len(list)):
        if len(list[seq]) > 0:
            for i in range(len(list[seq])):
                arr.append(list[seq][i])
    print(f"num of {name}: {len(arr)}")
    return arr


def get_goals_sequences(sequences):
    arr = []
    for sequence in sequences:
        for event_json in sequence['event'].values:
            if event_json != '':
                if event_json.get('outcome') != None:
                    if event_json.get('outcome', {}).get('name') == 'Goal':
                        arr.append(sequence)
    print(f"num of goal sequences : {len(arr)}")
    return arr

def get_gk_accurate_shot_saved_sequences(sequences):
    arr = []
    for sequence in sequences:
        for event_json in sequence['goalkeeper'].values:
            if event_json != '':
                if event_json.get('type') != None:
                    if event_json.get('type', {}).get('id') == 33: #keeper save from opposing team shot
                        arr.append(sequence)
    print(f"num of shots saved from opposing team: {len(arr)}")
    return arr


def get_saved_shots_sequences(sequences):
    arr = []
    for sequence in sequences:
        for event_json in sequence['event'].values:
            if event_json != '':
                if event_json.get('outcome') != None:
                    if event_json.get('outcome', {}).get('name') == 'Saved':
                        arr.append(sequence)
    print(f"num of saved shots: {len(arr)}")
    return arr


def get_inswinging_pasees_sequences(sequences):
    arr = []
    for sequence in sequences:
        for event_json in sequence['event'].values:
            if event_json != '':
                if event_json.get('technique') != None:
                    if event_json.get('technique', {}).get('name') == 'Inswinging':
                        arr.append(sequence)
    print(f"num of inswinging passes from corner: {len(arr)}")
    return arr

def get_outswinging_pasees_sequences(sequences):
    arr = []
    for sequence in sequences:
        for event_json in sequence['event'].values:
            if event_json != '':
                if event_json.get('technique') != None:
                    if event_json.get('technique', {}).get('name') == 'Outswinging':
                        arr.append(sequence)
    print(f"num of outswinging passes from corner: {len(arr)}")
    return arr

def get_straight_pasees_sequences(sequences):
    arr = []
    for sequence in sequences:
        for event_json in sequence['event'].values:
            if event_json != '':
                if event_json.get('technique') != None:
                    if event_json.get('technique', {}).get('name') == 'Straight':
                        arr.append(sequence)
    print(f"num of straight passes from corner: {len(arr)}")
    return arr
