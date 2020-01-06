#!/usr/bin/env python3.8
#>
# Author: sullenbode
# Description: Test script for practicing web scraping techniques with Python. Based off of a tutorial video on the tutorialinux YouTube channel.
#>

import requests
from bs4 import BeautifulSoup

url = 'https://www.humblebundle.com/books/python-machine-learning-packt-books'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# Creates a list of bs4 elements that have the specific child tag I'm looking for (h2 tags of dd-header-headline class)
# This is to exclude the final div tag from the scope of parent elements, as it contains an irrelevant h2 tag that happens to have the same class we'll be selecting.

tier_containers = soup.find_all('div', {'class': 'main-content-row dd-game-row js-nav-row'})

# The 3 elements can be accessed from the list with positional indexes, e.g. tier_containers[0]. Iterate through the list, grabbing the h2 tags and pulling the text, stripping whitespace from text for the final result.

tiernames = []
num_tiers = len(tier_containers)
i = 0

while i < num_tiers:
    tiernames.append(tier_containers[i].find('h2'))
    i += 1

# Use list comprehensions to get raw text, strip whitespace, and put the h2 tags into a list

stripped_tiernames = [tier.text.strip() for tier in tiernames]

print(stripped_tiernames)

# TODO:  Create a dictionary that includes the tier (tier 1, tier 2, etc.), the price for each tier, and the associated book names.

