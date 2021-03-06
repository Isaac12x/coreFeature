#
# Copyright 2014 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
## -*- coding: utf-8 -*-

import os
import requests
import json



class PersonalityInsightsService:
    """Wrapper on the Personality Insights service"""

    def __init__(self):
        """
        Construct an instance. Fetches service parameters from VCAP_SERVICES
        runtime variable for Bluemix, or it defaults to local URLs.
        """

        # Local variables
        self.url = "https://gateway.watsonplatform.net/personality-insights/api"
        self.username = "aa8cd577-e982-4c1a-94fb-b7a83714a95b"
        self.password = "24GfATDypTuV"

    def getProfile(self, text):
        """Returns the profile by doing a POST to /v2/profile with text"""        

        if self.url is None:
            raise Exception("No Personality Insights service is bound to this app")
        response = requests.post(self.url + "/v2/profile",
                          auth=(self.username, self.password),
                          headers = {"content-type": "text/plain"},
                          data=text
                          )
        try:
        	return json.loads(response.text)
        except:
            raise Exception("Error processing the request, HTTP: %d" % response.status_code)

# class DemoService(object):
#     """
#     REST service/app. Since we just have 1 GET and 1 POST URLs,
#     there is not even need to look at paths in the request.
#     This class implements the handler API for cherrypy library.
#     """
#     exposed = True

#     def __init__(self, service):
#         self.service = service
#         self.defaultContent = None
#         try:
#             contentFile = open("public/text/en.txt", "r")
#             self.defaultContent = contentFile.read()
#         except Exception as e:
#             print "ERROR: couldn't read mobidick.txt: %s" % e
#         finally:
#             contentFile.close()

#     def GET(self):
#         """Shows the default page with sample text content"""

#         return lookup.get_template("index.html").render(content=self.defaultContent)


#     def POST(self, text=None):
#         """
#         Send 'text' to the Personality Insights API
#         and return the response.
#         """
#         try:
#             profileJson = self.service.getProfile(text)
#             return json.dumps(profileJson)
#         except Exception as e:
#             print "ERROR: %s" % e
#             return str(e)


# if __name__ == '__main__':
#     lookup = TemplateLookup(directories=["templates"])

#     # Get host/port from the Bluemix environment, or default to local
#     HOST_NAME = os.getenv("VCAP_APP_HOST", "127.0.0.1")
#     PORT_NUMBER = int(os.getenv("VCAP_APP_PORT", "3000"))
#     cherrypy.config.update({
#         "server.socket_host": HOST_NAME,
#         "server.socket_port": PORT_NUMBER,
#     })

#     # Configure 2 paths: "public" for all JS/CSS content, and everything
#     # else in "/" handled by the DemoService
#     conf = {
#         "/": {
#             "request.dispatch": cherrypy.dispatch.MethodDispatcher(),
#             "tools.response_headers.on": True,
#             "tools.staticdir.root": os.path.abspath(os.getcwd())
#         },
#         "/public": {
#             "tools.staticdir.on": True,
#             "tools.staticdir.dir": "./public"
#         }
#     }

#     # Create the Personality Insights Wrapper
#     personalityInsights = PersonalityInsightsService(os.getenv("VCAP_SERVICES"))

#     # Start the server
#     print("Listening on %s:%d" % (HOST_NAME, PORT_NUMBER))
#     cherrypy.quickstart(DemoService(personalityInsights), "/", config=conf)
