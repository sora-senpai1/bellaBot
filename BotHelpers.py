import websocket
import requests
import amino
import json


class Helper:
    def __init__(self, headers, client=None, sub=None, amino=None):
        self.headers = headers
        self.url = "wss://ws1.narvii.com"
        self.api = 'https://service.narvii.com/api/v1/'
        self.chat = '/s/chat/thread/'
        self.client = client
        self.amino = amino

    def start_vc(self, comId: str, chatId: str, joinType: int = 1):
        websocket.enableTrace(True)
        ws = websocket.WebSocket()
        ws.connect(self.url, header=self.headers)
        data = {
            "o": {
                "ndcId": comId,
                "threadId": chatId,
                "joinRole": joinType,
                "id": "2154531"
            },
            "t": 112
        }
        data = json.dumps(data)
        ws.send(data)
        data = {
            "o": {
                "ndcId": comId,
                "threadId": chatId,
                "channelType": 1,
                "id": "2154531"
            },
            "t": 108
        }
        data = json.dumps(data)
        ws.send(data)

    def end_vc(self, comId = None, chatId = None):
        websocket.enableTrace(True)
        websockets = websocket.WebSocket()
        websockets.connect(self.url, header=self.headers)
        data = {
            "o": {
                "ndcId": comId,
                "threadId": chatId,
                "joinRole": 2,
                "id": "2154531"  # Need to change?
            },
            "t": 112
        }
        data = json.dumps(data)
        websockets.send(data)
        websockets.close()

    def send_message(self, comId: str, chatId: str, message: str, type: int = 0):
        data = {
            'content': message,
            'type': type,
        }
        data = json.dumps(data)
        r = requests.post(url=f'{self.api + comId + self.chat + chatId}/message', data=data, headers=self.headers).text
        request = json.loads(r)
        return request

    def setCom(self, comId: str):
        self.sub = amino.SubClient(comId=comId, profile=self.client.profile)
