# On Unix: Access with ``$ nc 127.0.0.1 5000``
# On Window: Access with ``$ telnet 127.0.0.1 5000``

from gevent.server import StreamServer


def handle(socket, address):
    socket.send(b"Hello from a telnet!\n")
    for i in range(5):
        socket.send((str(i) + "\n").encode())
    socket.close()


if __name__ == "__main__":
    server = StreamServer(("127.0.0.1", 5000), handle)
    server.serve_forever()
