from textblob import TextBlob
from sys import argv

script, text = argv

file_object = open(text, 'r')
file_object.read()

def first_analysis(inputText):
    analysis = TextBlob(inputText)
    text_sentiment = analysis.sentiment 
    text_sentiment_polarity = text_sentiment.polarity
    text_sentiment_subjectivity = text_sentiment.subjectivity

first_analysis(file_object)
