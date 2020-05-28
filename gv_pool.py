from gevent.pool import Pool

pool = Pool(2)


def hello_from(n):
    print("Size of pool %s" % len(pool))


if __name__ == "__main__":
    pool.map(hello_from, range(3))
