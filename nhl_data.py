import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib.ticker as mtick
import os 
from logos import get_logos
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image 
import sys

# nhl data 
nhl_edge_data = pd.read_csv(os.path.abspath(os.getcwd())+r"/NHL-Edge-Data-Teams-21-23.csv", header = [0, 1])
seasons_nhl_edge = nhl_edge_data.groupby(nhl_edge_data["Season", "Season"]) # group by seasons

# strip all % from data with %
for x_val, y_val in nhl_edge_data:
    if '%' in y_val:
        for i in range(len(nhl_edge_data[x_val, y_val])):
            nhl_edge_data.loc[:, (x_val, y_val)].values[i] = (float)(nhl_edge_data.loc[:, (x_val, y_val)].values[i][:-1])

# plot images as markers 
def plot_images(x, y, teams, ax=None):
    ax = ax or plt.gca()

    for xi, yi, zi in zip(x, y, teams):
        path = get_logos(zi)
        image = Image.open(path)
        image.thumbnail((60, 60), Image.Resampling.LANCZOS)
        im = OffsetImage(image, zoom=72/ax.figure.dpi)
        im.image.axes = ax

        ab = AnnotationBbox(im, (xi,yi), frameon=False, pad=0.0,)

        ax.add_artist(ab)

def graph_nhl(season:str, category1:str, subcategory1:str, category2:str, subcategory2:str):
    fig1, ax1 = plt.subplots(1, 1)
    ax1.grid()
    if '%' in subcategory2:
        fmt = '%.1f%%'
        yticks = mtick.FormatStrFormatter(fmt)
        ax1.yaxis.set_major_formatter(yticks)
    ax1.set_title(season + " " + category1 + ": " + subcategory1 + " vs. " + category2 + ": " + subcategory2)
    ax1.set_xlabel(category1+": "+subcategory1)
    ax1.set_ylabel(category2+": "+subcategory2)
    season_group = seasons_nhl_edge.get_group(season)
    ax1.plot(season_group[category1, subcategory1], season_group[category2, subcategory2], linestyle="None")
    plot_images(season_group[category1, subcategory1], season_group[category2, subcategory2], season_group['Abbreviation', 'Abbreviation'], ax=ax1)

# graph_nhl("21-22", "Skating Speed", "22+", "Distance (above average)", "ES")

# plt.show()

# sys.exit(0)