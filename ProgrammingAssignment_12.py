from collections import OrderedDict 



def unique_dict():
    dict1 = {'A' : [1, 3, 5, 4],
             'B' : [4, 6, 8, 10],
             'C' : [6, 12, 4 ,8],
             'D' : [5, 7, 2]}

    print("The original dictionary is : " ,dict1)

    res = list(sorted({ele for val in dict1.values() for ele in val}))
    print("The unique values list is : " , res)

def sum_dict():
    dic={ 'x':455, 'y':223, 'z':300, 'p':908 }
    print("Dictionary: ", dic)
    print("sum: ",sum(dic.values()))


def merge_dict():
    dict_3 = {1: 'a', 2: 'b'}
    dict_4 = {2: 'c', 4: 'd'}

    print(dict_3 | dict_4)

def flatten_dict():
    dic= { "day": [1, 2, 3], "name": ['Mon', 'Tues', 'Wed' ] }
    print("Original dictionary: ",dic)

    f_dic= dict(zip(dic["day"], dic["name"]))
    print("FLATTENED DICTIONARY: ", f_dic)

def insert_dict():
    dic1 = OrderedDict([('A', '100'), ('B', '200'), ('C', '300')])
    insrt = OrderedDict([("D", '400')])
  
    final = OrderedDict(list(insrt.items()) + list(dic1.items()))
    print ("Resultant Dictionary :")
    print(final)

def checkOrder(string, pattern): 
    dic = OrderedDict.fromkeys(string) 
    print(dic)
    ptr = 0
    for key,value in dic.items(): 
        if (key == pattern[ptr]): 
            ptr = ptr + 1
        if (ptr == (len(pattern))): 
            return 'True'
    return 'False'

print (checkOrder('Study tonight','stu'))

def sort_dict():
    key_value={}

    key_value[5] = 10      
    key_value[3] = 8
    key_value[6] = 77
    key_value[4] = 23
    key_value[2] = 9     
    key_value[1] = 43
 
    print("sorting on the basis of keys")
    print(sorted(key_value))
    for i in sorted(key_value) :
        print ((i,key_value[i]), end =" ")

#sort_dict()
     
#insert_dict()
#flatten_dict()
#merge_dict()
#sum_dict()
#unique_dict()