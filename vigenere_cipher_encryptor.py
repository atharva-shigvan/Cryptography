p=input("Enter the plain text for encryption\n")	#plaintext

k=input("Enter the key \n")	#cipherkey
num_key=[]	#textkey converted to numeric key

if len(k)<=len(p):
	key=k.lower()
	for j in range(len(key)):
		key1=key[j]
		num_key.append(ord(key1)-97)  #97 is unicode for 'a'

count=0 
c=' '	#ciphertext
for i in range(len(p)):
	char0=p[i]
	char=char0.lower()
	
	if char==" ":	#space
		c=c+' '
		
	elif char.isdigit():	#digit characters remain same
		c=c+char
	
	elif char.isalpha():
		if count<len(num_key):
			key1=num_key[count]
			c=c+chr((ord(char)+key1-97)%26+97)	#97 is unicode for 'a'
			count=count+1
			if count==len(num_key):
				count=0
#RESULT
print("\nEncrypted cipher text is: "+c)
