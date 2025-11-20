Name: Max McKie (mmckie2)

Module Info: Module 8 Assignment: Generative Artificial Intelligence due on
                                    10/27/2025 at 11:59 PM EST

Approach: 

api.py - This module first imports requests and then the API class is defined.
The init method takes a url and an api key as parameters, both strings, and sets
the instance variables 'self.url' and 'self.api_key' to these values. There is
also a 'get_response()' method that takes API request parameters as an argument
and sends a get request to 'self.url' using these parameters, then returns the
response in JSON format.

apod.py - This module first imports requests and the API class from api.py. Then
the APOD class is defined to inherit from the API class. The NASA APOD API url
is defined as a class variable since this class is only meant to be used with
that API. Next an init method is defined that takes an api key as an argument.
This init method first calls super().__init__() to instantiate the parent API
class using the NASA APOD API url and the provided api key. Next there is a
'fetch_apod()' method that takes a date argument in the format 'YYYY-MM-DD'. If
the date passed is '2024-12-14', then the provided dummy payload is hardcoded
with 'Title' and 'explanation' fields as provided in the assignment. If it is
any other value, then the payload will be created with information stating that
the date entered was invalid and a message stating that the date was invalid will
be printed to the terminal. The method then returns the payload. There is also a
'download_image()' method that accepts a file name and url as strings. The url
argument is set to None by default since the APOD API is currently down. If url
is None, then the url will be set to a string stating that the image download is
skipped due to the API outage. Then, the value of 'url' will be printed to the
terminal and it will be appended to the end of the file named 'file_name'.

wiki.py - This module first imports wikipedia and warnings, then calls
warnings.filterwarnings() to prevent warning messages from cluttering the
terminal. A function 'fetch_wikipedia_summary()' is defined to accept two
arguments 'query_term' and 'file', both as strings, for the term to search on
wikipedia and the filename to write the resulting summary to. Inside a try block,
any spaces in the query_term are first replaced with an underscore character.
Then a variable 'search_results' is created to store the result of calling
wikipedia.search() with 'query_term'. If there are no search results, then a
message will be printed to 'file' stating that no articles were found for that
term. Otherwise, the summary of only the first result will be retreived by
calling wikipedia.summary() with the first element of search_results and then
written to 'file', and the summary will be returned. Outside of the try block,
an except block will print a statement to 'file' stating that an issue occured
retrieving information from wikipedia about 'query_term' if any errors occur
during execution of the try block. 

rag.py - This module first imports chat from the ollama library, then defines
the RAG class. This class' init method accepts a model name as a string to
define which ollama model to use. A 'rag_response()' method is defined to accept
a string prompt and then generate a response from the model using the chat import
and passing the prompt as the content. The response's message content is then
returned. Next there is a 'generate_lookup_list()' method that accepts a photo
explanation and a file name as string parameters. A lookup prompt is defined
according to the assignment instructions, and then the photo explanation is
concatenated onto it to form the full prompt to pass to the ollama model. A
variable 'response' is created to store the result of calling 'rag_response()'
with this prompt, and then the parentheses and double quote characters are
removed from the response. A list of all the individual search terms is then
created by calling response.split(', '), and the unicode escape sequence for a
bullet point is stored in a variable. Then 'file_name' is opened, and each search
term is written to the file on a new line with a preceding bullet point, and
finally the list of search terms is returned. Lastly, there is a method
'generate_augmented_description()' that accepts 'apod_info' (the payload returned
from the APOD API call), and 'wiki_summary', a string. The photo's title and
explanation are retrieved from the provided 'apod_info' and the RAG prompt is
defined according to the assignment instructions by using f-strings and
concatenation to fill in the required fields. Finally, the augmented photo
description is obtained by passing the RAG prompt into 'self.rag_response()',
and the augmented description is returned.

main.py - This module first imports the datetime module, the APOD and RAG classes,
and the wiki module. Then the NASA APOD API key is stored in a variable (although
it is not currently used due to the API outage), and the 'run_rag()' function is
defined to accept a 'date' argument in 'YYYY-MM-DD' format, with a default value
of None. Inside the function, if 'date' is none, then datetime.today() will
retrieve today's date and use the datetime.strftime() function to transform the
date to 'YYYY-MM-DD' format. Next, the an instance of the APOD class is created
using the APOD API key defined above, and the 'apod_info' payload is obtained
using 'apod.fetch_apod()' with the provided date. The photo's explanation and
the filename to write all subsequent results to are assigned to variables, and
then the explanation is written to the results file as well as printed to the
terminal. Next, an instance of the RAG class is instantiated to use ollama's
llama3.2 model. A lookup list of terms to search on Wikipedia is created using
'rag.generate_lookup_list()' with the photo explanation, and then a summary for
each term is created by iterating through this list and calling
'wiki.fetch_wikipedia_summary()' for each item, and each item summary is
concatenated to a single string 'all_item_summaries'. Next the augmented photo
description is created by calling 'rag.generate_augmented_description()' and
passing 'apod_info' along with 'all_item_summaries', and the RAG generated
description is written to the results file as well as printed to the terminal.
Finally, 'apod.download_image()' is called to write the image url to the results
file (under normal circumstances). Outside of this function, there is an if name
equals main statement to call 'run_rag('2024-12-14')' if this module is executed
as a script.

Known Bugs:
There are no known bugs.

Citations:
-https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior