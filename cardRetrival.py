from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import asyncio
import datetime
import threading
from datetime import date
import re
import os
from touramentRetrival import getTournamentDeckLists
import csv
import logging
from moxfieldAPIresolver import convertPath, getDeckArrayFromMoxifled



#browser = webdriver.Chrome()
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
    deckspercent = 0
    errorCount = 0
    for url in decklists[1]:
        print(f'{((deckspercent/len(decklists[1])) * 100)}%'  )
        deckspercent += 1
        try:
            deckURL = convertPath(url)
            deckList = getDeckArrayFromMoxifled(deckURL)
            deckListArray = []
            for card in deckList:
                if(card not in cardDict and not card == ''):
                    cardDict[card] = 1
                elif(card in cardDict and not card == ''):
                    cardDict[card] += 1
            #for key in cardDict:
                #print(f'{key}: {cardDict[key]}')
            #browser.quit()
        except Exception as e:
            print(f' error: {e}')
            errorCount += 1
    cardDict = dict(sorted(cardDict.items(), key=lambda item: item[1], reverse=True))
    with open(f'{decklists[0]}', mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Card Name", "Count"])
        writer.writerow(decklists[0])
        writer.writerow([f'Decklist errors {errorCount}'])  # Write headers
        for key, value in cardDict.items():
            writer.writerow([key, value]) 
    for key in cardDict:
        print(f'{key}: {cardDict[key]}')



#asyncio.run(main())