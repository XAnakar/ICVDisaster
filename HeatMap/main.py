import folium
from folium import plugins
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os



hawaii = pd.read_csv('RESULT.csv')
divvyStations = pd.concat([hawaii], axis=0).drop_duplicates(subset=['id_str'])

m = folium.Map([19.433409, -155.287767], zoom_start=7)
stationArr = divvyStations[['latitude', 'longitude']].as_matrix()

m.add_child(plugins.HeatMap(stationArr, radius=15))
m.save(os.path.join('heatmap.html'))