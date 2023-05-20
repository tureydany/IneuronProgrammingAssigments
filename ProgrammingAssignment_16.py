import math

def stutter(word):
    s = word[:2]
    return (2 * (s + '... ')) + word + '?'


#print(stutter("incredible"))

def radians_to_degrees(radian):
    pi = 3.14159
    #formula
    degree = radian * (180/pi)
    return degree
'''radian = float(input('Enter the Radian : '))
print("degree =",(radians_to_degrees(radian)))'''

def checkIfCurzonNumber(n):
 
    power, product = 0, 0
 
    # Find 2**n + 1
    power = pow(2, n) + 1
 
    # Find 2*n + 1
    product = 2 * n + 1
 
    # Check for divisibility
    if (power % product == 0):
        print(n, "is Curzon Number")
    else:
        print(n, "is not a Curzon Number")
        
'''n = int(input('Enter a number : '))
checkIfCurzonNumber(n)'''

def area_of_hexagon(s):     
    return ((3 * math.sqrt(3) * (sideLength * sideLength)) / 2);
     
#length of a side.
sideLength = float(input('Enter the length : '))

#print("Area:","{0:.4f}".format(area_of_hexagon(sideLength)))

def decimalToBinary(n):
    return bin(n).replace("0b", "")
   
for i in range(0,50):
    print(decimalToBinary(i))