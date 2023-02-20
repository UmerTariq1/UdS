"""
Introduction to Python Programming
COLLECTIONS

Exercise 1: Lists (4 points)

a) Write a function countElements(myList) that takes a list
   as its parameter and that counts for each element of the
   list how often it occurs in the list. The return value of
   the function is supposed to be a dictionary whose keys are
   the elements of the list and whose values are integers
   indicating how often each element occurs in the list. 
"""

def countElements(myList):
    """
    Remove the 'pass' statement (which stands for 'do nothing')
    and write your own code.

    Example code:
    >>> countElements(['b','b','c','a','a','b','c','b','a'])
    {'b': 4, 'c': 2, 'a': 3}
    """
    count_values = {}
    for i in myList:
        if i not in count_values:
            count_values[i] = 1
        else:
            count_values[i] += 1
    return count_values
    


"""
b) Implement the above function such that it returns a list of tuples
   (key, value). The returned list of tuples is supposed to be sorted
   by the second element of the tuples (= by how often the values
   occur in the dictionary, with the element that occurs most often
   first).
   
   You can use the builtin functions sorted() or list.sort() to sort
   a list of tuples. Note, however, that these function sort by the first
   element of a tuple by default.
"""

def countElements2(myList):
    """
    Remove the 'pass' statement and write your own code.

    >>> countElements2(['c','b','c','a','c','b','c','b','a'])
    [('c', 4), ('b', 3), ('a', 2)]
    """
    count_values = {}
    for i in myList:
        if i not in count_values:
            count_values[i] = 1
        else:
            count_values[i] += 1
            
    return {k: v for k, v in sorted(count_values.items(), key=lambda item: item[1], reverse=True)}


if __name__ == "__main__":
    # This executes the functions
    # Comment out one of the functions when testing!
    
    print ( countElements(['b','b','c','a','a','b','c','b','a']) )
    
    print( countElements2(['c','b','c','a','c','b','c','b','a']) )

