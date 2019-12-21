# -*- coding: utf-8 -*-
"""
Created on Wed Mar  7 17:01:00 2018

@author: Anette
"""
import json
import watson_developer_cloud 

conversation = watson_developer_cloud.ConversationV1(
    username = 'bef8a2a7-65b6-4fcb-99d1-920b0779d8b3',
    password = 'KjJTjZDKDEs5',
    version = '2018-03-07'
)
#response = conversation.list_workspaces()

response = conversation.message(
    workspace_id='c39d60be-4f64-4b04-a047-70715b04c63b',
    input={
        'text': 'several tornadoes touch down is a line of severe thunderstorms swept through Colorado on Sunday'
    }
)

print(json.dumps(response, indent=2))