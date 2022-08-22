def lcm():
    x=int(input("Enter first number"))
    y=int(input("Enter second number"))

    def gcd(x, y):
        while (y):
            x, y = y, x % y
        return x

    res=(x*y)//gcd(x,y)
    print("LCM IS " ,res)
    print("GCD IS",gcd(4,3))
#lcm()

def dec_cn():
    num=int(input("Enter decimal number"))

    print(num,"in binary forat number is ",bin(num))
    print(num,"in octal format is ",oct(num))
    print(num,'in hexadecimal format is ',hex(num))
#dec_cn()

def ascii_val():
    a=input("Enter a character")
    print("The ascii value is ",ord(a))

#ascii_val()

def calculator():
    print(" Choose any one of the operations  \n1.Addition \n2.Subtraction \n3.Multiplication \n4.Division")
    c=int(input("Enter option -"))

    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))

    def add(x,y):
        return x+y
    def sub(x,y):
        return x-y
    def mul(x,y):
        return x*y
    def div(x,y):
        return x/y


    if c==1:
        print("Addition operation",add(a,b))
    elif c==2:
        print("Subtraction operation",sub(a,b))
    elif c==3:
        print("Multiplication operation",mul(a,b))
    elif c==4:
        print("Division operation",div(a,b))
    else:
        print("Invalid choice")

calculator()







