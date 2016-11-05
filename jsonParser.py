import urllib, json
from sys import argv

def parseJsonToText(url):
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return data

parseJsonToText("https://www.campus.co/london/en/contact")