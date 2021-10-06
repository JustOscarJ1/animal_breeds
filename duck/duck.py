import time
from bs4 import BeautifulSoup # pip install bs4
import requests # pip install requests

request_data = requests.get('https://en.wikipedia.org/wiki/List_of_duck_breeds').text # Makes a request to the website and gets the HTML data by accessing the .text attribute of the request.
soup = BeautifulSoup(request_data, features="html.parser") # Uses the HTML data to make soup.

for i in soup.select('div[class="mw-parser-output"] > ul > li > a'): # Grabs every element with this specific CSS selector then iterates over the elements.
    print(i.text) # Prints the text within the element

time.sleep(5) # Allows time for user to collect results.

'''
Will return four non-breed results, all at the start of the list.
Index 0: "American Poultry Association"
Index 1: "Poultry Club of Great Britain"
Index 2: "Entente Européenne d’Aviculture et de Cuniculture"
Index 3: "Australian Poultry Standards"
'''