import requests
import json
from watson_developer_cloud import speech_to_text_v1


def get_me_text(audioFile):
    speech = speech_to_text_v1(
        username='18ab33e2-0567-4d02-ad63-266171c3b14d',
        password='rPBiaHH8L4Ji',)
    try:
        return json.dumps(speech.recognize(audio=audioFile))
    except:
        return False

