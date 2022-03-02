#!/usr/bin/sh
echo "##.....Cryptography.....##"
echo "Select type of cipher: "
echo "1- Caeser"
echo "2- Vigenere"
echo "Any other to exit"
read -p 'Option: ' a

if  [[ $a -eq 1 ]];
	then
	printf "\n"
	echo "##  Caeser cipher  ##"
	echo "Select any one option: "
	echo "1- Encrypting Text"
	echo "2- Decrypting Text"
	read -p 'Choice: ' b
		if [[ $b -eq 1 ]];
		then
		printf "\n"
		python3 caeser_cipher_encryptor.py
		elif [[ $b -eq 2 ]];
		then
		printf "\n"
		python3 caeser_cipher_decryptor.py
		else
		printf "\n"
		echo "Error!"
		fi
		
elif [[ $a -eq 2 ]];
	then
	printf "\n"
	echo "##  Vigenere cipher  ##"
	echo "Select any one option: "
	echo "1- Encrypting Text"
	echo "2- Decrypting Text"
	read -p 'Choice: ' c
		if [[ $c -eq 1 ]];
		then
		printf "\n"
		python3 vigenere_cipher_encryptor.py
		elif [[ $c -eq 2 ]];
		then
		printf "\n"
		python3 vigenere_cipher_decryptor.py
		else
		printf "\n"
		echo "Error!"
		fi
	else
	sleep 0.5
	clear
	echo "Exiting."
	sleep 0.5
	clear
	echo "Exiting.."
	sleep 0.5
	clear
	echo "Exiting..."
	sleep 0.5
	clear
	echo "Exiting...."
	sleep 0.5
	clear
	echo "Exiting....."
fi








