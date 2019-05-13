import asyncio
from  http_proxy_network import connection_handler,HttpProxyTransport
from http_proxy_connection_maneger import HttpProxyConnectionManeger

loop = asyncio.get_event_loop()
coro = asyncio.start_server(connection_handler,sock=HttpProxyTransport().socket,loop=loop)
server = loop.run_until_complete(coro)
loop.run_until_complete(loop.create_task(HttpProxyConnectionManeger().handle_connections()))

