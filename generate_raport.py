from get_data.get_data import get_matches
from dataframe_modify.add_positions import add_positions
from dataframe_modify.swap_perspective import swap_y
from dataframe_modify.swap_perspective import generalize_perspective
from dataframe_modify.grid_areas import add_grid_areas
from dataframe_modify.add_context import add_context
from get_data.get_data import get_merged_events
from get_data.get_data import get_sb360
from sequences.get_sequences import get_sequences_by_possession
from analysis.metric_fast_sequence import metric_fast_sequence
from draw.draw_sequences import draw_events_sequence
from sequences.find_fast_actions import find_fast_actions
from get_data.get_data import get_matches
from fpdf import FPDF

MATCH_ID = 3836322

matches = get_matches(38, 235)
match = matches[matches['match_id'] == MATCH_ID]

match_date = match['match_date'].values[0]
home_team = match['home_team'].values[0]
away_team = match['away_team'].values[0]

EVENTS_TO_ANALIZE = ['passes', 'carrys', 'ball_receipts', 'ball_recoverys', 'dribbles', 'blocks', 'clearances', 'duels',
'dispossesseds', 'errors', 'foul_committeds', 'foul_wons', 'half_ends', 'injury_stoppages', 'interceptions', 'miscontrols', 'shots']

frames = get_sb360(MATCH_ID)
events = get_merged_events(EVENTS_TO_ANALIZE, MATCH_ID)

team_1 = events['possession_team'][0]

events = add_context(events, frames)
events = add_positions(events)
events = swap_y(events)
events = generalize_perspective(events, team_1)
events = add_grid_areas(events)

sequences = get_sequences_by_possession(events)

team_2 = sequences[1]['possession_team'].values[0]

fast_attact_team_1 = find_fast_actions(sequences=sequences, team=team_1, start_team=team_1, half=1)

scores  = [metric_fast_sequence(s, team_1, team_1, 1) for s in fast_attact_team_1]

pdf = FPDF()
pdf.set_font("Arial", size = 10)

for i, seq, score in zip(range(len(fast_attact_team_1)), fast_attact_team_1, scores):
    pdf.add_page()
    text = f'{home_team} - {away_team} ({match_date})'
    text = text.encode('latin-1', 'replace').decode('latin-1')
    pdf.cell(200, 10, txt = text, ln = 1, align = 'L')
    text = f'sequence {i}'
    text = text.encode('latin-1', 'replace').decode('latin-1')
    pdf.cell(200, 10, txt = text, ln = 1, align = 'L')
    draw_events_sequence(seq, team_1, 12, 8, scale=2, scores=score[0], scores_locations=score[1], counterattack_pass_id=score[2], pdf=pdf)
    pdf.image('seq.png', x=-20, w = 250, h = 160, type = 'PNG')

pdf.output(f"raport-{home_team}-{away_team}({match_date}).pdf")
