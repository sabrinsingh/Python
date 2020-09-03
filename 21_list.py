fruits= ['apple', 'mango','banana','grape']
print(fruits)

# remove from the list as per index
fruits.pop(0)
print(fruits)

#append the value to list
fruits.append('orannge')
print(fruits)


#To add the fruit name to the list until user stops

quit= False
while not quit:
    inp=input("Enter y to add more fruits and n to quit : y" ).lower()
    if(inp == 'y'):
        fruitname=input("Enter the name of fruit : ")
        fruits.append(fruitname)
    elif(inp == 'n'):
        print("Thank you!!!")
        quit = True
    else:
        print("Invalid Entry!!!! Please try again")


fruits.sort()
print(fruits)


