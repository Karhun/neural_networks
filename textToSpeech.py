# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 17:28:15 2018

@author: Anette

"""
import requests
import websocket
import json

uri='https://stream.watsonplatform.net/authorization/api/v1/token?url=https://stream.watsonplatform.net/text-to-speech/api'
user='5336a282-212b-4be7-bc47-f3301bb8621c'
password='wmjeFrmHnaxJ'
#get token
r=requests.get(uri,auth=(user,password))
token=r.text
print(token)

voice = 'en-GB_KateVoice'
formaatti = 'audio/wav'

wsURI = "wss://stream.watsonplatform.net/text-to-speech/api/v1/synthesize?voice=" + voice + "&watson-token=" + token
ws = websocket.create_connection(wsURI)

ws.send(json.dumps({'text':'Hello texy', 'accept':formaatti}))
print(type('Hello texy'))
#otettaan tavaraa vastaan
texy = ws.recv()
response = json.loads(texy)
print(response)

texy1 = ws.recv()
texy2 = ws.recv()
#texy3 = ws.recv()

with open("helloworld.wav","wb") as file:
    file.write(texy1)
    file.write(texy2)
#    file.write(texy3)