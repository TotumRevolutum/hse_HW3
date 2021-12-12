import numpy as np


def maxi(numb):
    if len(numb) >= 1:
        maxi = numb[0]
    else:
        return 'error'
    for i in numb:
        if i > maxi:
            maxi = i
    return maxi


def mini(numb):
    if len(numb) >= 1:
        mini = numb[0]
    else:
        return 'error'
    for i in numb:
        if i < mini:
            mini = i
    return mini


def summa(numb):
    s = 0
    for i in numb:
        s += i
    return s


def multi(numb):
    s = 1
    for i in numb:
        try:
            s *= i
            print(s, i)
        except MemoryError:
            print('!')
            raise
    return s


def open_file(name):
    f = open(name, 'r')
    numb = []
    lines = [line.strip().split() for line in f]
    for i in lines:
        for j in i:
            try:
                numb.append(int(j))
            except ValueError:
                raise
    f.close()
    return numb
