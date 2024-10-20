import requests
from pprint import pprint
import re
import time
import csv

#csv files cannot contain commas, replace them to allow proper usage
def replace_commas(value):
    return value.replace(',', '|')


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
    deckListCommanders = [[],[],[]]
    time.sleep(3)
    response  = requests.get(deckURL)
    response = response.json()
    cardIDpath = response["boards"]["mainboard"]["cards"]
    commanderPath = response["boards"]["commanders"]["cards"]
    for card in commanderPath.items():
        deckListCommanders[1].append(card[1]['card']['colors'])
        deckListCommanders[0].append(card[1]['card']['name'])
    for card in cardIDpath.items():
        deckListCommanders[2].append(card[1]['card']['name'])
        deckList.append(card[1]['card']['name'])

    for i, d in enumerate(deckListCommanders):
        for j, card in enumerate(d): 
            deckListCommanders[i][j] = replace_commas(''.join(card))  

    
    with open('Data/fullDeckLists.csv', mode='a', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(deckListCommanders)
        
    return deckList