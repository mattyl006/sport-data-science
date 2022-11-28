from mplsoccer.pitch import Pitch
import matplotlib.pyplot as plt

def draw_heatmap(location_xy, title, x_areas=12, y_areas=8):
    #plot vertical pitch
    pitch = Pitch(line_zorder=2, line_color='black')
    fig, ax = pitch.grid(grid_height=0.9, title_height=0.06, axis=False,
                        endnote_height=0.04, title_space=0, endnote_space=0)
    #get the 2D histogram
    bin_statistic = pitch.bin_statistic(location_xy.x, location_xy.y, statistic='count', bins=(x_areas, y_areas), normalize=False)
    #normalize by number of games
    bin_statistic["statistic"] = bin_statistic["statistic"]
    #make a heatmap
    pcm  = pitch.heatmap(bin_statistic, cmap='Reds', edgecolor='grey', ax=ax['pitch'])
    #legend to our plot
    ax_cbar = fig.add_axes((1, 0.093, 0.03, 0.786))
    cbar = plt.colorbar(pcm, cax=ax_cbar)
    fig.suptitle(title, fontsize = 30)
    plt.show()