import matplotlib as mpl
from svgpathtools import svg2paths
from svgpath2mpl import parse_path
import os

# logos 
filepath = os.path.abspath(os.getcwd()) + "/logos/"

logos = {'ANA': filepath+"Anaheim_Ducks.png",
         'ARI': filepath+"Arizona_Coyotes_logo_(2021).png",
         'BOS': filepath+"Boston_Bruins.png",
         'BUF': filepath+"Buffalo_Sabres_Logo.png",
         'CGY': filepath+"Calgary_Flames_logo.png",
         'CAR': filepath+"Carolina_Hurricanes.png",
         'CHI': filepath+"Chicago_Blackhawks_logo.png",
         'COL': filepath+"Colorado_Avalanche_logo.png",
         'CBJ': filepath+"Columbus_Blue_Jackets_logo.png",
         'DAL': filepath+"Dallas_Stars_logo_(2013).png", 
         'DET': filepath+"Detroit_Red_Wings_logo.png", 
         'EDM': filepath+"Logo_Edmonton_Oilers.png", 
         'FLA': filepath+"Florida_Panthers_2016_logo.png",
         'L.A': filepath+"Los_Angeles_Kings_logo.png",
         'MIN': filepath+"Minnesota_Wild.png", 
         'MTL': filepath+"Montreal_Canadiens.png", 
         'N.J': filepath+"New_Jersey_Devils_logo.png", 
         'NSH': filepath+"Nashville_Predators_Logo_(2011).png", 
         'NYI': filepath+"Logo_New_York_Islanders.png", 
         'NYR': filepath+"New_York_Rangers.png", 
         'OTT': filepath+"Ottawa_Senators_2020-2021_logo.png", 
         'PHI': filepath+"Philadelphia_Flyers.png", 
         'PIT': filepath+"Pittsburgh_Penguins_logo_(2016).png", 
         'S.J': filepath+"SanJoseSharksLogo.png", 
         'SEA': filepath+"Seattle_Kraken_official_logo.png", 
         'STL': filepath+"St._Louis_Blues_logo.png", 
         'T.B': filepath+"Tampa_Bay_Lightning_2011.png", 
         'TOR': filepath+"Toronto_Maple_Leafs_2016_logo.png", 
         'VAN': filepath+"Vancouver_Canucks_logo.png", 
         'VGK': filepath+"Vegas_Golden_Knights_logo.png", 
         'WPG': filepath+"Winnipeg_Jets_Logo_2011.png", 
         'WSH': filepath+"Washington_Capitals.png"}

def get_logos(team: str):
    logo_file = logos[team]
    # path, attributes = svg2paths(logo_file)
    # team_marker = parse_path(attributes[0]['d'])
    # team_marker.vertices -= team_marker.vertices.mean(axis=0)
    # team_marker = team_marker.transformed(mpl.transforms.Affine2D().rotate_deg(180))
    # team_marker = team_marker.transformed(mpl.transforms.Affine2D().scale(-1,1))
    return(logo_file)