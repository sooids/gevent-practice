import socket

print(socket.socket)

print("After monkey patch")
from gevent import monkey  # noqa: E402

monkey.patch_socket()
print(socket.socket)

import select  # noqa: E402

print(select.select)
monkey.patch_select()
print("After monkey patch")
print(select.select)
