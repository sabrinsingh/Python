# SLS is just an object can use anything
count=0
fhand=open('test.txt','r')
for SLS in fhand:
   if SLS.startswith('My'):
      count=count +1
      print(SLS)
   print(SLS)
print(count)


# print has its own \n i.e. enter the next line 
# and also in file there is entry in new line so two new line can be seen.

# To avoid this, we use rstrip function....check file number 3
