#!/usr/bin/python2.7

import sys
import os
sys.path.append(os.path.dirname(__file__) + '/../gcloud')
sys.path.append(os.path.dirname(__file__) + '/../sns')
sys.path.append(os.path.dirname(__file__) + '/../server/coreFeature')

import json

from sentiment import analyse_sentiment
from tweets import query_lgbt_tweets, get_location_from_addr
from personality_insights import PersonalityInsightsService

def main(address_list):
    watsonInsights = PersonalityInsightsService()
    output = open('insights.out', 'w')
    for addr in address_list:
        loc = get_location_from_addr(addr)
        text = '\n'.join(query_lgbt_tweets(loc[0], loc[1]))
        res = watsonInsights.getProfile(text.encode('utf8'))
        output.write('\n' + addr + ':\n')
        json.dump(res, output, ensure_ascii=False)

if __name__ == '__main__':
    ldn_boroughs = ["Camden, London",
                    "Royal Borough of Greenwich, London",
                    "Hackney, London",
                    "Hammersmith and Fulham, London",
                    "Islington, London",
                    "Royal Borough of Kensington and Chelsea, London",
                    "Lambeth, London",
                    "Lewisham, London",
                    "Southwark, London",
                    "Tower Hamlets, London",
                    "Wandsworth, London",
                    "City of Westminster, London"]
    main(ldn_boroughs)
