import matplotlib.pyplot as plt
from matplotlib.patches import Arc

def draw_pitch(ax, areas=5, scale=1):
    # size of the pitch is 120, 80

    #Pitch Outline & Centre Line
    plt.plot([0,0],[0,80*scale], color="black")
    plt.plot([0,120*scale],[80*scale,80*scale], color="black")
    plt.plot([120*scale,120*scale],[80*scale,0], color="black")
    plt.plot([120*scale,0],[0,0], color="black")
    plt.plot([60*scale,60*scale],[0,80*scale], color="black")

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
    for i in range(1, areas):
        plt.plot([120*scale,0],[(80/areas)*i*scale,(80/areas)*i*scale], color="gray")

    for i in range(1, areas):
        plt.plot([(120/areas)*i*scale,(120/areas)*i*scale],[80*scale,0], color="gray")
    
    #Prepare Circles
    centreCircle = plt.Circle((60*scale,40*scale),8.1,color="black",fill=False)
    centreSpot = plt.Circle((60*scale,40*scale),0.71,color="black")
    leftPenSpot = plt.Circle((9.7*scale,40*scale),0.71,color="black")
    rightPenSpot = plt.Circle((110.3*scale,40*scale),0.71,color="black")

    #Draw Circles
    ax.add_patch(centreCircle)
    ax.add_patch(centreSpot)
    ax.add_patch(leftPenSpot)
    ax.add_patch(rightPenSpot)

def draw_passes_sequence(sequence, start_team, areas=5, scale=1):
    if areas < 2:
        areas = 2
    if scale < 1:
        scale = 1

    fig, ax = plt.subplots()
    fig.set_size_inches(7*scale, 5*scale)
    i = 1

    for index, row in sequence.iterrows():
        plt.plot(int(row['pass_start_x']*scale), int(row['pass_start_y']*scale), marker='o',
        markersize=16, markeredgecolor="black", markerfacecolor="black")
        if row['possession_team'] == start_team:
            plt.plot([int(row['pass_start_x']*scale), int(row['pass_end_x']*scale)],
            [int(row['pass_start_y']*scale),int(row['pass_end_y']*scale)], color='blue')
        else:
            plt.plot([int(row['pass_start_x']*scale), int(row['pass_end_x']*scale)],
            [int(row['pass_start_y']*scale),int(row['pass_end_y']*scale)], color='red')
        plt.text(int(row['pass_start_x']*scale)-1, int(row['pass_start_y']*scale)-1, i,
        color='white', fontsize=8)
        i += 1

    print([team for team in sequence['possession_team']][0])
    draw_pitch(ax, areas, scale)
    plt.show()