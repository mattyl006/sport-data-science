from get_data.get_data import get_merged_events
from get_data.get_data import get_sb360
from dataframe_modify.add_positions import add_positions
from dataframe_modify.swap_perspective import swap_y
from dataframe_modify.swap_perspective import generalize_perspective, generalize_perspective_sb360
from dataframe_modify.grid_areas import add_grid_areas
from dataframe_modify.add_context import add_context
from sequences.get_sequences import get_sequences, get_sequences_by_possession
from draw.Draw import Draw
from dataframe_modify.swap_perspective import swap_x

def forward_perspective_sb360_flow(events_to_analize, match_id, sequences_n=100, seq_with_possesion=False):
    events = get_merged_events(events_to_analize, match_id)
    frames = get_sb360(match_id)
    start_team = events['possession_team'][0]
    events = add_context(events, frames)
    events = add_positions(events)
    events = swap_y(events)
    events = generalize_perspective_sb360(events)
    events = add_grid_areas(events)
    sequences = get_sequences(events)
    if seq_with_possesion:
        sequences = get_sequences_by_possession(events)
    draw = Draw(scale=2)
    start_team = events['possession_team'][0]
    second_half_sequences = None
    for i, s in enumerate(sequences[:sequences_n]):
        print(f'sequence {i}')
        draw.draw_sequence(s, start_team)
        if ('Half End' in s['type'].values):
            first_half_sequences = sequences[:i+1]
            second_half_sequences = sequences[i+1:]
            break
    if second_half_sequences is not None:
        second_half_sequences = [swap_x(sequence) for sequence in second_half_sequences]
        second_half_sequences = [add_grid_areas(s) for s in second_half_sequences]
        for i, s in enumerate(second_half_sequences[:(sequences_n-len(first_half_sequences))]):
            print(f'sequence {i}')
            draw.draw_sequence(s, start_team)

def generalized_perspective_only_events_flow(events_to_analize, match_id, sequences_n=100):
    events = get_merged_events(events_to_analize, match_id)
    start_team = events['possession_team'][0]
    events = add_positions(events)
    events = swap_y(events, sb360=False)
    events = generalize_perspective(events, start_team)
    events = add_grid_areas(events)
    sequences = get_sequences(events)
    draw = Draw(scale=2)
    start_team = events['possession_team'][0]
    second_half_sequences = None
    for i, s in enumerate(sequences[:sequences_n]):
        print(f'sequence {i}')
        draw.draw_sequence(s, start_team, sb360=False)
        if ('Half End' in s['type'].values):
            first_half_sequences = sequences[:i+1]
            second_half_sequences = sequences[i+1:]
            break
    if second_half_sequences is not None:
        second_half_sequences = [swap_x(sequence, sb360=False) for sequence in second_half_sequences]
        second_half_sequences = [add_grid_areas(s) for s in second_half_sequences]
        for i, s in enumerate(second_half_sequences[:(sequences_n-len(first_half_sequences))]):
            print(f'sequence {i}')
            draw.draw_sequence(s, start_team, sb360=False)
