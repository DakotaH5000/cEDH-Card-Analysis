import os
import requests
#Thank you top deck gg for the FREE data source for all things cEDH

async def requestTopDeckGGAPI():
    APIkey = os.getenv("API_KEY")

    headers = {
        "Authorization": APIkey
    }
#Modify Last to change number of tournaments
    body = {
    "last": 10,
    "rounds": False,
    "deckSnapshot": True,
    "game": "Magic: The Gathering",
    "format": "EDH",
    "participantMax": 100,
    "participantMin": 50
    }

    APIkey = os.getenv("API_KEY")
    response = requests.post('https://topdeck.gg/api/v2/tournaments', headers=headers, json=body)
    return response.json()