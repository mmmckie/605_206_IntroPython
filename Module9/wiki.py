'''
Retrieve Wikipedia Summary based on formatted query term.
'''

import wikipedia
import warnings

## This handles a warning message that can sometimes occur with wikipedia
warnings.filterwarnings('ignore') 


def fetch_wikipedia_summary(query_term: str, file: str):
    '''Search wiki for query_term, fetch summary of the first result, and print
    summary to file.

    Arguments:
    query_term: str = term to search on wikipedia
    file: str = file name to write results to

    Returns:
    summary: str = retrieved wiki summary
    '''
    
    ## Search for article titles related to the query
    try:
        # Replace all spaces in the query_term with underscores ('_')
        query_term = query_term.replace(' ', '_')

        # Use wikipedia's search method to search for the query_term
        search_results = wikipedia.search(query_term)
        
        # Note: Multiple results will be returned in a list, we will only use
        # the first entry. 

        # If there are no results of the search, print to file: "No article
        # found for 'query_term'" and return None.
        if len(search_results) == 0:
            with open(file, 'a') as f:
                f.write(f"No articles found for '{query_term}'...\n")
        else:
            # Store the first result
            first_result = search_results[0]
            
            # Fetch the wikipedia summary and write to file, then return summary
            with open(file, 'a') as f:
                f.write(f"Searching Wikipedia for '{query_term}'...\n")
                summary = wikipedia.summary(first_result)
                f.write(f"Summary of '{first_result}': {summary}")
                
                # Formatting for file readability
                if not summary.endswith('\n'):
                    f.write('\n')

            return summary

    except:
        # Print to file: "An issue occured retrieving information for 'query_term'."
        with open(file, 'a') as f:
            f.write(f'An issue occurred retrieving information for {query_term}\n')
