'''
A series of unit tests for the enhanced WMATA API.
'''

from wmata_api import app
import json
import unittest

class WMATATest(unittest.TestCase):
    # Ensure both endpoints return a 200 HTTP code
    def test_http_success(self):
        escalator_response = app.test_client().get('/incidents/escalators').status_code
        # Assert that the response code of 'incidents/escalators returns a 200 code
        self.assertEqual(escalator_response, 200, 'escalators did not return a 200 code')
        
        elevator_response = app.test_client().get('/incidents/elevators').status_code
        # Assert that the response code of 'incidents/elevators returns a 200 code
        self.assertEqual(elevator_response, 200, 'elevators did not return a 200 code')

    # Ensure all returned incidents have the 4 required fields
    def test_required_fields(self):
        required_fields = ['StationCode', 'StationName', 'UnitType', 'UnitName']

        for endpoint in ['escalators', 'elevators']:
            response = app.test_client().get(f'/incidents/{endpoint}')
            json_response = json.loads(response.data.decode())

            # For each incident in the JSON response assert that each of the
            # required fields is present
            for entry in json_response:
                for field in required_fields:
                    self.assertIn(field, entry, f'{field} not in JSON response')

    # Ensure all entries returned by the /escalators endpoint have a UnitType of
    # "ESCALATOR"
    def test_escalators(self):
        response = app.test_client().get('/incidents/escalators')
        json_response = json.loads(response.data.decode())
        # Check each entry for the correct unit type
        error_msg = '/escalators returned non-escalator outage'
        for entry in json_response:
            unit_type = entry['UnitType']
            self.assertEqual(unit_type, 'ESCALATOR', error_msg)

    # Ensure all entries returned by the /elevators endpoint have a UnitType of
    # "ELEVATOR"
    def test_elevators(self):
        response = app.test_client().get('/incidents/elevators')
        json_response = json.loads(response.data.decode())
        # Check each entry for the correct unit type
        error_msg = '/elevators returned non-elevator outage'
        for entry in json_response:
            unit_type = entry['UnitType']
            self.assertEqual(unit_type, 'ELEVATOR', error_msg)


if __name__ == "__main__":
    unittest.main()
    