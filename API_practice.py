#%%
# Use the citipy module to determine city based on latitude and longitude.

# Import the dependencies.
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# import csv
import csv

from citipy import citipy
#%%

# Import the requests library.
import requests

# Import the API key.
from config import weather_api_key

#%%
# Create a practice set of random latitude and longitude combinations.
x = [25.12903645, 25.92017388, 26.62509167, -59.98969384, 37.30571269]
y = [-67.59741259, 11.09532135, 74.84233102, -76.89176677, -61.13376282]
coordinates = zip(x, y)


#%%

# Use the tuple() function to display the latitude and longitude combinations.
for coordinate in coordinates:
    print(citipy.nearest_city(coordinate[0], coordinate[1]).city_name,
          citipy.nearest_city(coordinate[0], coordinate[1]).country_code)

# %%
# Add the latitudes and longitudes to a list.
coordinates = list(lat_lngs)

# %%
coordinates

# %%
# Starting URL for Weather Map API Call.
url = "http://api.openweathermap.org/data/2.5/weather?units=Imperial&APPID=" + weather_api_key
print(url)

# %%
# Create an endpoint URL for a city.
city_url = url + "&q=" + "Boston"
print(city_url)

# %%
# Make a 'Get' request for the city weather.
city_weather = requests.get(city_url)
city_weather

# %%
# Create an endpoint URL for a city.
city_url = url + "&q=" + "Bston"
city_weather = requests.get(city_url)
city_weather

# %%
# Create an endpoint URL for a city.
city_url = url + "&q=" + "Boston"
city_weather = requests.get(city_url)
city_weather

# %%
# Get the text of the 'Get' request.
city_weather.text

# %%
# Get the JSON text of the 'Get' request.
city_weather.json()

# %%
# Create an endpoint URL for a city.
city_url = url + "&q=" + "Boston"
city_weather = requests.get(city_url)
if city_weather.status_code == 200:
    print(f"City Weather found.")
else:
    print(f"City weather not found.")


# %%
# Create an endpoint URL for a city.
city_url = url + "&q=" + "Bston"
city_weather = requests.get(city_url)
if city_weather.json():
    print(f"City Weather found.")
else:
    print(f"City weather not found.")

# %%
print(city_url)

# %%
# Create an endpoint URL for a city.
city_url = url + "&q=" + "Boston"
city_weather = requests.get(city_url)
city_weather.json()

# %%
# Get the JSON data.
boston_data = city_weather.json()

# %%
boston_data["sys"]["country"]

# %%
# Import the datetime module from the datetime library.
from datetime import datetime
# Get the date from the JSON file.
date = boston_data["dt"]
# Convert the UTC date to a date format with year, month, day, hours, minutes, and seconds.
datetime.utcfromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S')

