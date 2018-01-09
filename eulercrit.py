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
    if len(argv)<3:
        print "[ERR] Eksik parametreler var!"
        print "[INFO] Doğru kullanım : python eulercrit.py <asal moduler ust sinir> <quadratic residue>"
        print "[INFO] Istege Bagli : python eulercrit.py [--list|-l] <moduler ust sinir>"
        exit(1)
    if (argv[1]=="--list" or argv[1]=="-l"):
        p=int(argv[2])
        i=0
        j=0
        primeSquaredList= []
        uniqueList = []
        if p<2:
            print "Girilen sayi icin quadratic residue bulunmamaktadir."
            exit(1)
        for num in range(1,p):
            primeSquaredList.append(pow(num,2,p))
            if ((primeSquaredList[i] not in uniqueList) and primeSquaredList[i] != 0):
                uniqueList.append(primeSquaredList[i])
                j=j+1
            i=i+1
        uniqueList = sorted(uniqueList)
        print ", ".join([str(x) for x in uniqueList])
        exit(1)
    p=int(argv[1])
    a=int(argv[2])
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
