from statsbombpy import sb
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from sequences.get_sequences import *
from sequences.draw_sequences import *
from sequences.which_sector import which_sector

def match_frames_id_sb360(match_id, event_id):
    
    match_frames = sb.frames(match_id, fmt='dataframe')
    match_frames = match_frames.loc[match_frames['id']==event_id]

    return match_frames

#frames = match_frames_id_sb360(3800107,'f7639670-8851-4df0-846a-bceead668983')

def plot_sb360(match_frames, def_areas_x, def_areas_y):
    
    teammate_locs = []
    opponent_locs = []

    for i in range(0,len(match_frames['teammate'])):
        if match_frames['teammate'][i:i+1].bool() == True:
            teammate_locs.append(match_frames[i:i+1])
        else:
            opponent_locs.append(match_frames[i:i+1])
    
    teammate_locs_x = []
    teammate_locs_y = []
    opponent_locs_x = []
    opponent_locs_y = []
    loc = match_frames['location']

    for i in range(0,len(loc)):
        if match_frames['teammate'][i:i+1].bool() == True:
            teammate_locs_x.append(loc[i:i+1].values[0][0])
            teammate_locs_y.append(loc[i:i+1].values[0][1])
        else:
            opponent_locs_x.append(loc[i:i+1].values[0][0])
            opponent_locs_y.append(loc[i:i+1].values[0][1])
            
    #plotting the teams on pitch
    draw_pitch(def_areas_x,def_areas_y)

    plt.scatter(teammate_locs_x, teammate_locs_y, c='orange', s=60, ec='k')
    plt.scatter(opponent_locs_x, opponent_locs_y, c='dodgerblue', s=60, ec='k')

    sectors_x = list()
    sectors_y = list()
    
    print('First (orange) team sectors:')
    for i in range (0,len(teammate_locs_x)):   
        sectors_x.append(which_sector(teammate_locs_x[i], teammate_locs_y[i],6,4))
    print(sectors_x)

    print('Second (blue) team sectors:')    
    for i in range (0,len(opponent_locs_x)):
        sectors_y.append(which_sector(opponent_locs_x[i], opponent_locs_y[i],6,4))
    print(sectors_y)

    #return teammate_locs_x, teammate_locs_y, opponent_locs_x, opponent_locs_y
    
