import matplotlib.pyplot as plt
from matplotlib.patches import Arc

def draw_pitch(ax, areas_x, areas_y, scale=1):
    # size of the pitch is 120, 80
    
    X = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']
    Y = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    #Pitch Outline & Centre Line
    plt.plot([0,0],[0,80*scale], color="black")
    plt.plot([0,120*scale],[80*scale,80*scale], color="black")
    plt.plot([120*scale,120*scale],[80*scale,0], color="black")
    plt.plot([120*scale,0],[0,0], color="black")
    plt.plot([60*scale,60*scale],[0,80*scale], color="black")
    
    for i in range (0,areas_x):
        plt.text((((60/areas_x)+i*120/areas_x)-1)*scale, 82*scale, X[i], fontdict=None, fontsize = 8*scale)
        
    for i in range (0,areas_y):
        plt.text(-3*scale, (((40/areas_y)+i*80/areas_y)-1)*scale, Y[i], fontdict=None, fontsize = 8*scale)

    #Left Penalty Area
    plt.plot([14.6*scale,14.6*scale],[57.8*scale,22.2*scale],color="black")
    plt.plot([0,14.6*scale],[57.8*scale,57.8*scale],color="black")
    plt.plot([0,14.6*scale],[22.2*scale,22.2*scale],color="black")

    #Right Penalty Area
    plt.plot([120*scale,105.4*scale],[57.8*scale,57.8*scale],color="black")
    plt.plot([105.4*scale,105.4*scale],[57.8*scale,22.5*scale],color="black")
    plt.plot([120*scale, 105.4*scale],[22.5*scale,22.5*scale],color="black")

    #Left 6-yard Box
    plt.plot([0,4.9*scale],[48*scale,48*scale],color="black")
    plt.plot([4.9*scale,4.9*scale],[48*scale,32*scale],color="black")
    plt.plot([0,4.9*scale],[32*scale,32*scale],color="black")

    #Right 6-yard Box
    plt.plot([120*scale,115.1*scale],[48*scale,48*scale],color="black")
    plt.plot([115.1*scale,115.1*scale],[48*scale,32*scale],color="black")
    plt.plot([120*scale,115.1*scale],[32*scale,32*scale],color="black")
    
    #Sectors
    for i in range(1, areas_y):
        plt.plot([120*scale,0],[(80/areas_y)*i*scale,(80/areas_y)*i*scale], color="gray")

    for i in range(1, areas_x):
        plt.plot([(120/areas_x)*i*scale,(120/areas_x)*i*scale],[80*scale,0], color="gray")
    
    #Prepare Circles
    centreCircle = plt.Circle((60*scale,40*scale),8.1*scale,color="black",fill=False)
    centreSpot = plt.Circle((60*scale,40*scale),0.71,color="black")
    leftPenSpot = plt.Circle((9.7*scale,40*scale),0.71,color="black")
    rightPenSpot = plt.Circle((110.3*scale,40*scale),0.71,color="black")

    #Draw Circles
    ax.add_patch(centreCircle)
    ax.add_patch(centreSpot)
    ax.add_patch(leftPenSpot)
    ax.add_patch(rightPenSpot)

def draw_passes_sequence(sequence, start_team, areas_x, areas_y, scale):
    if areas_x < 2:
        areas_x = 2
    if areas_y < 2:
        areas_y = 2
    if scale < 1:
        scale = 1

    fig, ax = plt.subplots()
    fig.set_size_inches(7*scale, 5*scale)
    i = 1
    
    team = [team for team in sequence['possession_team']][0]
    print(f'Team: {team}')

    for index, row in sequence.iterrows():
        plt.plot(int(row['start_x']*scale), int(row['start_y']*scale), marker='o',
        markersize=16, markeredgecolor="black", markerfacecolor="black")

        if row['possession_team'] == start_team:
            plt.plot([int(row['start_x']*scale), int(row['end_x']*scale)],
            [int(row['start_y']*scale),int(row['end_y']*scale)], color='blue')
        else:
            plt.plot([int(row['start_x']*scale), int(row['end_x']*scale)],
            [int(row['start_y']*scale),int(row['end_y']*scale)], color='red')

        plt.text(int(row['start_x']*scale)-1, int(row['start_y']*scale)-1, i,
        color='white', fontsize=8)
        
        player = row['player']
        print(f'{i}: {player}')

        i += 1


    draw_pitch(ax, areas_x, areas_y, scale)
    plt.show()


def draw_events_sequence(pass_sequence, start_team, areas_x, areas_y, scale, carrys_sequence=None):
    if areas_x < 2:
        areas_x = 2
    if areas_y < 2:
        areas_y = 2
    if scale < 1:
        scale = 1

    fig, ax = plt.subplots()
    fig.set_size_inches(7*scale, 5*scale)
    i = 1
    
    team = [team for team in pass_sequence['possession_team']][0]
    print(f'Team: {team}')

    for index, row in pass_sequence.iterrows():
        plt.plot(int(row['start_x']*scale), int(row['start_y']*scale), marker='o',
        markersize=16, markeredgecolor="black", markerfacecolor="black")

        if row['possession_team'] == start_team:
            plt.plot([int(row['start_x']*scale), int(row['end_x']*scale)],
            [int(row['start_y']*scale),int(row['end_y']*scale)], color='blue')
        else:
            plt.plot([int(row['start_x']*scale), int(row['end_x']*scale)],
            [int(row['start_y']*scale),int(row['end_y']*scale)], color='red')

        plt.text(int(row['start_x']*scale)-1, int(row['start_y']*scale)-1, i,
        color='white', fontsize=8)
        
        player = row['player']
        print(f'{i}: {player}')

        i += 1

    if not (carrys_sequence.empty):
        for index, row in carrys_sequence.iterrows():
            plt.plot(int(row['start_x']*scale), int(row['start_y']*scale), marker='o',
            markersize=4, markeredgecolor="red", markerfacecolor="red")

            if row['possession_team'] == start_team:
                plt.plot([int(row['start_x']*scale), int(row['end_x']*scale)],
                [int(row['start_y']*scale),int(row['end_y']*scale)], color='green')
            else:
                plt.plot([int(row['start_x']*scale), int(row['end_x']*scale)],
                [int(row['start_y']*scale),int(row['end_y']*scale)], color='green')

            plt.text(int(row['start_x']*scale)-1, int(row['start_y']*scale)-1, i,
            color='white', fontsize=8)
            
            player = row['player']
            print(f'{i}: {player}')

            i += 1

    draw_pitch(ax, areas_x, areas_y, scale)
    plt.show()