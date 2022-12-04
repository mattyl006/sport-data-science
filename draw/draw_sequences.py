import matplotlib.pyplot as plt

def draw_pitch(ax, x_areas=12, y_areas=8, scale=1):
    # size of the pitch is 120, 80
    X = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']
    Y = [i+1 for i in range(20)]

    #Pitch Outline & Centre Line
    plt.plot([0,0],[0,80*scale], color="black")
    plt.plot([0,120*scale],[80*scale,80*scale], color="black")
    plt.plot([120*scale,120*scale],[80*scale,0], color="black")
    plt.plot([120*scale,0],[0,0], color="black")
    plt.plot([60*scale,60*scale],[0,80*scale], color="black")
    
    for i in range (0,x_areas):
        plt.text((((60/x_areas)+i*120/x_areas)-1)*scale, 82*scale, str(X[i]), fontsize=8*scale)

    for i in range (0,y_areas):
        plt.text(-3*scale, (80 * scale) - (5.5 * scale) - (i * 10 * scale), str(Y[i]), fontsize=8*scale)

    # Left Penalty Area
    plt.plot([14.6*scale,14.6*scale],[57.8*scale,22.2*scale],color="black")
    plt.plot([0,14.6*scale],[57.8*scale,57.8*scale],color="black")
    plt.plot([0,14.6*scale],[22.2*scale,22.2*scale],color="black")

    # Right Penalty Area
    plt.plot([120*scale,105.4*scale],[57.8*scale,57.8*scale],color="black")
    plt.plot([105.4*scale,105.4*scale],[57.8*scale,22.5*scale],color="black")
    plt.plot([120*scale, 105.4*scale],[22.5*scale,22.5*scale],color="black")

    # Left 6-yard Box
    plt.plot([0,4.9*scale],[48*scale,48*scale],color="black")
    plt.plot([4.9*scale,4.9*scale],[48*scale,32*scale],color="black")
    plt.plot([0,4.9*scale],[32*scale,32*scale],color="black")

    # Right 6-yard Box
    plt.plot([120*scale,115.1*scale],[48*scale,48*scale],color="black")
    plt.plot([115.1*scale,115.1*scale],[48*scale,32*scale],color="black")
    plt.plot([120*scale,115.1*scale],[32*scale,32*scale],color="black")
    
    # Sectors
    for i in range(1, y_areas):
        plt.plot([120*scale,0],[(80/y_areas)*i*scale,(80/y_areas)*i*scale], color="gray")

    for i in range(1, x_areas):
        plt.plot([(120/x_areas)*i*scale,(120/x_areas)*i*scale],[80*scale,0], color="gray")
    
    # Prepare Circles
    centreCircle = plt.Circle((60*scale,40*scale),8.1*scale,color="black",fill=False)  # type: ignore
    centreSpot = plt.Circle((60*scale,40*scale),0.71,color="black") # type: ignore
    leftPenSpot = plt.Circle((9.7*scale,40*scale),0.71,color="black") # type: ignore
    rightPenSpot = plt.Circle((110.3*scale,40*scale),0.71,color="black") # type: ignore

    # Draw Circles
    ax.add_patch(centreCircle)
    ax.add_patch(centreSpot)
    ax.add_patch(leftPenSpot)
    ax.add_patch(rightPenSpot)

def draw_events_sequence(sequence, start_team, x_areas=12, y_areas=8, scale=1):
    if x_areas < 2:
        x_areas = 2
    if y_areas < 2:
        y_areas = 2
    if scale < 1:
        scale = 1

    events_without_location = {'Injury Stoppage', 'Half End'}
    fig, ax = plt.subplots()
    fig.set_size_inches(7*scale, 5*scale)
    i = 0
    team = [team for team in sequence['possession_team']][0]
    player = ''
    
    print(f'Team: {team}')

    for _, row in sequence.iterrows():
        if player != row['player']:
            player = row['player']
            i+=1
        event_type = row['type']
        timespamp = row['timestamp']
        print(f'{i}: {player} ({event_type}) <{timespamp}>')
        if row['team'] == start_team:
            general_color = 'blue'
        else:
            general_color = 'red'
        if event_type in events_without_location:
            start = (60.0, 40.0)
        else:
            start = (float(row['start_x']*scale), float(row['start_y']*scale))
        if row['end_x'] != '' and row['end_y'] != '':
            end = (float(row['end_x']*scale), float(row['end_y']*scale))
        else:
            end = start
        match row['type']:
            case 'Ball Receipt*':
                plt.plot(start[0], start[1], marker='.', markersize=8*scale, markeredgecolor=general_color, markerfacecolor=general_color)
                plt.plot(start[0], start[1], marker='o', markersize=8*scale, markeredgecolor=general_color, markerfacecolor="black")
            case 'Duel':
                plt.plot(start[0], start[1], marker='v', markersize=8*scale, markeredgecolor=general_color, markerfacecolor=general_color)
            case 'Pass':
                plt.plot([start[0], end[0]], [start[1], end[1]], color=general_color, linewidth=scale)
                plt.plot(start[0], start[1], marker='o', markersize=8*scale, markeredgecolor=general_color, markerfacecolor="black")
            case 'Carry':
                plt.plot([start[0], end[0]], [start[1], end[1]], color='green', linewidth=scale)
            case 'Dispossessed':
                plt.plot(start[0], start[1], marker='s', markersize=8*scale, markeredgecolor=general_color, markerfacecolor=general_color)
            case 'Shot':
                plt.plot([start[0], end[0]], [start[1], end[1]], color='yellow', linewidth=scale)
                plt.plot(start[0], start[1], marker='o', markersize=8*scale, markeredgecolor=general_color, markerfacecolor="black")
            case 'Block':
                plt.plot(start[0], start[1], marker='X', markersize=8*scale, markeredgecolor=general_color, markerfacecolor="maroon")
            case 'Ball Recovery':
                plt.plot(start[0], start[1], marker='D', markersize=7*scale, markeredgecolor=general_color, markerfacecolor="darkgreen")
            case 'Miscontrol':
                plt.plot(start[0], start[1], marker='H', markersize=9*scale, markeredgecolor=general_color, markerfacecolor="coral")
            case 'Interception':
                plt.plot(start[0], start[1], marker='p', markersize=8*scale, markeredgecolor=general_color, markerfacecolor="sienna")
            case 'Dribble':
                plt.plot(start[0], start[1], marker="$D$", markersize=8*scale, markeredgecolor=general_color, markerfacecolor="gold")
            case 'Clearance':
                plt.plot(start[0], start[1], marker='s', markersize=8*scale, markeredgecolor=general_color, markerfacecolor="fuchsia")
            case 'Foul Committed':
                plt.plot(start[0], start[1], marker="$F$", markersize=8*scale, markeredgecolor="orangered", markerfacecolor="orangered")
            case 'Foul Won':
                plt.plot(start[0], start[1], marker="$F$", markersize=8*scale, markeredgecolor="olive", markerfacecolor="olive")
            case _:
                plt.plot(start[0], start[1], marker='1', markersize=8*scale, markeredgecolor=general_color, markerfacecolor="black")
        for location in row['context_locations']:
            plt.plot(location[0], location[1], marker='o', markersize=6*scale, markeredgecolor=general_color, markerfacecolor="pink")
        plt.text(start[0]-(scale/2), start[1]-(scale/2), str(i), color='white', fontsize=4*scale)

    draw_pitch(ax, x_areas, y_areas, scale)
    plt.show()