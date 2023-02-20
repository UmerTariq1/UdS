'''
2 Points

Implement a function flatten1 that, when applied to a list of lists,
returns a list of all elements of the embedded lists, preserving their
order:

>>> flatten1([[1,2,3], [4,5,6], [7], [], [8, 9]]):
[1,2,3,4,5,6,7,8,9]

Note that flatten1 is not "recursive" i.e., when one of the embedded list
contains (one or more) other lists, these lists should not be "flattend":

>>> flatten1([[1,2,3], [[4,5,6], [7]], [], [8, 9]]):
[1,2,3,[4,5,6],[7],8,9]

'''

def flatten1(lol):
    # your code
    ret_list = []
    for l in lol:
        for item_l in l:
            ret_list.append(item_l)
    return ret_list

if __name__ == '__main__':
    print(flatten1([[1,2,3], [4,5,6], [7], [], [8, 9]]) == [1,2,3,4,5,6,7,8,9])
    print(flatten1([[1,2,3], [[4,5,6], [7]], [], [8, 9]]) == [1,2,3,[4,5,6],[7],8,9])
