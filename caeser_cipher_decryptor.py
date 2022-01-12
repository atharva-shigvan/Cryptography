#This is Cipher decryptor
#Note: Decrypted text will be in lowercase letters

print("Welcome!")
print("Enter the key for decryption: ")
k=int(input())
print("\nEnter Cipher text: ")
cipher=(input())
mesg=''
for i in range(len(cipher)):
	y=cipher[i]
	z=y.lower()
	if z==" ":
		mesg=mesg+' '
	elif y.isalpha():
		mesg=mesg+chr((ord(z)-k-97)%26+97)		#97 is unicode for letter 'a'
print("\nYour decrytped Message is: ")
print (mesg)
