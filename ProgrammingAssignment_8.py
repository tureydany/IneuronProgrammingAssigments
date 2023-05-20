def matrix_add():
    X=[[0,1,2],[3,4,5],[6,7,8]]
    Y=[[11,12,13],[14,15,16],[17,18,19]]

    Result=[[0,0,0],[0,0,0],[0,0,0]]

    for i in range(len(X)):
        for j in range(len(Y[0])):
            Result[i][j]=X[i][j]+Y[i][j]

    print(Result)
    return 0

def matrix_mul():
    p=int(input("Enter row number for matrix 1:"))
    q=int(input("Enter column number for matrix 2:"))
    n=int(input("Enter column number/row number  for matrix 1/matrix 2:"))


    print("Enter values for matrix 1 :")
    mat1=[[int(input()) for i in range(n)] for j in range(p)]
    print("matrix 1 :")
    for i in range(p):
        for j in range(n):
            print(format(mat1[i][j], ">5"),end=" ")
        print()

    print("Enter values for matrix 2 :")
    mat2=[[int(input()) for i in range(q)] for j in range(n)]
    print("matrix 2:")
    for i in range(n):
        for j in range(q):
            print(format(mat2[i][j],">5"),end=" ")
        print()
    
    result=[[0 for i in range(q)] for j in range(p)]

    for i in range(p):
        for j in range(q):
            for k in range(n):
                result[i][j]=result[i][j]+mat1[i][k]*mat2[k][j]

    print("Result is :")
    for i in range(p):
        for j in range(q):
            print(format(result[i][j],">5"),end=" ")
        print()

def matrix_transpose():
    p=int(input("Enter row number for matrix 1:"))
    q=int(input("Enter column number for matrix 2:"))

    print("Enter values for matrix:")
    mat1=[[int(input()) for i in range(q)] for j in range(p)]
    print("matrix:")
    for i in range(p):
        for j in range(q):
            print(format(mat1[i][j],">5"),end=" ")
        print()
    
    result=[[0 for i in range(q)] for j in range(p)]
    
    for i in range(q):
        for j in range(p):
            result[i][j]=mat1[j][i]

    print("Result is :")
    for i in range(p):
        for j in range(q):
            print(format(result[i][j],">5"),end=" ")
        print()

def sort_words():
    a = input("enter a sentence here: ")
    l = a.split()
    print (l)

    for i in range (len(l)):
        l[i] = l[i].lower()

    l.sort()

    for i in l:
        print (i)

def remove_punctuation():
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    string = input("enter a string here: ")

    empty_str = ""

    for i in string:
        if i not in punc:
            empty_str+=i

    print (empty_str)

remove_punctuation()
#sort_words()        

#matrix_transpose()
#matrix_mul()

#matrix_add()