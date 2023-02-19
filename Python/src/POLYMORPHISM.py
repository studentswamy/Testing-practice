# Method over riding.
class Vehicle:        # define parent class
    def run(self):
        print ("Vehicle is running")

class Bike (Vehicle): # define child class
   def run(self):
      print ("Bike is running")

c = Bike()          # instance of child
c.run()         # child calls overridden method

# 2. Method over loading.
Class emp
  def hello_emp(self,e_name=None):
   If e_name is not None:
   Print(“Hello”,e_name)
  Else:
   Print(“Hello”)
 Emp1=emp()
Emp1.hello_emp()
Emp1.hello_emp(“Kiran”)

class Overloading:#Overload@signature()
    def getmethod(self,j):
        print("First method",j)#getMethod.overload@signature(“int”)
    def getMethod(self,i):
        print("Second method",i)
obj = Overloading()
obj.getmethod(1)
obj.getMethod(2)











 
