import os

# logos 
filepath = os.path.abspath(os.getcwd()) + "/logos/"

logos = {'ANA': filepath+"Anaheim_Ducks.svg",
         'ARI': filepath+"Arizona_Coyotes_logo_(2021).svg",
         'BOS': filepath+"Boston_Bruins.svg",
         'BUF': filepath+"Buffalo_Sabres_Logo.svg",
         'CGY': filepath+"Calgary_Flames_logo.svg",
         'CAR': filepath+"Carolina_Hurricanes.svg",
         'CHI': filepath+"Chicago_Blackhawks_logo.svg",
         'COL': filepath+"Colorado_Avalanche_logo.svg",
         'CBJ': filepath+"Columbus_Blue_Jackets_logo.svg",
         'DAL': filepath+"Dallas_Stars_logo_(2013).svg", 
         'DET': filepath+"Detroit_Red_Wings_logo.svg", 
         'EDM': filepath+"Logo_Edmonton_Oilers.svg", 
         'FLA': filepath+"Florida_Panthers_2016_logo.svg",
         'L.A': filepath+"Los_Angeles_Kings_logo.svg",
         'MIN': filepath+"Minnesota_Wild.svg", 
         'MTL': filepath+"Montreal_Canadiens.svg", 
         'N.J': filepath+"New_Jersey_Devils_logo.svg", 
         'NSH': filepath+"Nashville_Predators_Logo_(2011).svg", 
         'NYI': filepath+"Logo_New_York_Islanders.svg", 
         'NYR': filepath+"New_York_Rangers.svg", 
         'OTT': filepath+"Ottawa_Senators_2020-2021_logo.svg", 
         'PHI': filepath+"Philadelphia_Flyers.svg", 
         'PIT': filepath+"Pittsburgh_Penguins_logo_(2016).svg", 
         'S.J': filepath+"SanJoseSharksLogo.svg", 
         'SEA': filepath+"Seattle_Kraken_official_logo.svg", 
         'STL': filepath+"St._Louis_Blues_logo.svg", 
         'T.B': filepath+"Tampa_Bay_Lightning_2011.svg", 
         'TOR': filepath+"Toronto_Maple_Leafs_2016_logo.svg", 
         'VAN': filepath+"Vancouver_Canucks_logo.svg", 
         'VGK': filepath+"Vegas_Golden_Knights_logo.svg", 
         'WPG': filepath+"Winnipeg_Jets_Logo_2011.svg", 
         'WSH': filepath+"Washington_Capitals.svg"}

def get_logos(team: str):
    logo_file = logos[team]