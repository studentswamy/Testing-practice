arr = []
arr = [0 for i in range(5)] 
print(arr)

# creating Array an initializer 
arr_num = [0] * 2
print(arr_num)

arr_str = ['P'] * 5
print(arr_str)

class Employee:
    id=10
    name="Harish"
    def display(self):
        print(self.id,self.name)
        
emp=Employee()
emp1=Employee()
emp.display();
emp1.display();
        
class Employee5:
    def display(self,id,name):
        print(id,name)
emp = Employee5()      
emp1 = Employee5()
emp3=Employee5()
emp.display(1,"swami");
emp1.display(2,"vinay");

#Multiplication
class mul:
    a=90
    b=8
    mul=a*b
    def display (self):
        print(self.mul)
        mul=mul()
        mul.display();
        
# addition
class add:
    a=10
    b=25
    mul=a*b
    def display (self):
        print(self.add)
        add=add()
        add.display();

# division
class div:
    a=100
    b=95
    div=a*b
    def display (self):
        print(self.div)
        add=div()
        add.display();
        
# division
class div:
    a=100
    b=95
    div=a*b
    def display (self):
        print(self.div)
        add=div()
        add.display();
        
#rectangle
class rectangle:
    l=9.25
    b=19.72
    rect=l*b
    def display (self):
        print(self.rect)
rect=rectangle()
rect.display();

# Area of circle
class circle(object):
    def _init_(self, r):
        self.radius = r
        self.pi = 3.14
    def area(self):
        return(self.pi)*(self.radius)*(self.radius)
    #create an object
        result = circle(5)
        print("area of circle is",result.area())
        
    