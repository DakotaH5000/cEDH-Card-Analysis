from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import asyncio
import datetime
import threading
from datetime import date
import re
import os
import csv
import logging
from moxfieldAPIresolver import convertPath, getDeckArrayFromMoxifled



#
filterValues = [ 
    r'Instants\(', 
    r'Artifacts\(',     
    r'Creatures\(',            
    r'Commander\(',             
    r'Enchantments\(',          
    r'Planeswalkers\(',
    r'Battles\(',        
    r'Lands\(',                
    r'Sorceries\(',
    r'\n', 
    r'Sideboard\(']


async def getCardData(decklists):
    #Deck list is [Name of tournament, [Array of decklist URLS]]
    cardDict = {}
    #Used to track error rate and provide feedback while program is running
    deckspercent = 0
    errorCount = 0
    #Core loop for determining cards, take a decklist and iterate through it adding it to a dictionary. 
    #Would like to expermient with this for multithrading, main concern will be race conditions causing in correct card counts
    #And a very difficult time in manually verifiying this data. 
    for url in decklists[1]:
        print(f'{((deckspercent/len(decklists[1])) * 100)}%'  )
        deckspercent += 1
        try:
            deckURL = convertPath(url)
            deckList = getDeckArrayFromMoxifled(deckURL)

            for card in deckList:
                if(card not in cardDict and not card == ''):
                    cardDict[card] = 1
                elif(card in cardDict and not card == ''):
                    cardDict[card] += 1


        except Exception as e:
            print(f' error: {e}')
            errorCount += 1
    cardDict = dict(sorted(cardDict.items(), key=lambda item: item[1], reverse=True))
    with open(f'Data/{decklists[0]}', mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(f'{decklists[0]}')
        writer.writerow(f'Deck Count: {len(decklists[1])}')
        writer.writerow(["Card Name", "Count"])
        writer.writerow([f'Decklist errors {errorCount}'])  # Write headers
        for key, value in cardDict.items():
            writer.writerow([key, value]) 
    for key in cardDict:
        print(f'{key}: {cardDict[key]}')



#asyncio.run(main())