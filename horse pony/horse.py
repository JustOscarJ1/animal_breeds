import time
from bs4 import BeautifulSoup # pip install bs4
import requests # pip install requests

request_data = requests.get('https://en.wikipedia.org/wiki/List_of_horse_breeds#').text # Makes a request to the website and gets the HTML data by accessing the .text attribute of the request.
soup = BeautifulSoup(request_data, features="html.parser") # Uses the HTML data to make soup.

horse_pony = 'pony' # Which animal you want to get the data for.

if horse_pony.lower() == 'horse':
    for i in soup.select('div[class="div-col"]')[0:4]: # Grabs every element with this specific CSS selector then iterates over the elements.
        print(i.text) # Prints the text within the element
elif horse_pony.lower() == 'pony':
    for i in soup.select('div[class="div-col"]')[4:]:
        print(i.text)
else:
    print('Unknown animal... accepted: Horse, Pony')

time.sleep(5) # Allows time for user to collect results.


'''
**IT IS NOT A GOOD IDEA TO USE THIS DATA**

First five results of sector are horse breeds, the rest are pony breeds.

Contains high amounts on non-breed data, example:
"Warmblood, see "Types of horse" below, or individual warmblood breed articles",
"Svensk Kallblodstravare (Swedish Coldblood Trotter), see Coldblood Trotter"
"Mountain and moorland pony breeds, abbreviated "M&M," a specific group of pony breeds native to the British Isles."
'''