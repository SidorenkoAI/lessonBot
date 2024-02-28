import requests
import pprint
with open('token.txt') as f:
    token = f.read()


import time
offset = -2
while True:
    #получить информацию по всем событиям (апдейтам)
    endPoint = f'https://api.telegram.org/bot{token}/getUpdates'
    param = {'offset': offset + 1}
    response = requests.get(endPoint, params=param).json()
    if response['result']:
        offset = response['result'][0]['update_id']
        userText = response['result'][0]['message']['text']
        chatID = response['result'][0]['message']['chat']['id']
        pprint.pprint(response)
        endPoint = f'https://api.telegram.org/bot{token}/sendMessage'
        params = {'chat_id': chatID, 'text': userText}
        res = requests.get(endPoint, params=params)
    time.sleep(1)

