#This is Cipher encryptor
#Note: Encrypted text will be in lowercase letters

print("Welcome!")
print("Enter the key for encryption: ")
k=int(input())
print("\nEnter Message: ")
mesg=(input())
cipher=''
for i in range(len(mesg)):
	y=mesg[i]
	z=y.lower()
	if z==" ":
		cipher=cipher+' '
	elif y.isalpha():
		cipher=cipher+chr((ord(z)+k-97)%26+97)		#97 is unicode for letter 'a'
print("\nYour encrytped Message is: ")
print (cipher)
