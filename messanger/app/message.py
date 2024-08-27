import django
django.setup()
from channels.consumer import AsyncConsumer
from .models import Message, User, Chat
import json
from asgiref.sync import sync_to_async


class Message(AsyncConsumer):

    async def websocket_connect(self, event):
        await self.send({"type": "websocket.accept"})



    @sync_to_async
    def websocket_receive(self, text_data):
        d = json.loads(text_data['text'])

        if d['message'] == 'list': #срабатывает каждую секунду
           # mess = Message.objects.filter(chat=Chat.objects.filter(id=d['chat']).first())
            #self.send(text_data="Hello world!")
            self.send({
            #    "type": "websocket.send",
                "text": "Hello from Django socket11111"
            })
        else: #срабатывает при отправке сообщения в чате
            m = Message()
            m.text = d['message']
            m.chat = Chat.objects.filter(id=d['chat']).first()
            m.user = User.objects.filter(login=d['user']).first()
            m.save()



    async def websocket_disconnect(self, event):
        pass