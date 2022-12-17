from analysis.timestamp_difference import timestamp_difference
from dataframe_modify.swap_perspective import swap_x
from sequences.split_sequences_by_half import split_sequences_by_half
from dataframe_modify.grid_areas import add_grid_areas

def find_fast_actions(sequences, team, start_team, half, max_timestamp=15000):
    fast_attact_sequences = []
    sequences = split_sequences_by_half(sequences)[half - 1]
    if team == start_team and half == 1:
        team_half = {'A', 'B', 'C', 'D', 'E', 'F'}
    elif team != start_team and half == 2:
        team_half = {'A', 'B', 'C', 'D', 'E', 'F'}
    else:
        team_half = {'G', 'H', 'I', 'J', 'K', 'L'}
    if half == 2:
        sequences = [swap_x(s) for s in sequences]
        sequences = [add_grid_areas(s) for s in sequences]
    for s in sequences:
        possesion_team = s['possession_team'].values[0]
        start_area = s['start_area'].values[0]
        end_area = s['start_area'].values[-1]
        start_timestamp = s['timestamp'].values[0]
        end_timestamp = s['timestamp'].values[-1]
        timestamp_diff = timestamp_difference(start_timestamp, end_timestamp)
        if start_area != '' and end_area != '' and possesion_team == team:
            if start_area[0] in team_half and end_area[0] not in team_half and timestamp_diff < max_timestamp:
                fast_attact_sequences.append(s)
    return fast_attact_sequences

# Klasyfikacja szybkich ataków
# W momencie kluczowego długiego podania brać lokalizacje przeciwników na przecięciu (po drodze) tego podania
# Badając w ten sposób czy podanie było "trudne" czy "łatwe"
# Jeśli trudne i się udało to odpowiednio wynagrodzić
# Jeśli trudne i się nie udało to mniej wynagrodzić
# Jeśli łatwe i nieudane to kara
# Jeśli łatwe i udane to wynagrodzić ale mniej niż to pierwsze
# Jeśli podanie zostanie przyjęte i po nim jest wysoki pressing to mniej wynagrodzić
# Jeśli podanie zostanie przyjęte i jest dużo otwartej przestrzeni to jeszcze bardziej wynagrodzić
# Jeśli przyjęcie będzie do stopy to bardziej wynagrodzić (?)
