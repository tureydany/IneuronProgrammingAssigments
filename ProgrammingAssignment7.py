import numpy as np

a=np.asarray([5,4,3,2,1])

def sum_a(x):
    sum=0
    for i in x:
        sum=sum+i
    print(sum)

#sum_a(a)

def max_a(x):
    print("Largest element is ",x.max())

#max_a(a)

def rt(x,d):
    n=len(x)
    x[:]=x[d,n]+x[0,d]
    return x

#rt(a,2)

def mt(x):
    n=len(x)
    flag=False
    if n==1:
        flag=True
    else:
        for i in range(n):
            for j in range(i+1,n):
                if a[i]<a[j]:
                    flag=True
                elif a[i]>a[j]:
                    flag=True
    if flag==True:
        print("True")
    else:
        print("False")

mt(a)