#!/usr/bin/python2.7

import sys
import os
sys.path.append(os.path.dirname(__file__) + '/../gcloud')
sys.path.append(os.path.dirname(__file__) + '/../sns')

from sentiment import analyse_sentiment
from tweets import query_lgbt_tweets, get_location_from_addr

def main(address_list):
    polarities = []
    subjectivities = []

    for addr in address_list:
        loc = get_location_from_addr(addr)
        text = '\n'.join(query_lgbt_tweets(loc[0], loc[1]))
        [p, m, s] = analyse_sentiment(text)
        polarities.append(str(p))
        subjectivities.append(str(s))

    print(','.join(polarities))
    print(','.join(subjectivities))

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
