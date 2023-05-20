def check_disarium(n):
    temp=n
    x=n

    count=0
    while temp>0:
        temp=temp//10
        count=count+1
    
    sum=0
    while x>0:
        rem=x%10
        sum=sum+rem**count
        x=x//10
        count=count-1

    if sum==n:
        print(n,"is a disarium number")
    else:
        print(n,"is not a disarium number")
    
    return n

def range_disarium():
    lower = int(input("ENTER LOWEST NUMBER : "))
    upper = int(input("ENTER HIGHEST NUMBER : "))
    print("DISARIUM NUMBERS WITHIN RANGE({},{}) ARE -".format(lower,upper))
    for i in range(lower,upper+1):
        if check_disarium(i) == i:
            print(i)

def check_happynum(n):
    x=n
    while x>10:
        sum=0
        while x>0:
            r=x%10
            sum=sum+(r**2)
            x=x//10
        x=sum
    if x==1:
        print(n,"is a Happy number")
    else:
        print(n,"is not a happy number")
    return x

def range_happynum():
    lower = int(input("ENTER LOWEST NUMBER : "))
    upper = int(input("ENTER HIGHEST NUMBER : "))
    print("HAPPY NUMBERS WITHIN RANGE({},{}) ARE -".format(lower,upper))
    for i in range(lower,upper+1):
        if check_happynum(i) == 1:
            print(i)

def check_harshadnum(n):
    x=n
    sum=0
    while x>0:
        r=x%10
        sum=sum+r
        x=x//10
    if n%sum==0:
        print(n,"is harshad number")
    else:
        print(n,"is not a harshad number")

    return n%sum



def range_harshadnum():
    lower = int(input("ENTER LOWEST NUMBER : "))
    upper = int(input("ENTER HIGHEST NUMBER : "))
    print("HAPPY NUMBERS WITHIN RANGE({},{}) ARE -".format(lower,upper))
    for i in range(lower,upper+1):
        if check_harshadnum(i) == 0:
            print(i)

range_harshadnum()

#range_happynum()
#range_disarium()




