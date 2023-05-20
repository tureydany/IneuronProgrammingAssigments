def sum_list():
    n=int(input("Enter size of list:"))
    l1=[]
    print("Enter list elements :")
    for i in range(n):
        l1.append(int(input()))

    sum=0
    for i in range(n):
        sum=sum+l1[i]
    print(sum)
    return sum

def mul_list():
    n=int(input("Enter size of list:"))
    l1=[]
    print("Enter list elements :")
    for i in range(n):
        l1.append(int(input()))

    product=1
    for i in range(n):
        product=product*l1[i]
    print(product)
    return product

def smallest_list():
    n=int(input("Enter size of list:"))
    l1=[]
    print("Enter list elements :")
    for i in range(n):
        l1.append(int(input()))

    print("Smallest element in list is",min(l1))

def largest_list():
    n=int(input("Enter size of list:"))
    l1=[]
    print("Enter list elements :")
    for i in range(n):
        l1.append(int(input()))

    print("Largest element in list is",max(l1))

def second_largest():
    n=int(input("Enter size of list:"))
    l1=[]
    print("Enter list elements :")
    for i in range(n):
        l1.append(int(input()))

    l1.sort()
    print("Second Largest element in list is",l1[n-2])

def get_NLargest():
    s=int(input("Enter size of list:"))
    l1=[]
    print("Enter list elements :")
    for i in range(s):
        l1.append(int(input()))

    l1.sort(reverse=True)
    n=int(input("Enter how many N largest elements to be displayed :"))
    for i in range(n):
        print(i,"nd largest element is",l1[i])

def display_even():
    s=int(input("Enter size of list:"))
    l1=[]
    print("Enter list elements :")
    for i in range(s):
        l1.append(int(input()))
    
    print("Even numbers in list:")
    for i in range(s):
        if l1[i]%2==0:
            print(l1[i])

def display_odd():
    s=int(input("Enter size of list:"))
    l1=[]
    print("Enter list elements :")
    for i in range(s):
        l1.append(int(input()))
    
    print("Odd numbers in list:")
    for i in range(s):
        if l1[i]%2!=0:
            print(l1[i])

def remove_emptylist():
    test_list = [5, 6, [], 3, [], [], 9]
    print("The original list is : " + str(test_list))

    res = [ele for ele in test_list if ele != []]
    print("List after empty list removal : " + str(res))

def cloning():
    l1 = [4, 8, 2, 10, 15, 18]

    l2=l1[:]
    print("Original List:", l1)
    print("After Cloning:", l2)

def countX(lst, x):
    count = 0
    for ele in lst:
        if (ele == x):
            count = count + 1
    print('{} has occurred {} times'.format(x,count))
    return count
    
 

countX([8, 6, 8, 10, 8, 20, 10, 8, 8],8)

#cloning()
#display_odd()
#display_even()
#get_NLargest()
#second_largest()
#largest_list()
#smallest_list()
#mul_list()
#sum_list()
