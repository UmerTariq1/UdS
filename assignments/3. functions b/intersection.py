'''

Implement a function that computes the intersection of two lists, i.e. a
function that returns a list of elements that are members of both input-lists.
(2 Points)

>>> intersection([1, 2, 3, 4], [2, 4, 6])
[2, 4]

Hints and comments:

x = [] creates an empty list

x.append(y) adds y to list x

>>> x = []
>>> x.append(1)
>>> x
[1]
>>> x.append(2)
>>> x
[1, 2]
'''


# ... your code ...

def is_member(a, list_b):
    for i in list_b:
        if a==i:
            return True
    return False

def intersection(list_a, list_b):
    ret_lsit = []
    for i in list_a:
        if is_member(i,list_b) :
            ret_lsit.append(i)
    return ret_lsit

# this is for automatic testing.
if __name__ == '__main__':
    print('*** Test intersection ***')
    print('Test1', sorted(intersection([1, 2, 3], [3, 2, 1])) == [1,2,3])
    print('Test2', sorted(intersection([1, 2, 3], [2, 3])) == [2,3])
    print('Test3', sorted(intersection([1, 2, 3], [4])) == [])
    print('Test4', sorted(intersection([], [4])) == [])
