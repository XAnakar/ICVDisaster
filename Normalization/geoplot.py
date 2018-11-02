from geopy.geocoders import Nominatim  
import gmplot, csv


# Go through all tweets and add locations to 'coordinates' dictionary
coordinates = {'latitude': [], 'longitude': []}  
for index in csv.DictReader(open("formated.csv","r")):  
    try:
        coordinates['latitude'].append(float(index['latitude']))
        coordinates['longitude'].append(float(index['longitude']))
    except:
        pass

# Instantiate and center a GoogleMapPlotter object to show our map
gmap = gmplot.GoogleMapPlotter(30, 0, 3)


# Insert points on the map passing a list of latitudes and longitudes
gmap.heatmap(coordinates['latitude'], coordinates['longitude'], radius=50)

# Save the map to html file
gmap.draw("geoplot.html")  