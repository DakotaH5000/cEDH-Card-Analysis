import requests
from pprint import pprint
import re
import time


def convertPath(url):
    baseURL = 'https://api2.moxfield.com/v3/decks/all/'
    invalidDecklists = [
      r'None', 
      r'^\s*$']
    if "undefined" not in url and not any(re.match(pattern, url) for pattern in invalidDecklists):
        targetPath = url.split('/')[-1]
    return baseURL + targetPath

def getDeckArrayFromMoxifled(deckURL):
    deckList = []
    time.sleep(5)
    response  = requests.get(deckURL)
    response = response.json()
    cardIDpath = response["boards"]["mainboard"]["cards"]
    for card in cardIDpath.items():
        deckList.append(card[1]['card']['name'])
    return deckList