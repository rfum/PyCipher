# -*- coding:utf-8 -*-

from random import sample
from string import ascii_lowercase,lower
from sys import argv
class SubsitutionCipher():
    letters = ascii_lowercase
    letters_shuffled = "".join(sample(letters,len(letters)))
    quantity_of_letters = len(letters)
    def encrypt(self,plain_text):
        plain_text=str(plain_text)
        plain_text=plain_text.lower()
        cipher_text = ""
        for letter in plain_text:
            if letter != " ":
                cipher_text += self.letters_shuffled[self.letters.index(letter)]
            else:
                continue
        return cipher_text
    def decrypt(self,cipher_text):
        cipher_text = str(cipher_text)
        cipher_text = cipher_text.lower()
        plain_text = ""
        for letter in cipher_text:
            plain_text += self.letters[self.letters_shuffled.index(letter)]
        return plain_text
if __name__=="__main__":
    subs = SubsitutionCipher()
    if len(argv) < 2:
        print "[ERR] Eksik parametreler var!"
        print "[INFO] Doğru kullanım : python sub_cipher.py <metin>"
        exit(1)
    text = argv[1]
    encrypted = subs.encrypt(text)
    decrypted = subs.decrypt(encrypted)
    print "[INFO] Şifrelenecek Metin : %s" % text
    print "[INFO] Alfabe : %s" % subs.letters
    print "[INFO] Alfabe Boyutu : %d" % subs.quantity_of_letters
    print "[OK] Şifreli Metin : %s" % encrypted
    print "[OK] Deşifre Edilmiş Metin : %s" %  decrypted


