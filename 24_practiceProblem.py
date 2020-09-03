# Separate the number from the string, then add each number and show the result. A
# Also, return the remaining string character

inp=input("Please enter a string : ")
numTotal=0
num=[]
chars=''

for char in inp:
    if(char.isdigit()):
        num.append(char)
        numTotal += int(char)
    else:
        chars+=char 
print(num)
print(numTotal)
print(chars)

