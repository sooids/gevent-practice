import gevent
from gevent.subprocess import Popen, PIPE


def cron():
    while True:
        print("cron")
        gevent.sleep(0.2)


if __name__ == "__main__":
    g = gevent.spawn(cron)
    sub = Popen(["sleep 1; uname"], stdout=PIPE, shell=True)
    out, err = sub.communicate()
    g.kill()
    print(out.rstrip())
