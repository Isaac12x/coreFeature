import httplib, urllib, base64
import json
from json import JSONEncoder

text = "Bring people from outside amazon to amazon (Facebook ads!!!) Amazon says thank you and give you free traffic!"


def microsoftParse(what, text):

    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '0c3a0dfd10294ff49b41284521a05d70',
    }

    params = urllib.urlencode({
    })

    rext = json.dumps(text)
    
    jsonString = JSONEncoder().encode({
        "documents": [{"language": "en", "id": "string", "text": rext}]
    })

    print jsonString


    try:
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        if what == "sentiment":
            conn.request("POST", "/text/analytics/v2.0/sentiment?%s" % params, jsonString, headers)
            response = conn.getresponse()
            data = response.read()
            rs = json.load(data)
            return rs
            conn.close()

        elif what == "phrases":
            conn.request("POST", "/text/analytics/v2.0/keyPhrases?%s" % params, text, headers)
            response = conn.getresponse()
            data = response.read()
            return data
            conn.close()
        else:
            print("you forget something")

    except Exception as e:
        print("Error")



microsoftParse("sentiment", text)


