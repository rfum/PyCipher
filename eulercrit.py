#!/usr/bin/python
#-*- coding: utf8 -*-
from sys import argv
import fermatlt

def eulerCrit(a,p):
    if pow(a,(p-1)/2,p) == 1:
        print "[OK] {} sayisi, {} sayisi icin quadratic residue'dir!".format(a, p)
    else:
        print "[INFO] {} sayisi, {} sayisi icin quadratic residue degildir!".format(a, p)

if __name__ == "__main__":
    p=int(argv[1])
    a=int(argv[2])
    if len(argv)<3:
        print "[ERR] Eksik argüman girildi!"
        print "[INFO] Doğru kullanım : python eulercrit.py <test edilecek asal sayi> <test edilecek quadratic residue>"
        exit(1)
    if p<3:
        print "[ERR] p sayisi 3'ten kucuk bir asal sayi(even prime) olamaz!"
        exit(1)
    if a>p:
        print "[ERR] test edilecek quadratic residue, test edilecek asal sayidan buyuk olamaz!"
        exit(1)
    if fermatlt.isPrime(fermatlt.findA(p),p) == 1:
        eulerCrit(a, p)
        exit(1)
    if fermatlt.isPrime(fermatlt.findA(p),p) == -1:
        print "[ERR] p sayisi asal olmak zorunda!"
        exit(1)
