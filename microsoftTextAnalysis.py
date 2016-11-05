import httplib, urllib, base64


text = {
  "documents": [
    {
      "language": "en",
      "id": "string",
      "text": "Power BI transforms your company's data into rich visuals for you to collect and organize so you can focus on what matters to you",
    }
  ]
}




def microsoftParse(what, text):

    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': '0c3a0dfd10294ff49b41284521a05d70',
    }

    params = urllib.urlencode({
    })

    try:
        conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
        if what == "sentiment":
            conn.request("POST", "/text/analytics/v2.0/sentiment_url?%s" % params, text, headers)
        elif what == "keyPhrases":
            conn.request("POST", "/text/analytics/v2.0/keyPhrases?%s" % params, text, headers)
        else:
            

        response = conn.getresponse()
        data = response.read()
        print(data)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))


microsoftParse(topics, text)


