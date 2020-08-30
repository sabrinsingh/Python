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


def main():
    c=myClass()
    c.method1()
    c.method2("HAHAHA")

    c=myAnotherClass()
    c.method1()
    c.method2("HEEEEEHHHHHHAWWWWWWWWWWWWWw")

if __name__=="__main__":
    main()