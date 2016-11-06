#!/usr/bin/python2.7

import sys
import os
sys.path.append(os.path.dirname(__file__) + '/../sns')

from tweets import query_lgbt_tweets, get_location_from_addr

def main(address_list):
    output = open('output.txt', 'w')

    for addr in address_list:
        loc = get_location_from_addr(addr)
        text = '\n'.join(query_lgbt_tweets(loc[0], loc[1]))
        output.write(text.encode('utf8'))

if __name__ == '__main__':
    addrs = ["London"]
    main(addrs)
