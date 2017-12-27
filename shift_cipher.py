#!/usr/bin/env python
#-*- coding: utf8 -*-
from string import upper,ascii_uppercase
from sys import argv
class ShiftCipher():
    letters = ascii_uppercase
    quantity_of_letters = len(letters)

    def encrypt(self,plain_text,key):
        plain_text = str(plain_text)
        plain_text = plain_text.upper()
        self.letters=ascii_uppercase
        self.quantity_of_letters=len(self.letters)
        cipher_text= ""
        for letter in plain_text:
            cipher_text+=self.letters[(self.letters.index(letter)+key)%self.quantity_of_letters]
        return cipher_text;
    def decrypt(self,cipher_text,key):
        cipher_text= str(cipher_text)
        cipher_text= cipher_text.upper()
        plain_text = ""
        for letter in cipher_text:
            plain_text +=self.letters[(self.letters.index(letter)-key)%self.quantity_of_letters]
        return plain_text

if __name__=="__main__":
    cipher=ShiftCipher()
    if len(argv) < 3:
        print "[ERR] Şifrelenecek metin girilmedi!"
        print "[INFO] Doğru kullanım : python shift_cipher.py <metin>"
        print "[INFO] Doğru kullanım : python shift_cipher.py <metin> <tamsayı(anahtar1)>"
        exit(1)
    text = argv[1]
    key = int(argv[2])
    print "[INFO] Alfabe : %s" % cipher.letters
    print "[INFO] Alfabe Boyutu : %d " % cipher.quantity_of_letters
    print "[INFO] Şifrelenecek metin : %s " % text
    encrypted = cipher.encrypt(text,key)
    print "[OK] Şifreli Metin : %s " % encrypted
    decrypted = cipher.decrypt(encrypted,key)
    print "[OK] Deşifre Edilmiş Metin : %s "  % decrypted



