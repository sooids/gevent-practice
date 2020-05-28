import gevent
from gv_actor import Actor


class Pinger(Actor):
    def receive(self, message):
        print(message)
        pong.inbox.put("ping")
        gevent.sleep(0)


class Ponger(Actor):
    def receive(self, message):
        print(message)
        ping.inbox.put("pong")
        gevent.sleep(0)


if __name__ == "__main__":
    ping = Pinger()
    pong = Ponger()

    ping.start()
    pong.start()

    ping.inbox.put("start")
    gevent.joinall([ping, pong])
