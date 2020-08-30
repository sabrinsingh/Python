a=input("Enter a number to check if its prime or not: ")
print(a)
a=int(a)
c=1

for i in range(2,a):
    if (a % i==0):
        c=0
if(c==0):
    print("Not a prime number")
else:
    print("A prime number") 

#if elif else

#Simple Python supporting conditional statement
st="a is lesser then 5" if (a<5) else "a =5"
print(st)