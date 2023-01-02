#singleton

class MyClass:
    __instance = None

    def __init__(self):
        if MyClass.__instance == None:
            MyClass.__instance = self
        else:
            print("MyClass::__init__ called")

    def instance(): 
        if MyClass.__instance == None:
            MyClass()
        
        return MyClass.__instance


myClass0 = MyClass.instance()
myClass1 = MyClass.instance()
print(myClass0)
print(myClass1)