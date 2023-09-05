# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 00:29:30 2023

@author: saksh
"""

letters = 'abcdefghijklmnopqrstuvwxyz '
num_letters = len(letters)

def encrypt(plaintext,key):
    ciphertext = ''
    for letter in plaintext:
        letter = letter.lower()
        index = letters.find(letter)
        if index == -1:
            ciphertext += letter
        else:
            new_index = index + key
            if new_index >= num_letters:
                new_index -= num_letters 
            ciphertext += letters[new_index]
    return ciphertext

def decrypt(ciphertext,key):
    plaintext = ''
    for letter in ciphertext:
        letter = letter.lower()
        index = letters.find(letter)
        if index == -1:
            plaintext += letter
        else:
            new_index = index - key
            if new_index < 0:
                new_index += num_letters 
            plaintext += letters[new_index]
    return plaintext

            
print()
print("*********Ceaser Cipher************")
print()

print("Do you want to encrypt or decrypt " )
user_input = input("encrypt/decrypt : ").lower()
print()

if user_input == 'e':
    print("Encryption Mode")
    print()
    key = int(input("Enter the key to encrypt : "))
    text = input("Enter a text to encrypt : ")
    ciphertext = encrypt(text, key)
    print("Cipher text : ",ciphertext )
elif user_input == 'd':
    print("Decryption Mode")
    print()
    key = int(input("Enter the key to decrypt : "))
    text = input("Enter a text to decrypt : ")
    plaintext = decrypt(text, key)
    print("Plain text : ",plaintext )
else:
    pass
    
    