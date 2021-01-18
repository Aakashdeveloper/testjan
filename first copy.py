class Person():

    def __init__(self,name):
        self.name = name 

    def getName(self):
        return self.name
    
    def isEmployee(self):
        return False
        
    def test(self):
        return 'hii'


class Employee(Person):
    def isEmployee(self):
        return True