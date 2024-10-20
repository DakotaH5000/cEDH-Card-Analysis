from cardRetrival import getCardData
import datetime
from touramentRetrival import getTournamentDeckLists
from TopDeckGGAPIrequests import requestTopDeckGGAPI
import asyncio
from pprint import pprint


async def main():
    tournaments = await requestTopDeckGGAPI()
    for tournament in tournaments:
        decklistArray = await getTournamentDeckLists(tournament)
        startTime = datetime.datetime.now()
        await getCardData(decklistArray)
        finishTime = datetime.datetime.now()
        print(finishTime - startTime)
    return -1


asyncio.run(main())