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

my_list=[2,4,5]

result=[[x] for x in my_list]
print(result)

result=[[x+i] for x in my_list for i in range(3)]
print(result)

result=[[x+i for x in my_list] for i in range(3)]
print(result)
