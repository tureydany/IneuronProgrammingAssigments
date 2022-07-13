import random

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