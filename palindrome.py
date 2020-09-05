#refer
def checkpalindrome(inp):
    rev=(inp[::-1])
    if(inp==rev):
        return "This is a palindrome."
    else:
        return "Not a palindrome"    


inp=input("Enter anything to check if its palindrome : ")
print(checkpalindrome(inp))



# <object_name>[<start_index>, <stop_index>, <step>]

a = '12345'
print(a[::2]) #from 1st to last with the step of 2

a = '12345'
print(a[::-2]) #from last to first with the step of 2



a = '1234'
print(a[3:0:1]) 


a = '1234'
print(a[3:0:-2]) #from 3rd index to 1 as it exclude last stop value i.e. 0 here .

# <object_name>[<start_index>, <stop_index>, <step>]
# Here a=obj_name, 3 = start_index, = =stop_index , step=2