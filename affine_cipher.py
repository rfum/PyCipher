
# -*- coding: utf-8 -*-
# Ramazan Furkan MATARACI, 1306151324
# Toprak KESKIN, 1306160200
from string import ascii_uppercase
from ext_gcd import ext_gcd
from sys import argv
from fractions import gcd
class AffineCipher():

	letters = ascii_uppercase
	quantity_of_letters = len(letters)

	@classmethod
	def encrypt(self, plain_text, a, b):
		plain_text=str(plain_text)
		plain_text=plain_text.upper()
		cipher_text = ""
	
		for letter in plain_text:
			if letter != ' ':
				cipher_text+=self.letters[(a*self.letters.index(letter) + b)%self.quantity_of_letters]
			else:
				continue

		return cipher_text

	@classmethod
	def decrypt(self, cipher_text, a, b):
		cipher_text=str(cipher_text)
		cipher_text=cipher_text.upper()
		plain_text = ""
		for letter in cipher_text:
			if letter != " ":
				g,t,s = ext_gcd(a, self.quantity_of_letters)
				inverse = t%self.quantity_of_letters
				index = (inverse*(self.letters.index(letter)-b))%self.quantity_of_letters
				plain_text+=self.letters[index]
			else:
				continue
		return plain_text
if __name__=="__main__":
	if len(argv) < 4:
		print "[ERR] Eksik parametreler var!"
		print "[INFO] Doğru kullanım : python affine_cipher.py <metin> <tamsayı(anahtar1)> <tamsayı(anahtar2)"
		exit(1)
	text = argv[1]
	k1,k2 = argv[2:]
	k1,k2 = int(k1),int(k2)
	print "[INFO] Alfabe : %s" % AffineCipher.letters
	print "[INFO] Alfabe Boyutu : %d" % AffineCipher.quantity_of_letters
	if gcd(k1,26) != 1:
		print "[ERR] İlk Anahtar Alfabe Boyutuyla Aralarında Asal Olmalı!"
		exit(1)
	encrypted = AffineCipher.encrypt(text, k1,k2)
	decrypted = AffineCipher.decrypt(encrypted, k1, k2)
	print "[INFO] Şifrelenecek Metin : %s" % text.upper()
	print "[OK] Şifreli Metin : %s" % encrypted
	print "[OK] Deşifre Edilmiş Metin : %s" %  decrypted



