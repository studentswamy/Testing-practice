def my_function(): 
  print("Hello from a function")

my_function()

def add_number():
    a=12;
    b=2;
    print("addition",a+b)
add_number()

def multiplication():
    a=12;
    b=2;
    print("multiplication",a*b)
multiplication()

def substraction():
    a=3;
    b=2;
    print("substraction",a-b)
substraction()

def square():
    num=6
    print("square of number",num*6)
square()

def area_circle():
    pi=3.142;
    r=3
    print("area of circle",pi*r*r)
area_circle()

def area_rectangle():
    w=8;
    l=10;
    print("area of rectangle",w*l)
area_rectangle()

def greaterthan():
    A=100;
    B=80;
    if A>B:
        print('A is greater than B')
    else:
        print('B is greater than A')
greaterthan()


def pattern6(n):
    for i in range (0,n):
        for j in range(0,i+1):
            print("*", end=" ")
            print()
pattern6(5)

def reverse_sting(Kanthara):
    string = "Kanthara"
    return string
        
