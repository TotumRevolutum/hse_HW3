from main import *
import time


def test_short():
    start = time.time()
    multi(open_file('text.txt'))
    end = time.time()
    return end - start


def test_long():
    start = time.time()
    multi(open_file('text2.txt'))
    end = time.time()
    return end - start


print(test_short())
print(test_long())
