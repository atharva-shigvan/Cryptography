c=input("Enter the cipher text for decryption\n")	#ciphertext

k=input("Enter the key for decryption\n")	#cipherkey
num_key=[]   #text key converted to numeric num_key

if len(k)<=len(c):
	key=k.lower()
	for j in range(len(key)):
		key1=key[j]
		num_key.append(ord(key1)-97)
		
count=0
p=' '  #plaintext
for i in range(len(c)):
	char0=c[i]
	char=char0.lower()
	
	if char==" ":
		p=p+' '

	elif char.isdigit():	#digit characters remain same
		p=p+char
	
	elif char.isalpha():
		if count<len(num_key):
			key1=num_key[count]
			p=p+chr((ord(char)-key1-97)%26+97)	#97 is unicode for 'a'
			count=count+1
			if count==len(num_key):
				count=0
#RESULT
print("\nDecrypted plain text is: "+p)
