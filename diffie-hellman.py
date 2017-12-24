#-*- coding:utf8 -*-
#!/usr/bin/env python
from random import getrandbits
from random import randrange
from miller_vs_solovay import miller_rabin

def diffie_hellman():
    alice_key = 5
    bob_key = 3
    modulo = getrandbits(512)
    while not miller_rabin(int(modulo)):
        modulo = getrandbits(512)
    alpha = getrandbits(512)
    while not miller_rabin(int(alpha)) :
        if alpha<modulo and len(str(modulo)) == len(str(alpha)):
            break
        else:
            alpha = getrandbits(512)
    alice_enc = (alpha**alice_key)%modulo
    bob_enc = (alpha**bob_key)%modulo

    alice_convention = (bob_enc**alice_key)%modulo
    bob_convention = (alice_enc**bob_key)%modulo
    return alice_convention,bob_convention

if __name__ == "__main__":
    alice_convention,bob_convention= diffie_hellman()
    print "Alice'in uzlaştığı anahtar : %d \n" % alice_convention
    print "Bob'un uzlaştığı anahtar : %d \n" % bob_convention
    print "Eşleşme durumu : %s \n" % (alice_convention == bob_convention)




