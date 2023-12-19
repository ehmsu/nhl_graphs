import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib.ticker as mtick
import os 

fig1, ax1 = plt.subplots(1, 1)

filepath = os.path.abspath(os.getcwd()) + "/logos/"
print(filepath)

# nhl data 
nhl_edge_data = pd.read_csv(os.path.abspath(os.getcwd())+r"/NHL-Edge-Data-Teams-21-23.csv", header = [0, 1])
seasons_nhl_edge = nhl_edge_data.groupby(nhl_edge_data["Season", "Season"]) # group by seasons

# convert Zone Time OZ% to OZ as a float 
for i in range(len(nhl_edge_data["Zone Time", "OZ%"])):
    nhl_edge_data["Zone Time", "OZ%"][i] = (float)(nhl_edge_data.loc[:, ("Zone Time", "OZ%")][i][:-1])
# convert Zone Time PPOZ to PPOZ as a float 
for i in range(len(nhl_edge_data["Zone Time", "PPOZ"])):
    nhl_edge_data["Zone Time", "PPOZ"][i] = (float)(nhl_edge_data.loc[:, ("Zone Time", "PPOZ")][i][:-1])

print(nhl_edge_data["Zone Time", "OZ%"])
# print(nhl_data["Zone Time", "OZ%"])
# nhl_data.replace(to_replace=nhl_data["Zone Time", "OZ%"], value=new_oz)

# 21-22 Season (Regular)
reg_season_21_22 = seasons_nhl_edge.get_group("21-22")

# 21-22 Season (Playoffs)
playoff_season_21_22 = seasons_nhl_edge.get_group("21-22p")

# 22-23 Season (Regular)
reg_season_22_23 = seasons_nhl_edge.get_group("22-23")

# 22-23 Season (Playoffs)
playoff_season_22_23 = seasons_nhl_edge.get_group("22-23p")

# Zone time comparison 

# print(reg_season_21_22["Zone Time", "OZ%"])
fmt = '%.1f%%'
yticks = mtick.FormatStrFormatter(fmt)
ax1.yaxis.set_major_formatter(yticks)
ax1.set_title("Time spent in OZ of PP")
ax1.scatter(reg_season_21_22["Abbreviation", "Abbreviation"], reg_season_21_22["Zone Time", "PPOZ"], label="Regular Season 2021-2022")
ax1.scatter(reg_season_22_23["Abbreviation", "Abbreviation"], reg_season_22_23["Zone Time", "PPOZ"], label="Regular Season 2022-2023")
ax1.set_xlabel("Teams")
ax1.set_ylabel("% PPOZ Time")
ax1.legend()

plt.show()

# print(nhl_data["Team"])