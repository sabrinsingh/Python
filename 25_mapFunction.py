def square(x):
    return x*x

num=[1,2,3,4,5,6]

a=list(map(square,num))
print(a)

b=list(map(lambda x: x*x,num))
print(b)