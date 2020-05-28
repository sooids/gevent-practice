import gevent.monkey

gevent.monkey.patch_socket()

import gevent  # noqa: E402
from urllib.request import urlopen  # noqa: E402
import simplejson as json  # noqa: E402


def fetch(pid):
    response = urlopen("https://worldtimeapi.org/api/timezone/Asia/Seoul")
    result = response.read()
    json_result = json.loads(result)
    datetime = json_result["datetime"]

    print("Process %s: %s" % (pid, datetime))
    return json_result["datetime"]


def synchronous():
    for i in range(1, 10):
        fetch(i)


def asynchronous():
    threads = []
    for i in range(1, 10):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)


if __name__ == "__main__":
    print("Synchronous:")
    synchronous()

    print("Asynchronous:")
    asynchronous()
