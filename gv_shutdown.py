import gevent
import gevent.signal
import signal


def run_forever():
    gevent.sleep(1000)


if __name__ == "__main__":
    gevent.signal.signal(signal.SIGQUIT, gevent.kill)
    thread = gevent.spawn(run_forever)
    thread.join()
