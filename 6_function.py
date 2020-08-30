#No argument
def func1():
    print("I am a function")

func1()  #prints the value
print(func1())  #prints the value through func1() and then python constant NONE as func1() does not retun a value

#With argument
def func2(a):
    return("The cube of the given value is " + str(a**3))

func2(4)
print(func2(4))

#multiple argument
def add(*args):
    sum=0
    for x in args:
        sum=sum + x
    return sum

print(add(1,2,3,4,5))


####
def inc(a,b=1):
    return(a+b)
a=inc(1)
a=inc(a,a)
print(a)