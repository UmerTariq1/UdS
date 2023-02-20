'''
Implement a function gcd(x, y) that computes the greatest common divisor 
of x and y. (1 Point)

>>> gcd(8, 12)
4

'''

# I have implemented two algos for gcd, and wanted to compare teir time too. the second approach is faster


import time



# ... your code ...
#my function below
def gcd(a,b):
    greater_number = a if a<=b else b   #get the smaller number
    current_number = int(greater_number / 2) # half of the smaller number
    while  current_number!=0:
        if a%current_number == 0 and b%current_number == 0:
            return current_number
        current_number -= 1

#code which is optimized like numpy. i didnt copy the code. i read the algorithm from stackoverflow and then wrote this code myself.
def gcd2(a,b):
    while b != 0:
        a,b = b,a%b
    return a

# this is for automatic testing.
if __name__ == '__main__':
    print('*** Test gcd ***')
    start = time.time()
    print('Test1', gcd(8, 12) == 4)
    print('Test2', gcd(42, 56) == 14)
    print('Test3', gcd(1071, 1029) == 21)
    end = time.time()
    print(end-start)

    print('*** Test gcd ***')
    start = time.time()
    print('Test1', gcd2(8, 12) == 4)
    print('Test2', gcd2(42, 56) == 14)
    print('Test3', gcd2(1071, 1029) == 21)
    end = time.time()
    print(end-start)
