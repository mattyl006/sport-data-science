from mplsoccer.pitch import Pitch
import matplotlib.pyplot as plt

class Draw:
    def __init__(self, pitch_size_x=120, pitch_size_y=80, x_areas=12, y_areas=8, scale=1, corner=False):
        letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T']
        self.pitch_size_x = pitch_size_x
        self.pitch_size_y = pitch_size_y
        self.x_areas = x_areas
        self.y_areas = y_areas
        self.X = letters[:self.x_areas]
        self.Y = [i+1 for i in range(self.y_areas)]
        self.scale = scale
        self.corner = corner
        self.events_without_location = {'Injury Stoppage', 'Half End'}

        if self.x_areas < 2:
            self.x_areas = 2
        if self.y_areas < 2:
            self.y_areas = 2
        if self.scale < 1:
            self.scale = 1

    def draw_pitch_outline_centreline(self):
        color = "black"
        plt.plot([0, 0],[0, self.pitch_size_y*self.scale], color=color)
        plt.plot([0, self.pitch_size_x*self.scale], [self.pitch_size_y*self.scale, self.pitch_size_y*self.scale], color=color)
        plt.plot([self.pitch_size_x*self.scale, self.pitch_size_x*self.scale],[self.pitch_size_y*self.scale, 0], color=color)
        plt.plot([self.pitch_size_x*self.scale, 0],[0, 0], color=color)
        plt.plot([(self.pitch_size_x/2)*self.scale, (self.pitch_size_x/2)*self.scale],[0, self.pitch_size_y*self.scale], color=color)

    def draw_grid_text(self, corner=False):
        if not corner:
            y = 82*self.scale
            for i in range (0, self.x_areas):
                x = ((((self.pitch_size_x/2) / self.x_areas) + i * self.pitch_size_x / self.x_areas) -1) * self.scale
                text = str(self.X[i])
                size = 8*self.scale  
                plt.text(x, y, text, fontsize=size)
            x = -3*self.scale
            for i in range (0, self.y_areas):
                y = (self.pitch_size_y - 5.5 - (i * 10)) * self.scale
                text = str(self.Y[i])
                size = 8*self.scale
                plt.text(x, y, text, fontsize=size)
        else:
            def generate_corner_text(x, y, text):
                size = 8*self.scale
                plt.text((x-1)*self.scale, (y-1)*self.scale, text, fontsize=size)
            generate_corner_text(102, 8, "RZ")
            generate_corner_text(102, 72, "LZ")
            generate_corner_text(93, 23, "RO")
            generate_corner_text(93, 57, "LO")
            generate_corner_text(93, 40, "CO")
            generate_corner_text(111, 23, "RP")
            generate_corner_text(111, 57, "LP")
            generate_corner_text(111, 40, "CP")        

    def draw_left_penalty_area(self):
        color = "black"
        plt.plot([18*self.scale,18*self.scale],[62*self.scale,18*self.scale],color=color)
        plt.plot([0,18*self.scale],[62*self.scale,62*self.scale],color=color)
        plt.plot([0,18*self.scale],[18*self.scale,18*self.scale],color=color)

    def draw_right_penalty_area(self):
        color = "black"
        plt.plot([self.pitch_size_x*self.scale,102*self.scale],[62*self.scale,62*self.scale],color=color)
        plt.plot([102*self.scale,102*self.scale],[62*self.scale,18*self.scale],color=color)
        plt.plot([self.pitch_size_x*self.scale, 102*self.scale],[18*self.scale,18*self.scale],color=color)

    def draw_left_six_yard_box(self):
        color = "black"
        plt.plot([0,6*self.scale],[48*self.scale,48*self.scale],color=color)
        plt.plot([6*self.scale,6*self.scale],[48*self.scale,32*self.scale],color=color)
        plt.plot([0,6*self.scale],[32*self.scale,32*self.scale],color=color)

    def draw_right_six_yard_box(self):
        color = "black"
        plt.plot([self.pitch_size_x*self.scale,114*self.scale],[48*self.scale,48*self.scale],color=color)
        plt.plot([114*self.scale,114*self.scale],[48*self.scale,32*self.scale],color=color)
        plt.plot([self.pitch_size_x*self.scale,114*self.scale],[32*self.scale,32*self.scale],color=color)

    def draw_sectors(self, corner=False):
        color = "gray"
        if not corner:
            x = [self.pitch_size_x*self.scale,0]
            for i in range(1, self.y_areas):
                y = [(self.pitch_size_y/self.y_areas)*i*self.scale,(self.pitch_size_y/self.y_areas)*i*self.scale]
                plt.plot(x, y, color=color)
            y = [self.pitch_size_y*self.scale,0]
            for i in range(1, self.x_areas):
                x = [(self.pitch_size_x/self.x_areas)*i*self.scale,(self.pitch_size_x/self.x_areas)*i*self.scale]
                plt.plot(x, y, color=color)
        else:
            # I
            plt.plot([48*self.scale,0],[80*self.scale,80*self.scale], color="gray")
            plt.plot([48*self.scale,48*self.scale],[80*self.scale,0], color="gray")
            plt.plot([48*self.scale,0],[0,0], color="gray")
            plt.plot([0,0],[0,80*self.scale], color="gray")

            # II
            plt.plot([84*self.scale,48*self.scale],[80*self.scale,80*self.scale], color="gray")
            plt.plot([84*self.scale,84*self.scale],[80*self.scale,0], color="gray")
            plt.plot([84*self.scale,48*self.scale],[0,0], color="gray")
            plt.plot([48*self.scale,48*self.scale],[0,80*self.scale], color="gray")

            # LZ
            plt.plot([120*self.scale,84*self.scale],[16*self.scale,16*self.scale], color="gray")
            plt.plot([120*self.scale,120*self.scale],[16*self.scale,0], color="gray")
            plt.plot([84*self.scale,84*self.scale],[16*self.scale,0], color="gray")
            plt.plot([84*self.scale,120*self.scale],[16*self.scale,16*self.scale], color="gray")

            # RZ
            plt.plot([120*self.scale,84*self.scale],[64*self.scale,64*self.scale], color="gray")
            plt.plot([120*self.scale,120*self.scale],[80*self.scale,64*self.scale], color="gray")
            plt.plot([84*self.scale,84*self.scale],[80*self.scale,64*self.scale], color="gray")
            plt.plot([84*self.scale,120*self.scale],[80*self.scale,80*self.scale], color="gray")

            # LO
            plt.plot([102*self.scale,84*self.scale],[30*self.scale,30*self.scale], color="gray")
            plt.plot([102*self.scale,102*self.scale],[30*self.scale,16*self.scale], color="gray")
            plt.plot([84*self.scale,84*self.scale],[30*self.scale,16*self.scale], color="gray")
            plt.plot([84*self.scale,102*self.scale],[16*self.scale,16*self.scale], color="gray")

            # CO
            plt.plot([102*self.scale,84*self.scale],[50*self.scale,50*self.scale], color="gray")
            plt.plot([102*self.scale,102*self.scale],[50*self.scale,30*self.scale], color="gray")
            plt.plot([84*self.scale,84*self.scale],[50*self.scale,30*self.scale], color="gray")
            plt.plot([84*self.scale,102*self.scale],[30*self.scale,30*self.scale], color="gray")

            # RO
            # plt.plot([102*self.scale,84*self.scale],[64*self.scale,64*self.scale], color="gray")
            # plt.plot([102*self.scale,102*self.scale],[80*self.scale,64*self.scale], color="gray")
            # plt.plot([84*self.scale,84*self.scale],[80*self.scale,64*self.scale], color="gray")
            # plt.plot([84*self.scale,102*self.scale],[80*self.scale,80*self.scale], color="gray")

            # LP
            plt.plot([120*self.scale,102*self.scale],[30*self.scale,30*self.scale], color="gray")
            plt.plot([120*self.scale,120*self.scale],[30*self.scale,16*self.scale], color="gray")
            plt.plot([102*self.scale,102*self.scale],[30*self.scale,16*self.scale], color="gray")
            plt.plot([102*self.scale,120*self.scale],[16*self.scale,16*self.scale], color="gray")

            # RP
            plt.plot([120*self.scale,102*self.scale],[64*self.scale,64*self.scale], color="gray")
            plt.plot([120*self.scale,120*self.scale],[64*self.scale,50*self.scale], color="gray")
            plt.plot([102*self.scale,102*self.scale],[64*self.scale,50*self.scale], color="gray")
            plt.plot([102*self.scale,120*self.scale],[64*self.scale,64*self.scale], color="gray")

            # CP
            plt.plot([120*self.scale,102*self.scale],[50*self.scale,50*self.scale], color="gray")
            plt.plot([120*self.scale,120*self.scale],[50*self.scale,30*self.scale], color="gray")
            plt.plot([102*self.scale,102*self.scale],[50*self.scale,30*self.scale], color="gray")
            plt.plot([102*self.scale,120*self.scale],[30*self.scale,30*self.scale], color="gray")

    def draw_circles(self):
        color = "black"
        centreCircle = plt.Circle((60*self.scale,40*self.scale),12*self.scale,color=color,fill=False)  # type: ignore
        centreSpot = plt.Circle((60*self.scale,40*self.scale),0.71,color=color) # type: ignore
        leftPenSpot = plt.Circle((12*self.scale,40*self.scale),0.71,color=color) # type: ignore
        rightPenSpot = plt.Circle((108*self.scale,40*self.scale),0.71,color=color) # type: ignore
        self.ax.add_patch(centreCircle)
        self.ax.add_patch(centreSpot)
        self.ax.add_patch(leftPenSpot)
        self.ax.add_patch(rightPenSpot)

    def draw_pitch(self, corner=False):
        self.draw_sectors(corner)
        self.draw_pitch_outline_centreline()
        self.draw_grid_text(corner)
        self.draw_left_penalty_area()
        self.draw_right_penalty_area()
        self.draw_left_six_yard_box()
        self.draw_right_six_yard_box()
        self.draw_circles()

    def draw_sequence(self, sequence, start_team, first_event_360=False, scores=[], scores_locations=[], counterattack_pass_id=None, pdf=False, image_name=None, sb360=True, corner=False):
        self.fig, self.ax = plt.subplots()
        self.fig.set_size_inches(7*self.scale, 5*self.scale)
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
            try:
                print(f'SCORE: {row["score"]}')
            except:
                pass
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
                # swap perspective if corner and not start team
                if corner and row['team']!= start_team:
                    row['start_x'] = 120.0 - float(row['start_x'])
                    row['start_y'] = 80.0 - float(row['start_y'])
                start = (float(row['start_x']*self.scale), float(row['start_y']*self.scale))
            if row['end_x'] != '' and row['end_y'] != '':
                # swap perspective if corner and not start team
                if corner and row['team']!= start_team:
                    row['end_x'] = 120.0 - float(row['end_x'])
                    row['end_y'] = 80.0 - float(row['end_y'])
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
        if sb360:
            if not first_event_360: #reverse sequence
                sequence = sequence[::-1]
            context_drown = False
            for _, row in sequence.iterrows():
                for location, teammate, actor in zip(row['context_locations'], row['teammate_locations'], row['actor_locations']):
                    if len(location) > 0 and location != '': #and True in row['actor_locations']
                        # swap perspective if corner and not start team
                        if corner and row['team']!= start_team:
                            location[0] = 120.0 - float(location[0])
                            location[1] = 80.0 - float(location[1])
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
        self.draw_pitch(corner)
        if image_name:
            plt.savefig(image_name)
        if not pdf:
            plt.show()

    def draw_heatmap(self, location_xy, title):
        pitch = Pitch(line_zorder=2, line_color='black')
        fig, ax = pitch.grid(grid_height=0.9, title_height=0.06, axis=False,
                            endnote_height=0.04, title_space=0, endnote_space=0)
        bin_statistic = pitch.bin_statistic(location_xy.x, location_xy.y, statistic='count', bins=(self.x_areas, self.y_areas), normalize=False)
        bin_statistic["statistic"] = bin_statistic["statistic"]
        pcm  = pitch.heatmap(bin_statistic, cmap='Reds', edgecolor='grey', ax=ax['pitch'])
        ax_cbar = fig.add_axes((1, 0.093, 0.03, 0.786))
        cbar = plt.colorbar(pcm, cax=ax_cbar)
        fig.suptitle(title, fontsize = 30)
        plt.show()
