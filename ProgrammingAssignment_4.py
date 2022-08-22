def fac():
    n=int(input("Enter a number : "))
    fact=1
    if n<0:
        print("Factorial for negative numbers not possible")
    elif n==0:
        print("Factorial of 0 is 1")
    else:
        for i in range(1,n+1):
            fact=fact*i
    print(fact)

#fac()

def mult_table():
    n=int(input("Enter number"))
    for i in range(1,11):
        m=n*i
        print(m)
#mult_table()

def fib():
    a=0
    b=1
    for i in range(10):
        a, b = b, b + a
        print(a)

#fib()

def arm():
    num = int(input("Enter a number: "))
    sum = 0

    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    if num == sum:
        print(num, "is an Armstrong number")
    else:
        print(num, "is not an Armstrong number")

#arm()

def arm_int():
    l=100
    u=2000

    for i in range(l, u + 1):
        order=len(str(i))
        sum = 0
        temp = i
        while temp > 0:
            digit = temp % 10
            sum += (digit ** order)
            temp //= 10

        if (i == sum):
            print(i)

#arm_int()

def sum_n():
    n=int(input("Enter till which number sum is required"))
    sum = 0
    for i in range(1,n+1):
        sum=sum+i
    print(sum)

sum_n()










