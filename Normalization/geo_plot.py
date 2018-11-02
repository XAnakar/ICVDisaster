from geopy.geocoders import Nominatim  
import gmplot, csv

coordinates = {'latitude': [], 'longitude': []}  
for index in csv.DictReader(open("formated.csv","r")):  
    try:
        coordinates['latitude'].append(float(index['latitude']))
        coordinates['longitude'].append(float(index['longitude']))
    except:
        pass

gmap = gmplot.GoogleMapPlotter(30, 0, 3)
gmap.heatmap(coordinates['latitude'], coordinates['longitude'], radius=50)
gmap.draw("geoplot.html")  
