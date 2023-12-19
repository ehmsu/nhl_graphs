import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib.ticker as mtick
import os 
from logos import get_logos
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image 

# nhl data 
nhl_edge_data = pd.read_csv(os.path.abspath(os.getcwd())+r"/NHL-Edge-Data-Teams-21-23.csv", header = [0, 1])
seasons_nhl_edge = nhl_edge_data.groupby(nhl_edge_data["Season", "Season"]) # group by seasons

# convert Zone Time OZ% to OZ as a float 
for i in range(len(nhl_edge_data["Zone Time", "OZ%"])):
    nhl_edge_data.loc[:, ("Zone Time", "OZ%")].values[i] = (float)(nhl_edge_data.loc[:, ("Zone Time", "OZ%")].values[i][:-1])
# convert Zone Time PPOZ to PPOZ as a float 
for i in range(len(nhl_edge_data["Zone Time", "PPOZ"])):
    nhl_edge_data.loc[:, ("Zone Time", "PPOZ")].values[i] = (float)(nhl_edge_data.loc[:, ("Zone Time", "PPOZ")].values[i][:-1])

# plot images 
def plot_images(x, y, ax=None):
    ax = ax or plt.gca()

    for xi, yi in zip(x,y):
        path = get_logos(xi)
        image = Image.open(path)
        image.thumbnail((50, 50), Image.Resampling.LANCZOS)
        im = OffsetImage(image, zoom=72/ax.figure.dpi)
        im.image.axes = ax

        ab = AnnotationBbox(im, (xi,yi), frameon=False, pad=0.0,)

        ax.add_artist(ab)

percentages = ["PPOZ", "OZ%"]

def graph_nhl(season:str, category:str, subcategory:str):
    fig1, ax1 = plt.subplots(1, 1)
    if subcategory in percentages:
        fmt = '%.1f%%'
        yticks = mtick.FormatStrFormatter(fmt)
        ax1.yaxis.set_major_formatter(yticks)
    ax1.set_title(season + " " + category + ": " + subcategory)
    ax1.set_xticks([]) # remove x ticks
    ax1.set_ylabel(category+": "+subcategory)
    season_group = seasons_nhl_edge.get_group(season)
    ax1.plot(season_group["Abbreviation", "Abbreviation"], season_group[category, subcategory], linestyle="None")
    plot_images(season_group["Abbreviation", "Abbreviation"], season_group[category, subcategory], ax=ax1)

graph_nhl("21-22", "Skating Speed", "22+")

plt.show()