import requests
import pprint
with open('token.txt') as f:
    token = f.read()
#endpoint = 'https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getMe'
# endPoint = f'https://api.telegram.org/bot{token}/getMe'
# res = requests.get(endPoint).json()
# pprint.pprint(res)
endPoint = f'https://api.telegram.org/bot{token}/getUpdates'
res = requests.get(endPoint).json()
pprint.pprint(res)
chatID = []
for i in res['result']:
    chatID.append(i['message']['chat']['id'])

print(chatID)
endPoint = f'https://api.telegram.org/bot{token}/sendMessage'
for id in chatID:
    params = {'chat_id': id, 'text': "Привет!!"}
    res = requests.get(endPoint, params=params).json()
