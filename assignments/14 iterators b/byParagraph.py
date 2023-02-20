######################################
# Introduction to Python Programming #
# WS 2013/2014                       #
# Iterators & Generators             #
######################################


'''
Implement an iterator that iterates over a file by paragraph.
By "paragraph" we mean all lines in the file which are not separated
by blank lines. For instance, the string

"""

This is an a sentence.

This is another sentence.
Followed by yet another one.


This is not the last sentence.
This one neither.



This one is the last one.
"""

contains four paragraphs. Yor iterator should thus return four strings.

(4 Points)

Hints:

* S.isspace() returns True if all characters in string S are whitespace
  and there is at least one character in S, False otherwise.
  
  Note that if you read in a file line by line, each line usually contains
  at least one character (the "newline" character \n).

  Note also that, when applied to the empty string, isspace returns False:

  >>> ''.isspace()
  False

* S.rstrip() returns a copy of S with all trailing white space characters removed.

* S.join(iterable) returns a string which is the concatenation of the
  strings in the iterable. The separator between elements is string S.
  
  For instance:
  
  ' '.join(['Help', 'me', 'please']) returns 'Help me please'
  
  (This is often more efficient than concatenating strings using + or +=)
'''

class ByParagraph:
  def __init__(self,data):
    self.data = data


  def __iter__(self):
    return self

  def __next__(self):
    paragraphs = []
    for i in self.data:
      if i.isspace():
        break
      paragraphs.append(i.strip())
    else:
      if not paragraphs:
        raise StopIteration()
    return ' '.join(paragraphs)



with open("example.txt") as f:
  for p in ByParagraph(f):
    print(p)
        

# should print four lines:

#This is an a sentence.
#This is another sentence. Followed by yet another one.
#This is not the last sentence. This one neither.
#This one is the last one.
