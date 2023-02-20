'''
Implement a function is_prime(x) that returns True if x is prime, False 
otherwise. (1 Point)

>>> is_prime(7)
True
>>> is_prime(15)
False
'''

import copy
# ... your code ...

def is_prime(a):
    #base case
    if a <= 1:
        return False
    current_number = copy.deepcopy(int((a/2)+1))

    while current_number > 1:
        if current_number != a and a%current_number==0:
            return False

        current_number-=1 
    return True

# this is for automatic testing.
if __name__ == '__main__':
    print('*** Test is_prime ***')
    print('Test1', is_prime(1) == False)
    print('Test2', is_prime(2) == True)
    print('Test3', is_prime(3) == True)
    print('Test4', is_prime(4) == False)
    print('Test5', is_prime(5) == True)
    print('Test6', is_prime(11021) == False)
