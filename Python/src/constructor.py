class Employee:  
    def __init__(self, name, id):  
        self.id = id  
        self.name = name  
  
    def display(self):  
        print("ID: %d \nName: %s" % (self.id, self.name))  
  
  
emp1 = Employee("Vinay", 101)  
emp2 = Employee("Metha", 102)  
  
# accessing display() method to print employee 1 information  
  
emp1.display()  
  
# accessing display() method to print employee 2 information  
emp2.display()


#Non - Parametrized constructor.

class Student:  
    # Constructor - non parameterized  
    def __init__(self):  
        print("This is non parametrized constructor")  
    def show(self,name):  
        print("Hello",name)         
student = Student()  
student.show("John")

# PYTHON DEFALUT CONSTRUCTOR:
class Student:  
    roll_num = 101  
    name = "Joseph"  
  
    def display(self):  
        print(self.roll_num,self.name)  
  
st = Student()  
st.display()

