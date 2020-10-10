import pandas as pd
import geopandas as gpd

# ========================= Data Prep =========================
# Pre-processed shapefile data and corresponding state information combined
merged_dict_df = pd.read_csv('nws_shapefile_translated.csv')

# data courtesy of https://mappingpoliceviolence.org/
mvp_raw = pd.read_csv("2013-2019 Police Killings_june05.csv")
mvp_raw = mvp_raw.rename(columns={'State':'STATE'})

# merge the recorded deaths dataset with the pre-processed shapefile data
kepler_mvp_df = pd.merge(MVP_raw,merged_dict_df, on=['STATE','County'])

kepler_mvp_df = kepler_mvp_df.dropna(subset=["Victim's name"])
kepler_mvp_df = kepler_mvp_df.rename(columns={'Date of Incident (month/day/year)':'datetime'})
kepler_mvp_df = kepler_mvp_df.sort_values(by="datetime")

kepler_mvp_df[‘datetime’] = kepler_mvp_df[‘datetime’].astype(str) + ‘ 0:00’


# ========================= Map Generation =========================
from keplergl import KeplerGl
mvp_map = KeplerGl(height=1000, data={'police actions that resulted in death': kepler_mvp_df})

# modify the map settings as you desire until you have your final map.

# This saves our current map configuration as current_config
current_config = mvp_map.config

#Thats it! Kepler.gl makes it really easy to build complex detailed 3D maps.
