from bs4 import BeautifulSoup # pip install bs4
import requests # pip install requests
import time

request_data = requests.get('https://en.wikipedia.org/wiki/List_of_dog_breeds').text # Makes a request to the website and gets the HTML data by accessing the .text attribute of the request.
soup = BeautifulSoup(request_data, features="html.parser") # Uses the HTML data to make soup.

for i in soup.select('div[class="div-col"] >ul > li > a'): # Grabs every element with this specific CSS selector then iterates over the elements.
    print(i.text) # Prints the text within the element


time.sleep(5) # Allows time for user to collect results.
