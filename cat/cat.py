import time
from bs4 import BeautifulSoup # pip install bs4
import requests # pip install requests

request_data = requests.get('https://www.tica.org/breeds/browse-all-breeds').text # Makes a request to the website and gets the HTML data by accessing the .text attribute of the request.
soup = BeautifulSoup(request_data, features="html.parser") # Uses the HTML data to make soup.

for i in soup.select('.rl_sliders-toggle-inner'): # Grabs every element with this specific CSS selector then iterates over the elements.
    print(i.text.strip()) # Prints the text within the element

time.sleep(5) # Allows time for user to collect results.