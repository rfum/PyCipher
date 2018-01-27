#!/usr/bin/python
#-*- coding: utf8 -*-
from sys import argv
import eulercrit
import fermatlt
import argparse

def legendreSymbol(integer,prime):
    if eulercrit.eulerCrit(integer, prime) == 1:
        return 1
    if (a%p == 0):
        return 0
    if eulercrit.eulerCrit(integer, prime) == -1:
        return -1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=
    "Legendre Sembolu Python2.7 uygulamasi")
    parser.add_argument("-p", "-P", "--prime", help="test edilecek asal moduler ust sinir", required="True")
    parser.add_argument("-a", "-A", "--integer", help="test edilecek quadratic residue", required="True")
    args = parser.parse_args()
    a=int(args.integer)
    p=int(args.prime)
    if p<3:
        print "[ERR] p sayisi 3'ten kucuk bir asal sayi(even prime) olamaz!"
        exit(1)
    if fermatlt.isPrime(fermatlt.findA(p),p) == 1:
            if legendreSymbol(a,p) == 1:
                print "[OK] 1".format(a, p)
                exit(1)
            elif legendreSymbol(a,p) == -1:
                print "[OK] -1".format(a, p)
                exit(1)
            elif legendreSymbol(a,p) == 0:
                print "[OK] 0".format(a,p)
                exit(1)
    elif fermatlt.isPrime(fermatlt.findA(p),p) == -1:
        print "[ERR] p sayisi asal olmak zorunda!"
        exit(1)
