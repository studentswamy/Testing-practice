def my_function(): 
  print("Hello from a function")

my_function()

def add():
  num =10
  num2=20
  sum= num+num2
  print("the sum of two numbers", sum)
add()

def my_function(fname,sno):
  print(fname)
  print(sno)
my_function("Emil",1)
my_function("Tobias",2)
my_function("Linus",4)


def add_one(x):
     # No return statement at all
     result = x+5
     return result
output = add_one(5)
print(output)


