'''
This module defines the APOD class to fetch NASA's Astronomy Picture of the day
from the APOD API.
'''

from api import API

class APOD(API):

    # NASA's APOD API url
    url = 'https://api.nasa.gov/planetary/apod'

    def __init__(self, api_key):
        super().__init__(self.url, api_key)


    def fetch_apod(self, date: str):
        '''Fetch APOD info for provided date. Due to current APOD API outage,
        a dummy payload has been defined for '2024-12-14'. All other passed
        values are invalid.
        
        Arguments:
        date: str = YYYY-MM-DD
        
        Returns:
        payload: dict
            --> payload['Title'] = <Title of photo>
            --> payload['explanation'] = <Photo explanation>
        '''

        if date == '2024-12-14':
            payload = {'Title': 'Apollo 17: Challenger in Lunar Orbit'}
            
            explanation = "Awkward and angular looking, Apollo 17's lunar " \
                + "module Challenger was designed for flight in the near " \
                + "vacuum of space. Digitally enhanced and reprocessed, this " \
                + "picture taken from Apollo 17's command module America shows " \
                + "Challenger's ascent stage in lunar orbit. Small reaction " \
                + "control thrusters are at the sides of the moonship with the " \
                + "bell of the ascent rocket engine underneath. The hatch " \
                + "allowing access to the lunar surface is seen at the front, " \
                + "with a round radar antenna at the top. Mission commander " \
                + "Gene Cernan is clearly visible through the triangular " \
                + "window. This spaceship performed gracefully, landing on the " \
                + "Moon and returning the Apollo astronauts to the orbiting " \
                + "command module in December of 1972. So where is Challenger " \
                + "now? Its descent stage remains at the Apollo 17 landing " \
                + "site in the Taurus-Littrow valley. The ascent stage pictured " \
                + "was intentionally crashed nearby after being jettisoned " \
                + "from the command module prior to the astronauts' return to " \
                + "planet Earth."
            
            payload['explanation'] = explanation
        
        else:
            payload = {'Title': 'Invalid Date'}
            explanation = 'Invalid date provided. Please provide a valid date.'
            payload['explanation'] = explanation
            print(explanation)
        
        return payload


    def download_image(self, file_name: str, url: str = None):
        '''Prints the url to terminal and writes it to the end of file at
        file_name.
        '''
        
        if url is None:
            url = 'Image download is skipped due to APOD API outage'
        
        print('\n' + url)
        with open(file_name, 'a') as f:
            f.write(url)
            f.write('\n')
