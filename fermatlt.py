#!/usr/bin/python
#-*- coding: utf8 -*-
import fractions
import random 
from sys import argv

def findA(primeNum):
    while True:
        a = int(random.randint(2, primeNum))
        check = fractions.gcd(a, primeNum)
        if check == 1:
            return a

def isPrime(a,p):
    print "[INFO] A sayisi: %d" %a
    if (pow(findA(p),p-1,p)) == 1:
        print "[OK] %d asal olabilir." %p
    else:
        print "[OK] %d asal degildir." %p

if __name__ == "__main__":
    if len(argv)<2:
        print "[ERR] Eksik argüman girildi!"
        print "[INFO] Doğru kullanım : python fermatlt.py <test edilecek sayi>"
        exit(1)
    p=int(argv[1])
    if p<3:
        print "[ERR] Girilen sayi 2den buyuk olmali!"
    isPrime(findA(p),p)

