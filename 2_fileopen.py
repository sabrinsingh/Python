
count=0
fhand=open('test.txt','r')
for SLS in fhand:
   if SLS.startswith('My'):
      count=count +1
      print(SLS)
   print(SLS , end = " ")
print(count)