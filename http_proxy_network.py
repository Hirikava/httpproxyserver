import asyncio
from singltone import singleton
import socket

@singleton
class HttpProxyProto(asyncio.Protocol):
    def __init__(self):
        asyncio.BaseProtocol.__init__(self)

    def connection_made(self, transport):
        print(transport)

    def data_received(self, data):
        print(data)

    def __call__(self, *args, **kwargs):
        return self



@singleton
class HttpProxyTransport():
    def __init__(self,port = 8080):
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.bind(('',port))


