# 1. A Caesar Cipher (or Cipher Wheel) is an ancient mechanism for encrypting text and a popular children's toy.
# It encrypts a message by shifting each alphabetic character in the text by a fixed amount. 
# For example, a Caesar cipher with a shift of 4 translates a to e, b to f etc.
#             abcdefghijklmnopqrstuvwxyz
#             efghijklmnopqrstuvwxyzabcd  
# and would encrypt helloworld as lippsasvph.
# Write a program in python that would, covert a string into Caesar cipher.

str="abcdefghijklmnopqrstuvwxyz"
print(str[0])
print(len(str))
print(ord('a'))   #97
print(ord('A'))   #65
print(ord('z'))   #122
print(ord('Z'))   #90
result=''
for i in range(len(str)):
    char= str[i]

    print(char, end='')
    if(char.isupper()):
        result += chr((ord(char) + 4-65) % 26 + 65)
    else:
        result += chr((ord(char) + 4- 97) % 26 + 97)    
print(result)