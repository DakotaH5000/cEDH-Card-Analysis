import requests
from pprint import pprint
import re
from dotenv import load_dotenv


async def getTournamentDeckLists(tournamentObject):
  invalidDecklists = [
      r'None', 
      r'^\s*$']

  tournament = tournamentObject
  pprint(f'tournament name: {tournament["tournamentName"]}')

  decks = []
  for deck in tournament["standings"]:
      if isinstance(deck["decklist"], str):
        if "undefined" not in deck["decklist"] and not any(re.match(pattern, deck["decklist"]) for pattern in invalidDecklists):
          decks.append(deck["decklist"])
          #Return a tourny name, decklist array
  return [tournament["tournamentName"], decks]


#getTournamentDeckLists()