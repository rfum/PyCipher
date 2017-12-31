#!/usr/bin/python
#-*- coding: utf8 -*-
from sys import argv

def eulerCrit(a,p):
    if pow(a,(p-1)/2,p) == 1:
        print "[OK] {} sayisi, {} sayisi icin quadratic residue'dir!".format(a, p)
    else:
        print "[INFO] {} sayisi, {} sayisi icin quadratic residue degildir!".format(a, p)

if __name__ == "__main__":
    if len(argv)<3:
        print "[ERR] Eksik argüman girildi!"
        print "[INFO] Doğru kullanım : python eulercrit.py < test edilecek asal sayi> <test edilecek quadratic residue>"
        exit(1)
    if argv[1]<3:
        print "[ERR] p sayisi 2 olamaz!"
    p=int(argv[1])
    a=int(argv[2])
    eulerCrit(a, p)
