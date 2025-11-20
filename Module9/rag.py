'''
This module defines the RAG class to obtain an augmented description of NASA's
APOD using an ollama model and a wikipedia summary of key terms in the APOD
description.
'''

from ollama import chat

class RAG:
    
    def __init__(self, model: str):
        self.model = model


    def rag_response(self, prompt: str):
        '''Query ollama model and return response content.'''

        response = chat(model = self.model,
             messages = [{'role': 'user', 'content': prompt}])
        
        return response['message']['content']


    def generate_lookup_list(self, photo_explanation: str, file_name: str):
        '''Utilize ollama model to ingest image description and generate list of
        terms to search on Wikipedia for RAG.

        Arguments:
        photo_explanation: str = image description returned from APOD API

        file_name: str = file name to write list of Wikipedia search terms to
        '''

        LOOKUP_PROMPT = 'Analyze the following and based on the information ' \
            + 'provided, create a list of terms to look-up for more information. ' \
            + 'The list should be returned as a list of strings in python ' \
            + 'format. No other information should be returned. Information: '
        
        prompt = LOOKUP_PROMPT + photo_explanation
        
        # Send prompt to ollama model, save response
        response = self.rag_response(prompt= prompt)

        # Strip [] from beginning/end, drop quotes
        response = response[1:-1].replace('"','')
        
        # Split string list of terms to create python list
        search_terms = response.split(', ')
        
        # Unicode bullet point escape sequence for pretty printing
        BULLET_POINT = '\u2022'

        # Write each search term to output file
        with open(file_name, 'a') as f:
            
            f.write('Additional Search Terms:\n')
            for term in search_terms:
                f.write(f'{BULLET_POINT} {term}\n')
            
            f.write('\n')

        return search_terms


    def generate_augmented_description(self, apod_info, wiki_summary):
        '''
        Generates RAG augmented description of APOD photo using the summary
        retrieved from Wikipedia.

        Arguments:
        apod_info: dict = payload retrieved from NASA's APOD API
        wiki_summary: str = Wiki summary of key terms in photo explanation

        Returns:
        augmented_description: str = ollama model description of APOD photo
        '''
        
        photo_title = apod_info['Title']
        photo_explanation = apod_info['explanation']
        
        RAG_PROMPT = f'NASA APOD Title: {photo_title}\n' \
                        + f'Explanation: {photo_explanation}\n' \
                        + 'Additional Context from Wikipedia:\n' \
                        + f'{wiki_summary}\n' \
                        + 'Write a more detailed and accessible description ' \
                        + 'of the image using all of the above'

        # Send RAG prompt to ollama model to get augmented photo description
        augmented_description = self.rag_response(RAG_PROMPT)
        return augmented_description
