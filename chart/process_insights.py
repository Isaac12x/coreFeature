#!/usr/bin/python2.7
import json

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

insights = open('./insights.out', 'r')
objList = json.load(insights)
for i in range(len(objList)):
    obj = objList[i]
    print(ldn_boroughs[i])
    for insight in obj['tree']['children']:
        if insight['id'] != "personality":
            continue
        numbers = []
        for attr in insight['children'][0]['children']:
            numbers.append(str(attr['percentage']))
        print(','.join(numbers))

