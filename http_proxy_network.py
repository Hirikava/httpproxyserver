import asyncio
from singltone import singleton
from http_proxy_connection_maneger import HttpProxyConnectionManeger
import socket

async def connection_handler(reader,writer):
    transport = reader._transport
    socket = transport._extra['socket']
    HttpProxyConnectionManeger().add_connection(socket)



@singleton
class HttpProxyTransport(asyncio.Transport):
    def __init__(self,port = 8080):
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.bind(('',port))



