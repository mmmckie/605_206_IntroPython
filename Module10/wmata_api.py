'''Enhanced WMATA API.'''

import json
import requests
from flask import Flask

# API endpoint URL's and access keys
WMATA_API_KEY = '4342052a2667460e809f6306e9ab539a'
INCIDENTS_URL = 'https://api.wmata.com/Incidents.svc/json/ElevatorIncidents'
headers = {'api_key': WMATA_API_KEY, 'Accept': '*/*'}

################################################################################

app = Flask(__name__)

# Get incidents by machine type (elevators/escalators)
# Field is called "unit_type" in WMATA API response
@app.route('/incidents/<unit_type>', methods=['GET'])
def get_incidents(unit_type: str):
  '''Retrieve ELEVATOR or ESCALATOR specific incidents from WMATA API.'''
  
  # Create an empty list called 'incidents'
  incidents = []
  # Use 'requests' to do a GET request to the WMATA Incidents API
  response = requests.get(INCIDENTS_URL, headers = headers)
  # Retrieve the JSON from the response
  response = response.json()

  # Iterate through the JSON response and retrieve all incidents matching 'unit_type'
  endpoint_mapping = {'escalators': 'ESCALATOR', 'elevators': 'ELEVATOR'}
  for incident in response['ElevatorIncidents']:
     if incident['UnitType'] == endpoint_mapping[unit_type]:
        # Collecting only the desired attributes for each incident
        info = {}
        for attribute in ['StationCode', 'StationName', 'UnitType', 'UnitName']:
           info[attribute] = incident[attribute]
        incidents.append(info)
  
  # Return collected incidents of unit_type
  return json.dumps(incidents)


if __name__ == '__main__':
    app.run(debug=True)
