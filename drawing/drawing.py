from matplotlib import pyplot as plt
from svgpath2mpl import parse_path
import matplotlib.transforms as mtransforms
import xml.etree.ElementTree as etree
import matplotlib as mpl


def custom_scatter(x, y, image, color):
    ### Plots a marker on the image ###
    # TODO - Rotate 180 degrees
    path = None
    with open(f'drawing/icons/{image}') as f:
        path = parse_svg(f)
        marker = parse_path(path)

    t = mpl.markers.MarkerStyle(marker=marker)
    t._transform = t.get_transform().rotate_deg(180)

    plt.scatter(x, y, marker=t, s=1000, c=color)


def parse_svg(file):
    ### Parses the SVG file and returns the path, width and height ###
    tree = etree.parse(file)
    root = tree.getroot()
    path = root.find('.//{http://www.w3.org/2000/svg}path')

    return path.attrib['d']



def draw_pass(start, end):
    plt.arrow(start[0], start[1], end[0] - start[0], end[1] - start[1], color='#3f3f3f', head_width=0.1)


def draw_reception(start):
    plt.scatter(start[0], start[1], color='#081972', marker='o', s=300)


def draw_shot(start, end):
    plt.arrow(start[0], start[1], end[0] - start[0], end[1] - start[1], color='#F7C84B', head_width=0.1)


def draw_carry(start, end):
    plt.plot([start[0], end[0]], [start[1], end[1]], color='#3f3f3f', linestyle='dashed', marker='')


def draw_duel(start):
    custom_scatter(start[0], start[1], color='#3f3f3f', image='swords.svg')


def draw_clearence(start):
    custom_scatter(start[0], start[1], color='#3f3f3f', image='cleat.svg')


def draw_recovery(start):
    custom_scatter(start[0], start[1], color='#f3f3f3', image='refresh.svg')


def draw_dispossessed(start):
    custom_scatter(start[0], start[1], color='#F74B4B', image='cross.svg')


def draw_interception(start):
    custom_scatter(start[0], start[1], color='#F74B4B', image='refresh.svg')


def draw_miscoontroll(start):
    # TODO - Change icon to dashed cross
    custom_scatter(start[0], start[1], color='#F74B4B', image='cross.svg')


def draw_block(start):
    custom_scatter(start[0], start[1], color='#F74B4B', image='shield.svg')


def draw_injury(start):
    custom_scatter(start[0], start[1], color='#F74B4B', image='injury.svg')


def draw_dribble(start):
    custom_scatter(start[0], start[1], color='#F7C84B', image='star.svg')


def draw_half_end(start):
    custom_scatter(start[0], start[1], color='#F7C84B', image='timer.svg')


def draw_foul_committed(start):
    custom_scatter(start[0], start[1], color='#F74B4B', image='cleat.svg')


def draw_foul_won(start):
    custom_scatter(start[0], start[1], color='#4BF75C', image='cleat.svg')