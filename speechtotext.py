# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 18:23:36 2018

@author: Anette
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 17:28:15 2018

@author: Anette

"""
import requests
import websocket
import json
import time
import watson_developer_cloud 
#import asyncio
#import websockets

uri='https://stream.watsonplatform.net/authorization/api/v1/token?url=https://stream.watsonplatform.net/speech-to-text/api'
user='87ec9982-c076-4fee-86b5-c14ad246b1cb'
password='X0OyWhpx32t6'
#get token
r=requests.get(uri,auth=(user,password))
token=r.text
print(token)

#voice = 'en-GB_KateVoice'
formaatti = 'audio/flac'
texy = 'audio-file.flac'

wsURI = 'wss://stream.watsonplatform.net/speech-to-text/api/v1/recognize?watson-token=' + token + '&model=en-GB_BroadbandModel'
ws = websocket.create_connection(wsURI)

message = {
    'audio': texy,
    'action': 'start',
    'content-type': formaatti,
    'interim_results': 'true',
    'max-alternatives': 3,
    'keywords': ['colorado', 'tornado', 'tornadoes'],
    'keywords_threshold': 0.5
  }

#otettaan tavaraa vastaan
#async def hello():
 #   async with websockets.connect(wsURI) as ws:

speech_to_text = watson_developer_cloud.SpeechToTextV1(
        username = '87ec9982-c076-4fee-86b5-c14ad246b1cb',
        password = 'X0OyWhpx32t6'
        )
#respo = speech_to_text.list_workspaces()  
#print(json.dumps(respo, indent=2)) 
#ws.send(json.dumps(message))
#ws.send(texy)

with open(texy) as audio_file:
    resposta = json.dumps(speech_to_text.recognize(audio_file, content_type=formaatti, model='en-GB_BroadbandModel', timestamps=True, word_confidence=True),indent=2)
print(resposta)

time.sleep(10)

ws.send(json.dumps({'action': 'stop'}))
#asyncio.get_event_loop().run_until_complete(hello())
        

#response = json.loads(texy)
#print(response)
