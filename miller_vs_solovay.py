# -*- coding:utf8 -*-
# !/usr/bin/python python
from random import randrange, getrandbits
from timeit import timeit

def solovay_strassen(n, k=10):
    if n == 2:
        return True
    if not n & 1:
        return False


def legendre(a, p):
    if p < 2:
        raise ValueError('p must not be < 2')
    if (a == 0) or (a == 1):
        return a
    if a % 2 == 0:
        r = legendre(a / 2, p)
        if p * p - 1 & 8 != 0:
            r *= -1
    else:
        r = legendre(p % a, a)
        if (a - 1) * (p - 1) & 4 != 0:
            r *= -1
        return r

    for i in xrange(k):
        a = randrange(2, n - 1)
        x = legendre(a, n)
        y = pow(a, (n - 1) / 2, n)
        if (x == 0) or (y != x % n):
            return False
    return True


def miller_rabin(n, k=10):
    if n == 2:
        return True
    if not n & 1:
        return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in xrange(s - 1):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    s = 0
    d = n - 1

    while d % 2 == 0:
        d >>= 1
        s += 1

    for i in xrange(k):
        a = randrange(2, n - 1)
        if not check(a, s, d, n):
            return False
    return True


def compare_two_algorithms():
    a_mighty_big_integer = getrandbits(64)
    print "[INFO]Miller Rabin çalışma zamanı : %f \n" % timeit("miller_rabin(%d)" % a_mighty_big_integer,'from __main__ import miller_rabin', number=1000)
    print "[INFO]Solovay Strassen çalışma zamanı : %f \n" % timeit("solovay_strassen(%d)" % a_mighty_big_integer,'from __main__ import solovay_strassen', number=1000)
if __name__ == "__main__":
    compare_two_algorithms()