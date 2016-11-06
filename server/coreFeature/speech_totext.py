import requests
import json
from watson_developer_cloud import speech_to_text_v1


def get_me_text(audioFile):
    speech = speech_to_text_v1(
        username='fb3a4eef-3535-4ea1-9920-5f944f53spee6501',
        password='C4lmPJgiupQB',)
    try:
        return json.dumps(speech.recognize(audio=audioFile))
    except:
        return False

