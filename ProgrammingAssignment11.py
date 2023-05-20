def word_k(k, s):    
    word = s.split(" ")
   
    for x in word:

        if len(x)>k:
            print(x)

#word_k(3,"Python is good")

def remove_char(i,str):

    str=str.replace(str[i]," ")
    print(str)

#remove_char(3,"Unforgiven")

def split_string(string):
    list_string = string.split(' ')
    print("After Splitting: ",list_string)
    return list_string

def join_string(string):
    string = '-'.join(string)
    print("After joining: ",string)
    return string

def check_binary(string) :
    b = set(string)
    s = {'0', '1'}
    if s == b or b == {'0'} or b == {'1'}:
        print("Binary String")
    else :
        print("Non Binary String")
  
#check_binary("00110101")

def UncommonWords(A, B):
 
    count = {}

    for word in A.split():
        count[word] = count.get(word, 0) + 1
 
    for word in B.split():
        count[word] = count.get(word, 0) + 1
 
    return [word for word in count if count[word] == 1]
 
from collections import Counter
def duplicate_character(input):
   string = Counter(input)

   for char, count in string.items():
      if (count > 1):
         print(char)
duplicate_character("test duplicate characters")

def check_special_char():
    import re
    string ="elephant_34^"

    if(bool(re.match('^[a-zA-Z0-9]*$', string)) == True):
        print('String does not contain any special characters.')
    else:
        print('The string contains special characters.')

check_special_char()
#print(UncommonWords("Hi Hello goodevening", "Hi Greetings hello goodbye"))


#split_string('Welcome to study tonight')
#join_string("Hi Hello")


    
   