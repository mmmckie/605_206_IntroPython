'''
This module defines a generic API class to send get requests to a given API url.
'''
import requests

class API:

    def __init__(self, base_url: str, api_key: str = None):
        self.url = base_url
        self.api_key = api_key


    def get_response(self, request_params):
        '''Send GET request to provided url and pass provided query params, then
        return response in JSON format.
        '''
        
        response = requests.get(self.url, params=request_params)
        return response.json()
