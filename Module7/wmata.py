'''
This script will query the WMATA API to obtain information about all stations
with accessibility outages and print the number of stations experiencing outages
as well as the name of each station. It will then build a geoJSON using the
location information from these stations and query the MapBox API to generate a
static map with markers for up to 20 of these locations and save it to 'map.png'.
'''

import json
import requests

from geojson import Point
from urllib.parse import urlencode, quote

# API endpoint URL's and access keys
WMATA_API_KEY = "4342052a2667460e809f6306e9ab539a"
MAPBOX_API_KEY = "pk.eyJ1IjoibW1ja2llMiIsImEiOiJjbWdoZnJuNjAwZ3BoMmxvZGZtMnQwOT\
dqIn0.9BxX0pInI_RUhykvVcvhrQ" # Default public MapBox token

INCIDENTS_URL = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"
STATION_URL = "https://api.wmata.com/Rail.svc/json/jStationInfo"
MAPBOX_URL = "https://api.mapbox.com/styles/v1/mapbox/streets-v12/static"
headers = {"api_key": WMATA_API_KEY, 'Accept': '*/*'}

# MapBox URL parameters
CENTER_POINT = "-77.054,38.942"
ZOOM_LEVEL = "9"
DIMENSIONS = "500x500"
MAPBOX_URL_PARAMS = f"{CENTER_POINT},{ZOOM_LEVEL}/{DIMENSIONS}"

################################################################################

# Query the WMATA 'ElevatorIncidents' API to get a list of outages
def get_station_incidents():
  # Use 'requests' to retrieve escalator/elevator incident information
  response = requests.get(INCIDENTS_URL, params = {'api_key': WMATA_API_KEY})
  response = response.json()
  all_incidents = response['ElevatorIncidents']

  # Parse the JSON response of all incidents and create a set containing the
  # station codes
  outage_station_codes = set()
  for incident in all_incidents:
    station_code = incident['StationCode']
    outage_station_codes.add(station_code)

  # Return the set of station codes
  return outage_station_codes


# Query the WMATA 'Stations' API to get location coordinates (lat/lon)
def get_station_info(station_code: str):
  # Use 'requests' to retrive station information by station code
  response = requests.get(STATION_URL, params = {'api_key': WMATA_API_KEY, \
                                                 'StationCode': station_code})
  
  # Return the response as JSON and print the name of the station
  response = response.json()
  print(response['Name'])

  # Create tuple of (lon, lat) and return it
  longitude = response['Lon']
  latitude = response['Lat']
  return (longitude, latitude)


# Convert list lon/lat pairs (tuples) to URL-encoded GeoJSON object
def encode_geojson(incident_locations):
  feature_collection = {"type":"FeatureCollection","features":[]}

  # Build out FeatureCollection to contain a list of "features"
  # Each "feature" contains a GeoJSON object that will be plotted as a map marker
  for location in incident_locations:
    feature = {"type":"Feature","properties": 
                {"marker-color":"#462eff",
                 "marker-size":"small",
                 "marker-symbol":"caution"},
                "geometry": Point(location)}
    feature_collection["features"].append(feature)

  # Return URL-encoded (quoted) GeoJSON object
  return quote(json.dumps(feature_collection))


# Retrieve static map image with GeoJSON multiple marker overlay
def get_static_map(encoded_geo_json):
  # MapBox static map URL for 500x500 image centered at (-77.054,38.942) lon/lat
  static_map_url = f"{MAPBOX_URL}/geojson({encoded_geo_json})/{MAPBOX_URL_PARAMS}?access_token={MAPBOX_API_KEY}"
  
  # Use 'requests' and the static_map_url to retrieve the map image
  static_map = requests.get(static_map_url)
  
  # If the status code is 200, write the raw bytes (binary data) in the response
  # to a new file called map.png
  # Else print "Error returned from MapBox API"
  if static_map.status_code == 200:
    with open('map.png', 'wb') as f:
      f.write(static_map.content)
  else:
    print('Error returned from MapBox API')


def main():
  # Get a set of unique station codes experiencing outages
  station_codes = get_station_incidents()
  
  # Print the total number of stations with outages
  num_outages = len(station_codes)
  print(f'{num_outages} stations are currently experiencing accessibility outages.')
  
  # Print the name of each station with an outage
  # Build a list of lon/lat pairs (tuples) of the locations of the first 20
  # stations with an outage
  station_coords = []
  for station in station_codes:
    lon_lat = get_station_info(station)
    if len(station_coords) < 20:
      station_coords.append(lon_lat)

  # Convert the list of lon/lat pairs to a URL-encoded GeoJSON blob
  geojson_blob = encode_geojson(station_coords)
  
  # Retrieve and download the static map image
  get_static_map(geojson_blob)  


if __name__ == "__main__":
  main()
