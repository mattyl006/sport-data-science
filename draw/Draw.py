from mplsoccer.pitch import Pitch
import matplotlib.pyplot as plt

class Draw:
    def __init__(self, pitch_size_x=120, pitch_size_y=80, x_areas=12, y_areas=8, scale=1):
        letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']
        self.pitch_size_x = pitch_size_x
        self.pitch_size_y = pitch_size_y
        self.x_areas = x_areas
        self.y_areas = y_areas
        self.X = letters[:self.x_areas]
        self.Y = [i+1 for i in range(self.y_areas)]
        self.scale = scale

        if self.x_areas < 2:
            self.x_areas = 2
        if self.y_areas < 2:
            self.y_areas = 2
        if self.scale < 1:
            self.scale = 1

        self.events_without_location = {'Injury Stoppage', 'Half End'}
        self.fig, self.ax = plt.subplots()
        self.fig.set_size_inches(7*self.scale, 5*self.scale)

    def draw_pitch_outline_centreline(self, scale):
        plt.plot([0, 0],[0, self.pitch_size_y*scale], color="black")
        plt.plot([0, self.pitch_size_x*scale], [self.pitch_size_y*scale, self.pitch_size_y*scale], color="black")
        plt.plot([self.pitch_size_x*scale, self.pitch_size_x*scale],[self.pitch_size_y*scale, 0], color="black")
        plt.plot([self.pitch_size_x*scale, 0],[0, 0], color="black")
        plt.plot([(self.pitch_size_x/2)*scale, (self.pitch_size_x/2)*scale],[0, self.pitch_size_y*scale], color="black")

    def draw_grid_text(self, scale):
        for i in range (0, self.x_areas):
            x = ((((self.pitch_size_x/2) / self.x_areas) + i * self.pitch_size_x / self.x_areas) -1) * scale
            y = 82*scale
            text = str(self.X[i])
            size = 8*scale  
            plt.text(x, y, text, fontsize=size)
        for i in range (0, self.y_areas):
            x = -3*scale
            y = (self.pitch_size_y - 5.5 - (i * 10)) * scale
            text = str(self.Y[i])
            size = 8*scale
            plt.text(x, y, text, fontsize=size)

    def draw_left_penalty_area(self, scale):
        plt.plot([14.6*scale,14.6*scale],[57.8*scale,22.2*scale],color="black")
        plt.plot([0,14.6*scale],[57.8*scale,57.8*scale],color="black")
        plt.plot([0,14.6*scale],[22.2*scale,22.2*scale],color="black")

    def draw_right_penalty_area(self, scale):
        plt.plot([self.pitch_size_x*scale,105.4*scale],[57.8*scale,57.8*scale],color="black")
        plt.plot([105.4*scale,105.4*scale],[57.8*scale,22.5*scale],color="black")
        plt.plot([self.pitch_size_x*scale, 105.4*scale],[22.5*scale,22.5*scale],color="black")

    def draw_left_six_yard_box(self, scale):
        plt.plot([0,4.9*scale],[48*scale,48*scale],color="black")
        plt.plot([4.9*scale,4.9*scale],[48*scale,32*scale],color="black")
        plt.plot([0,4.9*scale],[32*scale,32*scale],color="black")

    def draw_right_six_yard_box(self, scale):
        plt.plot([self.pitch_size_x*scale,115.1*scale],[48*scale,48*scale],color="black")
        plt.plot([115.1*scale,115.1*scale],[48*scale,32*scale],color="black")
        plt.plot([self.pitch_size_x*scale,115.1*scale],[32*scale,32*scale],color="black")

    def draw_sectors(self, scale):
        color = "gray"
        x = [self.pitch_size_x*scale,0]
        y = [(self.pitch_size_y/self.y_areas)*i*scale,(self.pitch_size_y/self.y_areas)*i*scale]
        for i in range(1, self.y_areas):
            plt.plot(x, y, color=color)
        x = [(self.pitch_size_x/self.x_areas)*i*scale,(self.pitch_size_x/self.x_areas)*i*scale]
        y = [self.pitch_size_y*scale,0]
        for i in range(1, self.x_areas):
            plt.plot(x, y, color=color)

    def draw_circles(self, scale):
        centreCircle = plt.Circle((60*scale,40*scale),8.1*scale,color="black",fill=False)  # type: ignore
        centreSpot = plt.Circle((60*scale,40*scale),0.71,color="black") # type: ignore
        leftPenSpot = plt.Circle((9.7*scale,40*scale),0.71,color="black") # type: ignore
        rightPenSpot = plt.Circle((110.3*scale,40*scale),0.71,color="black") # type: ignore
        self.ax.add_patch(centreCircle)
        self.ax.add_patch(centreSpot)
        self.ax.add_patch(leftPenSpot)
        self.ax.add_patch(rightPenSpot)

    def draw_pitch(self, scale):
        self.draw_pitch_outline_centreline(self, scale)
        self.draw_grid_text(self, scale)
        self.draw_left_penalty_area(self, scale)
        self.draw_right_penalty_area(self, scale)
        self.draw_left_six_yard_box(self, scale)
        self.draw_right_six_yard_box(self, scale)
        self.draw_sectors(self, scale)
        self.draw_circles(self, scale)

    def draw_sequence(self, start_team, sequence, first_event_360=False, counterattack_pass_id=None, pdf=False, image_name=None):
        i = 0
        team = [team for team in sequence['possession_team']][0]
        player = ''
        print(f'Team: {team}')
        if pdf:
            text = f'Team: {team}'
            pdf.cell(0, 4, txt = text, ln = 1, align = 'L')
        for _, row in sequence.iterrows():
            if player != row['player']:
                player = row['player']
                i+=1
            event_type = row['type']
            timespamp = row['timestamp']
            print(f'{i}: {player} ({event_type}) <{timespamp}>')
            if pdf:
                text = f'{i}: {player} ({event_type}) <{timespamp}>'
                pdf.cell(0, 4, txt = text, ln = 1, align = 'L')
            if row['team'] == start_team:
                    general_color = 'blue'
            else:
                general_color = 'red'
            if event_type in self.events_without_location:
                continue
            else:
                start = (float(row['start_x']*self.scale), float(row['start_y']*self.scale))
            if row['end_x'] != '' and row['end_y'] != '':
                end = (float(row['end_x']*self.scale), float(row['end_y']*self.scale))
            else:
                end = start
            match row['type']:
                case 'Ball Receipt*':
                    plt.plot(start[0], start[1], marker='.', markersize=8*self.scale, markeredgecolor=general_color, markerfacecolor=general_color)
                    plt.plot(start[0], start[1], marker='o', markersize=8*self.scale, markeredgecolor=general_color, markerfacecolor="black")
                case 'Duel':
                    plt.plot(start[0], start[1], marker='v', markersize=8*self.scale, markeredgecolor=general_color, markerfacecolor=general_color)
                case 'Pass':
                    if row['id'] == counterattack_pass_id:
                        plt.plot([start[0], end[0]], [start[1], end[1]], color='orange', linewidth=self.scale)
                    else:
                        plt.plot([start[0], end[0]], [start[1], end[1]], color=general_color, linewidth=self.scale)
                    plt.plot(start[0], start[1], marker='o', markersize=8*self.scale, markeredgecolor=general_color, markerfacecolor="black")
                case 'Carry':
                    plt.plot([start[0], end[0]], [start[1], end[1]], color='green', linewidth=self.scale)
                case 'Dispossessed':
                    plt.plot(start[0], start[1], marker='s', markersize=8*self.scale, markeredgecolor=general_color, markerfacecolor=general_color)
                case 'Shot':
                    plt.plot([start[0], end[0]], [start[1], end[1]], color='yellow', linewidth=self.scale)
                    plt.plot(start[0], start[1], marker='o', markersize=8*self.scale, markeredgecolor=general_color, markerfacecolor="black")
                case 'Block':
                    plt.plot(start[0], start[1], marker='X', markersize=8*self.scale, markeredgecolor=general_color, markerfacecolor="maroon")
                case 'Ball Recovery':
                    plt.plot(start[0], start[1], marker='D', markersize=7*self.scale, markeredgecolor=general_color, markerfacecolor="darkgreen")
                case 'Miscontrol':
                    plt.plot(start[0], start[1], marker='H', markersize=9*self.scale, markeredgecolor=general_color, markerfacecolor="coral")
                case 'Interception':
                    plt.plot(start[0], start[1], marker='p', markersize=8*self.scale, markeredgecolor=general_color, markerfacecolor="sienna")
                case 'Dribble':
                    plt.plot(start[0], start[1], marker="$D$", markersize=8*self.scale, markeredgecolor=general_color, markerfacecolor="gold")
                case 'Clearance':
                    plt.plot(start[0], start[1], marker='s', markersize=8*self.scale, markeredgecolor=general_color, markerfacecolor="fuchsia")
                case 'Foul Committed':
                    plt.plot(start[0], start[1], marker="$F$", markersize=8*self.scale, markeredgecolor="orangered", markerfacecolor="orangered")
                case 'Foul Won':
                    plt.plot(start[0], start[1], marker="$F$", markersize=8*self.scale, markeredgecolor="olive", markerfacecolor="olive")
                case _:
                    plt.plot(start[0], start[1], marker='1', markersize=8*self.scale, markeredgecolor=general_color, markerfacecolor="black")
            plt.text(start[0]-(self.scale/2), start[1]-(self.scale/2), str(i), color='white', fontsize=4*self.scale)
        if not first_event_360: #reverse sequence
            sequence = sequence[::-1]
        context_drown = False
        for _, row in sequence.iterrows():
            for location, teammate, actor in zip(row['context_locations'], row['teammate_locations'], row['actor_locations']):
                if len(location) > 0 and location != '': #and True in row['actor_locations']
                    if team != start_team and teammate:
                        team_color = 'red'
                    elif team == start_team and not teammate:
                        team_color = 'red'
                    else:
                        team_color = 'blue'
                    if actor:
                        plt.plot(location[0]*self.scale, location[1]*self.scale, 
                        marker='o', markersize=7*self.scale, markeredgecolor="yellow", markerfacecolor=team_color)
                    else:
                        plt.plot(location[0]*self.scale, location[1]*self.scale, 
                        marker='o', markersize=6*self.scale, markeredgecolor="pink", markerfacecolor=team_color)
                    context_drown = True
            if context_drown:
                ctx_locations_drown = row['context_locations']
                break
        if scores is None:
            scores = []
        if scores_locations is None:
            scores_locations = []
        if len(scores) > 0 and len(scores_locations) > 0:
            for score, loc in zip(scores, scores_locations):
                if scores_locations not in ctx_locations_drown:
                    plt.plot(loc[0]*self.scale, loc[1]*self.scale, 
                    marker='o', markersize=4*self.scale, markeredgecolor='red', markerfacecolor='orange')
                plt.text(loc[0]*self.scale-(4*self.scale), loc[1]*self.scale-(2.5*self.scale), score, color='black', fontsize=5*self.scale)

        self.draw_pitch(self.ax, self.x_areas, self.y_areas, self.scale)
        plt.savefig(image_name)
        if not pdf:
            plt.show()

    def draw_heatmap(self, location_xy, title):
        pitch = Pitch(line_zorder=2, line_color='black')
        fig, self.ax = pitch.grid(grid_height=0.9, title_height=0.06, axis=False,
                            endnote_height=0.04, title_space=0, endnote_space=0)
        bin_statistic = pitch.bin_statistic(location_xy.x, location_xy.y, statistic='count', bins=(self.x_areas, self.y_areas), normalize=False)
        bin_statistic["statistic"] = bin_statistic["statistic"]
        pcm  = pitch.heatmap(bin_statistic, cmap='Reds', edgecolor='grey', ax=ax['pitch'])
        ax_cbar = fig.add_axes((1, 0.093, 0.03, 0.786))
        cbar = plt.colorbar(pcm, cax=ax_cbar)
        fig.suptitle(title, fontsize = 30)
        plt.show()
