# -*- coding: utf-8 -*-
# Ramazan Furkan MATARACI 1306151324
from string import ascii_lowercase
from string import lower
from sys import argv
class VigenereCipher():
	alphabet = ascii_lowercase
	size_of_alphabet = len(alphabet)
	def encrypt(self,plain_text,key_text):
		plain_text = lower(plain_text)
		key_text = lower(key_text)		
		cipher_text = ""
		size_of_key_text = len(key_text)
		size_of_plain_text = len(plain_text)
		for ind in range(size_of_plain_text):
			if plain_text[ind] != " ":
				cipher_text +=self.alphabet[(self.alphabet.index(plain_text[ind]) + 
				self.alphabet.index(key_text[ind%size_of_key_text]))%self.size_of_alphabet]
			else:
				continue
		return cipher_text

	def decrypt(self,cipher_text,key_text):
		cipher_text = lower(cipher_text)
		key_text = lower(key_text)
		size_of_key_text = len(key_text)
		size_of_cipher_text = len(cipher_text)
		plain_text = ""
		for ind in range(size_of_cipher_text):
			if cipher_text[ind] != " ":
				plain_text +=self.alphabet[(self.alphabet.index(cipher_text[ind]) - 
				self.alphabet.index(key_text[ind%size_of_key_text]))%self.size_of_alphabet]
			else:
				continue
		return plain_text
if __name__=="__main__":
	vigenere = VigenereCipher()
	if len(argv) < 3:
		print "[ERR] Eksik parametreler var!"
		print "[INFO] Doğru kullanım : python vigenere.py <metin> <metin(anahtar)>"
		exit(1)
	text = argv[1]
	key = argv[2]
	encrypted = vigenere.encrypt(text,key)
	decrypted = vigenere.decrypt(encrypted,key)
	print "[INFO] Şifrelenecek Metin : %s" % text
	print "[INFO] Alfabe : %s" % vigenere.alphabet
	print "[INFO] Alfabe Boyutu : %d" % vigenere.size_of_alphabet
	print "[OK] Şifreli Metin : %s" % encrypted
	print "[OK] Deşifre Edilmiş Metin : %s" % decrypted
