import math
def fib_rec():

    def fib(x):
        if x<=1:
            return x
        else:
            return (fib(x-1)+fib(x-2))

    n = int(input("Enter number of terms"))

    if n<=0:
        print("Enter positive number")
    else:
        print("Fibonacci series")
        for i in range(n):
            print(fib(i))

#fib_rec()

def factorial():

    def fact(x):
        if x==1:
            return 1
        else:
            return x*fact(x-1)

    n=int(input("Enter a number"))
    if n<0:
        print("Factorial for neg numbers not possible")
    elif n==1:
        print("Factorial of 1 is 1")
    else:
        print(fact(n))

#factorial()

def bmi():
    w=float(input("Enter weight"))
    h=float(input("Enter height"))
    bmi=w/(h/100)**2
    if (bmi<=18.5):
        print("Underweight")
    elif bmi<=24.9:
        print("Healthy")
    elif bmi<=29.9:
        print("overweight")
    else:
        print("obese")

#bmi()

def ln():
    n=int(input("Enter number"))
    a=math.log(n)
    print(a)

#ln()

def scub():
    num=int(input("Enter num"))
    sum=0
    for i in range(num):
        sum=sum+i**3
    print(sum)

scub()




