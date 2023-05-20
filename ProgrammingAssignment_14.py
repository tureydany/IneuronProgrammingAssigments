import operator
import zlib
import math

#n = int(input())
#divBy7 = [i for i in range(0, n) if (i % 7 == 0)]
#print(divBy7)

def divChecker(n):
    for i in range(n):
        if i % 7 == 0:
            value = True
        else:
            value = False
        print(i, value)

#divChecker(n)

def word_count_sort_dict():
    text_line = input("Type in: ")

    freq_dict = {}

    for i in text_line.split(' '):
        if i.isalpha():
            if i not in freq_dict:
                freq_dict[i] = 1
        elif i in freq_dict:
            freq_dict[i] = freq_dict[i] + 1
        else:
            pass

    sorted_freq_dict = sorted(freq_dict.items(), key = operator.itemgetter(0))
    print(sorted_freq_dict)

    for i in sorted_freq_dict:
        print(i[0], i[1])

#word_count_sort_dict()

class Person(object):
    def getGender( self ):
        return "Unknown"

class Male(Person):
    def getGender( self ):
        return "Male"

class Female(Person):
    def getGender( self ):
        return "Female"

    aMale = Male()
    #aFemale = Female()
    print (aMale.getGender())
    #print (aFemale.getGender())

def compress():
    s = 'hello world!hello world!hello world!hello world!'

    y = bytes(s, 'utf-8')
    x = zlib.compress(y)
    print(x)
    print(zlib.decompress(x))

#compress()

def bin_search(li, element):
    bottom = 0
    top = len(li)-1
    index = -1
    while top>=bottom and index==-1:
        mid = int(math.floor((top+bottom)/2.0))
        if li[mid]==element:
            index = mid
        elif li[mid]>element:
            top = mid-1
        else:
            bottom = mid+1

    return index
print(bin_search([2,5,7,9,11,17,222],11))
print (bin_search([2,5,7,9,11,17,222],12))