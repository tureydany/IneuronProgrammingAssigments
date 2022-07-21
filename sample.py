import calendar
import cmath

def km_to_m(a):
    c=a*1000.0
    print("%0.0f km converted to %0.0f m "%(a,c))

km_to_m(2)

def celsius_to_fahrenheit():
    d=float(input("Enter temperature in celsius"))
    f=(d*1.8)+32
    print("%0.00f celsius converted to %0.00f fahrenheit" %(d,f))

#celsius_to_fahrenheit()

def calendar_func():
    year=int(input("Enter year"))
    month=int(input("Enter month"))
    print(calendar.month(year,month))

#calendar_func()

def quadratic_eq():
    a=float(input("Enter value for a :"))
    b=float(input("Enter value for b:"))
    c=float(input("Enter value for c:"))

    d=(b**2)-(4*a*c)

    s1=(-b+cmath.sqrt(d))/2*a
    s2=(-b-cmath.sqrt(d))/2*a

    print("The solutions are {0} and {1}".format(s1,s2))

quadratic_eq()

