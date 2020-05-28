import time


def echo(i):
    time.sleep(0.001)
    return i


# Non Deterministic Process Pool
def t1():
    from multiprocessing.pool import Pool  # noqa: E402

    p = Pool(10)
    run1 = [v for v in p.imap_unordered(echo, range(10))]
    run2 = [v for v in p.imap_unordered(echo, range(10))]
    run3 = [v for v in p.imap_unordered(echo, range(10))]
    run4 = [v for v in p.imap_unordered(echo, range(10))]

    print(run1 == run2 == run3 == run4)
    print(run1)
    print(run2)


# Deterministic Gevent Pool
def t2():
    from gevent.pool import Pool  # noqa: E402

    p = Pool(10)
    run1 = [v for v in p.imap_unordered(echo, range(10))]
    run2 = [v for v in p.imap_unordered(echo, range(10))]
    run3 = [v for v in p.imap_unordered(echo, range(10))]
    run4 = [v for v in p.imap_unordered(echo, range(10))]

    print(run1 == run2 == run3 == run4)
    print(run1)
    print(run2)


if __name__ == "__main__":
    t1()
    t2()
