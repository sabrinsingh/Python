my_list=['x','y','z']
print(my_list)

result=[x for x in my_list]
print(result)

# How it works
result=[]
for x in my_list:
    result.append(x)
print(result)    

result = [x*i for x in my_list for i in range(1,4)]
print(result)


# How it works
result=[]
for x in my_list:
    for i in range(1,4):
        result.append(x*i)
print(result)   

result = [x*i for x in my_list for i in range(1,4)]
print(result)

result = [x*i for i in range(1,4) for x in my_list]
print(result)

my_list=[2,3,4]

result=[[x] for x in my_list]
print(result)

result=[[x+i] for x in my_list for i in range(3)]
print(result)

result=[[x+i for x in my_list] for i in range(3)]
print(result)


f=input("First : ")
s=input("Second : ")
o=input("Operation : ")
print(f + o + s + " = " ,eval(f + o + s))



for i in range(2, 10, 2):    
    print(i, end=', ')

print([x for x in range(2,10,2)])
