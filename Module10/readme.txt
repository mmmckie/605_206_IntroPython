Name: Max McKie (mmckie2)

Module Info: Module 10 Assignment: Accessibility API due on 11/02/2025 at
                                    11:59 PM EST

Approach: 

wmata_api.py - The 'get_incidents()' function is first defined to accept an
argument 'unit_type'. Inside this function, an empty list called 'incidents' is
created to store all incidents returned from the WMATA API of the corresponding
unit type. A GET request is sent to the API, and the response is stored in JSON
format. Before iterating through all incidents in the response, a dict called
'endpoint_mapping' is first defined to determine whether the incidents to return
should have a unit type of 'ELEVATOR' or 'ESCALATOR' based on the 'unit_type'
argument passed to the function. Next, all incidents in the JSON response are
iterated through in a for loop, and for any incidents where the unit type matches
the desired value ('ESCALATOR' or 'ELEVATOR'), an empty dict called 'info' is
created. This dict is then populated with the four key-value pairs for 
'StationCode', 'StationName', 'UnitType', and 'UnitName' obtained from the JSON
for that particular incident, and 'info' is appended to 'incidents'. Finally,
'incidents' is returned as a JSON string using 'json.dumps(incidents)'.

test_wmata_api.py - The first unit test, 'test_http_success()' first queries the
'incidents/escalators' endpoint and saves its status code to a variable. Then, a
call to 'self.assertEqual()' checks to ensure this status code is a 200 to verify
the endpoint is responding properly. This function then does the exact same for
the 'incidents/elevators' endpoint. The second unit test, 'test_required_fields()',
frst defines all the fields that should be present for each incident in the
response in a list. Then, a for loop first gets the JSON response for each of the
two endpoints '/incidents/escalators' and '/incidents/elevators'. Inside this for
loop, there is another for loop that iterates over each individual incident
returned by the GET request. For each field in the list of required fields, this
inner for loop calls 'self.assertIn()' to verify that all of the required fields
are contained in each and every incident returned by the API. The third unit test,
'test_escalators()', makes a GET request to the '/incidents/escalators' endpoint
and retrieves the JSON response. Then, for each incident of the response, a call
to 'self.assertEqual()' verifies that the 'UnitType' field is equal to 'ESCALATOR'
to verify that all incidents are of the correct type. The final unit test, 
'test_elevators()', functions exactly the same as 'test_escalators()', except the
GET request is made to the '/incidents/elevators' endpoint and the 'UnitType'
field is checked for equality with 'ELEVATOR'.

Known Bugs:
There are no known bugs.

Citations:
N/A