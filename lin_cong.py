#!/usr/bin/python3.5
#-*-coding:utf8-*-

from ext_gcd import ext_gcd
# gcd m a = 1

def lin_cong(a,b,m):
    g,t,s = ext_gcd(a,m)
    inverse = t%m
    if g==1:
        #print("Bütün çözümler birbirine eşittir.")
        #print("gcd(a,m) = 1")
        #print("ters = a' mod(m) ->  %d' mod (%d) = %d" % (a, m, inverse))
        #print("ters*b mod(m) = x -> (%d*%d) mod (%d)" % (inverse, b, m))
        #print("x = %d" % ((inverse*b)%m))
        return (inverse*b)%m
    else:
        print("En büyük ortak bölen(%d) kadar çözüm vardır." % (g) )
        return None
if __name__ == "__main__":
    lin_cong(11,1,26)
