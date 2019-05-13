import asyncio
import socket
from  http_proxy_network import HttpProxyProto,HttpProxyTransport

loop = asyncio.get_event_loop()
coro = loop.create_server(HttpProxyProto(),sock=HttpProxyTransport().socket)
server = loop.run_until_complete(coro)
loop.run_forever()
