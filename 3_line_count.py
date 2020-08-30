# SLS is just an object can use anything
count=0
fhand=open('test.txt','r')
for SLS in fhand:
      print(SLS.rstrip())

# print has its own \n i.e. enter the next line 
# and also in file there is entry in new line so two new line can be seen.

# To avoid this, we use rstrip function

print()
print()
fname=input("Enter the file name:")
fhand=open(fname,'r')
for line in fhand:
   line=line.rstrip()
   if line.startswith('My'):
      count=count +1
      print(line)
print(count)