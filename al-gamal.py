# -*- coding:utf8 -*-
from sys import getsizeof
from miller_vs_solovay import miller_rabin
from random import getrandbits
from lin_cong import lin_cong


def key_pair_generation(alpha, p):
    privkey = getrandbits(512)
    while not privkey < p:
        privkey = getrandbits(512)
    pubkey = pow(alpha,privkey,p)
    return privkey, pubkey


def encrypt(p=2579, alpha=2, privkey=765, k=853, msg=1299):
    p = getrandbits(512)
    while not miller_rabin(p):
        p = getrandbits(512)
    alpha = getrandbits(512)
    while not miller_rabin(alpha):
        alpha = getrandbits(512)
    privkey, pubkey = key_pair_generation(alpha, p)
    k = getrandbits(512)
    cipher1 = pow(alpha,k,p) # k sabit olursa sniffer k'yı tahmin edip cipher1'i çözebilir
    cipher2 = msg * pow(pubkey,k,p)  # k oscar tarafından bilindği vakit cipher2'de çözülür
    return cipher1, cipher2, privkey, p


def decrypt(cipher1, cipher2, privkey, p):
    return (cipher2 * lin_cong(pow(cipher1,privkey,p), 1, p)) % p


if __name__ == "__main__":
    plain = 16283516823
    cipher1, cipher2, privkey, p = encrypt(msg=plain)
    print "Şifrelenecek Mesaj : %d" % plain
    print "p € Zp* : %d" % p
    print "Gizli anahtar : %d" % privkey
    print "Şifreli mesaj 1 : %d" % cipher1
    print "Şifreli mesaj 2 : %d" % cipher2
    plain = decrypt(cipher1, cipher2, privkey, p)
    print "Deşifre edilmiş mesaj : %d" % plain
