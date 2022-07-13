import random

#1.Write a Python program to print &quot;Hello Python&quot;?
def sample():
    print("Hello Python")

#2. Write a Python program to do arithmetical operations addition and division.?
def add(a,b):
    c=a+b
    print("sum of two nos:",c)


def division(a,b):
    c=a/b
    print("division of two nos :",c)

sample()
add(3,4)
division(4,2)

#3. Write a Python program to find the area of a triangle?
def area_t(b,h):
    a=0.5*b*h
    print("area of triangle is :",a)

area_t(3,4)

#4. Write a Python program to swap two variables?
def swap():
    a=input("Enter value for a")
    b=input("Enter value for b")
    t=a
    a=b
    b=t
    print("value of a:",a)
    print("value of b:",b)
swap()

#5. Write a Python program to generate a random number?
e=random.randint(0,10)
print(e)