# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 18:05:56 2018

@author: Anette
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 17:35:48 2018

@author: Anette
"""
import requests
import websocket
import json
import watson_developer_cloud 

conversation = watson_developer_cloud.ConversationV1(
    username = 'bef8a2a7-65b6-4fcb-99d1-920b0779d8b3',
    password = 'KjJTjZDKDEs5',
    version = '2018-03-07'
)
#esponse = conversation.list_workspaces()

response = conversation.message(
    workspace_id='c39d60be-4f64-4b04-a047-70715b04c63b',
    input={
        'text': 'several tornadoes touch down is a line of severe thunderstorms swept through Colorado on Sunday'
    }
)

#print(json.dumps(response, indent=2))
result = (response.get('output').get('text'))


uri='https://stream.watsonplatform.net/authorization/api/v1/token?url=https://stream.watsonplatform.net/text-to-speech/api'
user='5336a282-212b-4be7-bc47-f3301bb8621c'
pwd='wmjeFrmHnaxJ'
#get token
r=requests.get(uri,auth=(user,pwd))
token=r.text
print(token)

voice = 'en-GB_KateVoice'
formaatti = 'audio/wav'

wsURI = "wss://stream.watsonplatform.net/text-to-speech/api/v1/synthesize?voice=" + voice + "&watson-token=" + token
ws = websocket.create_connection(wsURI)
#print(type(result[0]))
ws.send(json.dumps({'text':'Hello texy', 'accept':formaatti}))
#ws.send(json.dumps({'text':result[0], 'accept':formaatti}))

#otettaan tavaraa vastaan
texy = ws.recv()
response = json.loads(texy)
print(response)

texy1 = ws.recv()
texy2 = ws.recv()
#texy3 = ws.recv()

with open('bob.wav','wb') as file:
    file.write(texy1)
    file.write(texy2)
#    file.write(texy3)