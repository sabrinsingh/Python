class myClass():

    def method1(self):
        print("First method")
    
    def method2(self, str):
        print("self is similar to \"this\" and this is the second string :" + str)

class myAnotherClass():
    def method1(self):
        print("First method")
    
    def method2(self, str):
        print("self is similar to \"this\" and this is the second string from myAnotherClass :" + str)

    

class otherClass():
    def __init__(self, fname, middlename, lname):
        self.firstname=fname
        self.middlename=middlename
        self.lastname=lname
    
    def name(self):
        print(self.firstname, self.middlename,self.lastname)

def main():
    obj1=myClass()
    obj1.method1()
    obj1.method2("HAHAHA")

    obj2=myAnotherClass()
    obj2.method1()
    obj2.method2("HEEEEEHHHHHHAWWWWWWWWWWWWWw")

    obj3=otherClass(
        'Sabrin',
        'Lal',
        'Singh'
    )

    obj3.name()

if __name__=="__main__":
    main()