
def numbers():
    try:
        a = int(input("Enter a number"))
        if a > 0:
            print("Positive number")
        elif a < 0:
            print("Negative number ")
        else:
            print("Zero")
    except Exception as e:
        print(e)

numbers()

def even_odd():
    try:
        x = int(input("Enter value for x:"))
        if x%2==0:
            print("{0} is even number".format(x))
        else:
            print("{0} is odd number".format(x))
    except Exception as e:
        print(e)

even_odd()

def leap_year():
    year=int(input("Enter year"))
    if year%400==0 and year%100==0:
        print("{0} is a leap year".format(year))
    elif year%4==0 and year!=100:
        print("{0} is a leap year".format(year))
    else:
        print("{0} is not a leap year".format(year))

leap_year()

def prime():
    flag=False
    num=int(input("Enter a number"))
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                flag=True
                break
    if flag==True:
        print("{0} is not a prime number".format(num))
    else:
        print("{0} is a prime number ".format(num))

prime()

def prime_range():
    flag =False
    for i in range(1, 10000):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
                else:
                    print(i)

prime_range()






