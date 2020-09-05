# WAP to show [1,9,25]
# This is the square of the order number

result=[x**2 for x in range(6) if x%2!=0]
print(result)

# How it works behind the scene
result=[]
for x in range(6):
    if(x % 2 !=0):
        result.append(x**2)

print(result)