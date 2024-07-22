import json
from channels.generic.websocket import WebsocketConsumer

class MarketConsumer(WebsocketConsumer):

    def connect(self):
       
        self.accept()
        self.send(text_data=json.dumps({"message_from_server":"hello"}))
        # self.accept("subprotocol")
        # self.close()
    def disconnect(self, close_code):
        pass

    def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        print(text_data_json) 
       

   