# -*-coding:utf8
# !/usr/bin/env python

import fractions
from random import getrandbits, randrange
import ext_gcd #genişletilmiş öklid teoremi
from miller_vs_solovay import miller_rabin

# p ve q asallarını miller-rabin yardımıyla üretirler
def prime_generator():
    p = 0
    q = 0
    while not miller_rabin(int(p)):
        p = getrandbits(512)
    while not miller_rabin(int(q)):
        q = getrandbits(512)
    return p,q
#mesajı şifreler
def encrypt(key, plain, n):
    return pow(plain,key,n)

#şifreli mesajı açar
def decrypt(key, cipher, n):
    return pow(cipher , key, n)

#umumi ve özel anahtar üretir
def key_pair_generation(p=17, q=13):
    n = p * q
    toitent = (p - 1) * (q - 1)
    pubkey = randrange(1, toitent)
    g = fractions.gcd(pubkey, toitent)#phi ile umumi anahtar aralarında asal mı?
    while g != 1: #değilse olana kadar üret
        pubkey = randrange(1, toitent)
        g = fractions.gcd(pubkey, toitent)
    privkey = ext_gcd.ext_gcd(pubkey, toitent) #umumi anahtarın tersi
    if privkey[1] < 0:
        return pubkey, privkey[1] + toitent, n
    else:
        return pubkey, privkey[1], n


if __name__ == "__main__":
    p,q = prime_generator()
    pubkey, privkey, n = key_pair_generation(p, q)
    plain = 16386152631873 #şifrelenecek mesaj
    print "p : %d" % p
    print "q : %d" % q
    print "toitent : %d " % ((q - 1) * (p - 1))
    print "açık anahtar : %d " % pubkey
    print "kapalı anahtar : %d " % privkey
    print "n : %d " % n
    print "Temiz mesaj : %d" % plain
    cipher = encrypt(pubkey, plain, n)
    print "Şifreli mesaj : %d " % cipher
    plain = decrypt(privkey, cipher, n)
    print "Çözülen mesaj : %d" % plain
