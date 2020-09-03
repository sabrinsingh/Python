# Dictionary is a set of key-value pair
# For e.g., a person has many attributes such as name, age, dpb, etx

sabrin={
    # key: value
    "firstName" : "Sabrin",
    "lastName"  : "Singh",
    "dob"       : "2-2-1990",
    "email"     : "sabrinsingh@email.com"
}

print(sabrin)
print(type(sabrin))
print(sabrin["firstName"], sabrin["email"])

# adding to the dictionary
sabrin["phone"]="9840052920"
print(sabrin)

#Loop inside the dictionary
for i in sabrin:
    print(i) #This gives keys only

print()

# for the keys and value 
for i in sabrin.values():
        print(i)   #This gives values only
print()

# for the keys and value 
for i in sabrin:
        print(f"{i} : {sabrin[i]}") #"f" helps to write the variables inside the string


      