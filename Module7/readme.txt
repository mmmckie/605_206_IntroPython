Name: Max McKie (mmckie2)

Module Info: Module 7 Assignment: WMATA Accessibility due on 10/12/2025 at 11:59 PM EST

Approach: 

wmata.py - At the start of this script there are a few necessary imports and 
variable assignments for the API keys and endpoints for WMATA and MapBox in order
to later retrieve the stations where there are elevator/escalator outages and
generate a static map using their coordinates. There are also some defined
parameters to define the coordinates, zoom level, and size of the map that will
be generated. Next, the function get_station_incidents() is defined to query the
WMATA ElevatorIncidents endpoint and retrieve a payload of all accessibility
outages. This payload is then turned into a json and an empty set called
'outage_station_codes' is created to store these station codes. A for loop
iterates through all outage incidents in the json and adds all station codes to
the set. This function then returns the set 'outage_station_codes'. Another
function 'get_station_info()' is defined to accept a single station code as a
string to then query the WMATA Stations API endpoint and retrieve info about that
station. This response is then turned into a json and the name of the station is
printed to the console. The longitude and latitude of the station are retrieved
from this json and a tuple of (longitude, latitude) is returned. The next
function 'encode_geojson()' is defined to accept a list of (longitude, latitude)
pairs and convert this into a GeoJSON object for the MapBox API to use for
generating a static map. A fourth function, 'get_static_map()' is then defined to
accept this GeoJSON, query the MapBox API with this info as a parameter, and
retrieve the binary data of this static map. If the status code of this API call
is 200/successful, then the binary data of the map will be saved to a file called
'map.png'. If the status code is anything other than 200, a print statement will
tell the user that there was an error in querying the MapBox API. Finally, there
is a main() function that: (1) obtains a set of all the station codes
experiencing outages by calling 'get_station_incidents()'; (2) prints the number
of stations with outages to the console; (3) creates an empty list called
'station_coords' to store the (lon, lat) coords of all these stations; (4)
iterates through the station codes to obtain these coords and print the station
names to console with successive calls to 'get_station_info()', and adds the
coords to the 'station_coords' list as long as there are less than 20 stations
already stored; (5) converts this list of coords into a GeoJSON blob using
'encode_geojson()'; and (6) retreives and downloads the static map to a file
called 'map.png' using the 'get_static_map()' function. At the end of the script,
the main() function is wrapped in an 'if name main' dunder statement to ensure it
is only executed when the file is run as a script.

Known Bugs:
There are no known bugs.

Citations:
N/A