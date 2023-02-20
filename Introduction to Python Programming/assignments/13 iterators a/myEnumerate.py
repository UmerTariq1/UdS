######################################
# Introduction to Python Programming #
# Iterators                          #
######################################

'''
EXERCISES 1

Reimplement the builtin "enumerate." Each call of the "next" method should
return a pair (tuple) containing the count (starting from 0) and the value
obtained from iterating over the sequence the function is applied to. Make sure
that your also works with unordered collection types such as sets or
dictionaries. (2 Points)

Note: If you have troubles in making myEnumerate work for unordered types,
implement it for ordered types such as lists or strings. (-1 Point)
'''

class myEnumerate:

    def __init__(self, iterable):
        self.iterable = iterable
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        try:
            item = self.iterable[self.count]
            count = self.count
            self.count += 1
            return count, item
        except IndexError:
            raise StopIteration
        



if __name__ == '__main__':
    for (i, ch) in myEnumerate("Python"):
        print(i, ch)

    # Output:
    # 0 P
    # 1 y
    # 2 t
    # 3 h
    # 4 o
    # 5 n
    
    # NOT IMPLEMENTED FOR UNORDERED LISTS. COMMENTED THE CODE SO THERE IS NO ERROR IN OUTPUT
      
    # for (i, ch) in myEnumerate(set(["a", "b", "c"])):
    #     print(i, ch)
    
    # Output: (order might differ)
    # 0 a
    # 1 b
    # 2 c
