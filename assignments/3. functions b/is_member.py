'''
Implement a function is_member(x, somelist) that returns True if x is an element
of somelist, False otherwise. (2 Points)

>>> is_member(2, [1, 2, 3])
True
>>> is_member(4, [1, 2, 3])
False

Note that this is exactly what the in operator does. 

>>> 2 in [1, 2, 3]
True
>>> 4 in [1, 2, 3]
False

For the sake of the exercise you should not use this operator.
'''


# ... your code ...
def is_member(a, list_b):
    for i in list_b:
        if a==i:
            return True
    return False


# this is for automatic testing.
if __name__ == '__main__':
    print('*** Test is_member ***')
    print('Test1', is_member(2, [1, 2, 3]) == True)
    print('Test2', is_member(4, [1, 2, 3]) == False)
    print('Test1', is_member(2, []) == False)
