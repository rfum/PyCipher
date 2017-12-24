#!/bin/python2
# -*- coding: utf-8 -*-
# Toprak Olga KESKİN, 1306160200
# Ramazan Furkan MATARACI, 1306151324 
import sys

# Özyinelemeyi sınırlandırıyoruz.
sys.setrecursionlimit(1000000)

# Özyineleme derinliği
depth=0

# En büyük ortak bölen
# Genişletilmiş Öklid Algoritması
# Return (g, t, s) a*t + b*s = gcd(t, s)
def ext_gcd(a,b):	

	global depth # Global tanımlanan derinliği kullanacağımızı belirtiyoruz.
	#print ("#Iter NO (%d) : Şuanki Durum, a=%d b=%d" % (depth,a,b))
	
	if a == 0:
		#print("#Iter NO (%d) : Return (b, 0, 1) : (%d,%d,%d)" % (depth,b,0,1))
		return (b, 0, 1)
	else:
		depth +=1 # Derinliği arttır
		g, t, s = ext_gcd(b % a, a)
		depth -=1 # Sonuç döndüğünde, derinliği düzelt
		
		#print("#Iter NO (%d) : Return (g, t, s): (%d,%d,%d) ve a=%d, b=%d" 
		#		% (depth,g, s - (b // a) * t, t, a, b))	
				
		return (g, s - (b // a) * t, t)

		
# Sonucu yazdır
if __name__ == "__main__":
	print "Sonuç: (g, t, s):(%d, %d, %d)" % (ext_gcd(87,55))


"""
Homeworkler : 
splice metodu
string sorting
"""

"""
kitaptan :
39
57
58
76

"""