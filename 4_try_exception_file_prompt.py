fname=input("Enter a file you want to open:")
try:
    fhand=open(fname,'r')

except:
    print("Sorry file can not be opened.")
    quit()

for line in fhand:
    print(line)
