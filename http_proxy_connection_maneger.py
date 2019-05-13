from singltone import singleton
import select
import asyncio
import socket

@singleton
class HttpProxyConnectionManeger():
    def __init__(self):
        self.connections = dict()

    def add_connection(self,transport):
        self.connections[transport] = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connections[transport].bind(('',0))
        self.connections[self.connections[transport]] = transport

    async def handle_connections(self):
        while True:
            rlist = self.connections.values()
            if(len(rlist) > 0):
                readable,writeable,exceptional = select.select(rlist,rlist,rlist)
                for rsocket in writeable:
                    data = await asyncio.get_event_loop().sock_recv(rsocket,1024)
                    print(data)
            await asyncio.sleep(0.2)
