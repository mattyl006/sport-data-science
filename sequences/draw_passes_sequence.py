import matplotlib.pyplot as plt
from matplotlib.patches import Arc

def draw_pitch(ax):
    # size of the pitch is 120, 80
    #Create figure

    #Pitch Outline & Centre Line
    plt.plot([0,0],[0,80], color="black")
    plt.plot([0,120],[80,80], color="black")
    plt.plot([120,120],[80,0], color="black")
    plt.plot([120,0],[0,0], color="black")
    plt.plot([60,60],[0,80], color="black")

    #Left Penalty Area
    plt.plot([14.6,14.6],[57.8,22.2],color="black")
    plt.plot([0,14.6],[57.8,57.8],color="black")
    plt.plot([0,14.6],[22.2,22.2],color="black")

    #Right Penalty Area
    plt.plot([120,105.4],[57.8,57.8],color="black")
    plt.plot([105.4,105.4],[57.8,22.5],color="black")
    plt.plot([120, 105.4],[22.5,22.5],color="black")

    #Left 6-yard Box
    plt.plot([0,4.9],[48,48],color="black")
    plt.plot([4.9,4.9],[48,32],color="black")
    plt.plot([0,4.9],[32,32],color="black")

    #Right 6-yard Box
    plt.plot([120,115.1],[48,48],color="black")
    plt.plot([115.1,115.1],[48,32],color="black")
    plt.plot([120,115.1],[32,32],color="black")
    
    #Sectors
    plt.plot([120,0],[32,32], color="gray")
    plt.plot([120,0],[48,48], color="gray")
    plt.plot([120,0],[65,65], color="gray")
    plt.plot([120,0],[15,15], color="gray")
    plt.plot([14.6,14.6],[80,0], color="gray")
    plt.plot([105.4,105.4],[80,0], color="gray")
    plt.plot([40,40],[80,0], color="gray")
    plt.plot([80,80],[80,0], color="gray")
    
    #Prepare Circles
    centreCircle = plt.Circle((60,40),8.1,color="black",fill=False)
    centreSpot = plt.Circle((60,40),0.71,color="black")
    leftPenSpot = plt.Circle((9.7,40),0.71,color="black")
    rightPenSpot = plt.Circle((110.3,40),0.71,color="black")

    #Draw Circles
    ax.add_patch(centreCircle)
    ax.add_patch(centreSpot)
    ax.add_patch(leftPenSpot)
    ax.add_patch(rightPenSpot)

    #Prepare Arcs
    # arguments for arc
    # x, y coordinate of centerpoint of arc
    # width, height as arc might not be circle, but oval
    # angle: degree of rotation of the shape, anti-clockwise
    # theta1, theta2, start and end location of arc in degree
    leftArc = Arc((9.7,40),height=16.2,width=16.2,angle=0,theta1=310,theta2=50,color="black")
    rightArc = Arc((110.3,40),height=16.2,width=16.2,angle=0,theta1=130,theta2=230,color="black")

    #Draw Arcs
    ax.add_patch(leftArc)
    ax.add_patch(rightArc)

def draw_passes_sequence(sequence, start_team):
    fig, ax = plt.subplots()
    fig.set_size_inches(7, 5)
    i = 1

    for index, row in sequence.iterrows():
        plt.plot(int(row['pass_start_x']), int(row['pass_start_y']), marker='o',
        markersize=16, markeredgecolor="black", markerfacecolor="black")
        if row['possession_team'] == start_team:
            plt.plot([int(row['pass_start_x']), int(row['pass_end_x'])],
            [int(row['pass_start_y']),int(row['pass_end_y'])], color='blue')
        else:
            plt.plot([int(row['pass_start_x']), int(row['pass_end_x'])],
            [int(row['pass_start_y']),int(row['pass_end_y'])], color='red')
        plt.text(int(row['pass_start_x'])-1, int(row['pass_start_y'])-1, i,
        color='white', fontsize=8)
        i += 1

    print([team for team in sequence['possession_team']][0])
    draw_pitch(ax)
    plt.show()