''' 1. POS-Tagged text (3 Points)

The file "example.xml"  containing POS-tagged text, where words are 
represented as follows:

    <W TYPE="part of speech" ...>word</W>

Write a function that reads the file and ** returns ** a list of word-POS 
pairs (see example below).

Example:

read_file("example.xml")

should return:

[('FACTSHEET', 'NN1'), ('WHAT', 'DTQ'), ('IS', 'VBZ'), ...]
'''

import sys
import re



def read_file(filename):
    pattern = '<W TYPE="(.+?)".*?>(.+?)<\/W>'
    with open(filename) as f:
        ret_data = []
        data = f.read()
        for index,each_data in enumerate(data.split("\n")):
            match = re.search(pattern, each_data)
            if match:
                ret_data.append(match.groups())


    return ret_data# the resulting list; DO NOT PRINT

def main():
    # for testing
    pairs = read_file('example.xml')
    for (word, pos) in pairs:
        print(word, pos)

if __name__ == '__main__':
    main()

