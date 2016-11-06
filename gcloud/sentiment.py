#!/usr/bin/python2.7
import argparse
from googleapiclient import discovery
import httplib2
import json
import numpy
from oauth2client.client import GoogleCredentials
from textblob import TextBlob

DISCOVERY_URL = ('https://{api}.googleapis.com/'
                 '$discovery/rest?version={apiVersion}')

def analyse_sentiment(text):
    ''' Run a sentiment analysis and return the results'''
    http = httplib2.Http()
    credentials = GoogleCredentials.get_application_default().create_scoped(
        ['https://www.googleapis.com/auth/cloud-platform'])
    http = httplib2.Http()
    credentials.authorize(http)
    service = discovery.build('language', 'v1beta1',
                              http=http, discoveryServiceUrl=DISCOVERY_URL)
    service_request = service.documents().analyzeSentiment(
        body = {
            'document': {
                'type': 'PLAIN_TEXT',
                'content': text
            }
        }
    )
    # Google Cloud Natural Language analysis
    response = service_request.execute()
    # TextBlob analysis
    tb_analysis = TextBlob(text).sentiment

    gc_polarity = response['documentSentiment']['polarity']
    magnitude = response['documentSentiment']['magnitude']
    tb_polarity = tb_analysis.polarity
    subjectivity = tb_analysis.subjectivity

    # For now, just take an average of polarities
    polarity = numpy.mean([tb_polarity, gc_polarity])

    return polarity, magnitude, subjectivity

def main(movie_review_file):
    '''Run a sentiment analysis request on text within a passed filename'''
    review_text = open(movie_review_file, 'r')
    sentiment = analyse_sentiment(review_text.read())

    print('Sentiment Analysis Results:\npolarity: %s\nmanitute: %s\n'
          'subjectivity: %s' % sentiment)
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'movie_review_file', help = 'The filename of the movie review you\'d like to analyze.')
    args = parser.parse_args()
    main(args.movie_review_file)
