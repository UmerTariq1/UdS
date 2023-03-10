
'''

Counting words (2 Points)

On the lecture's homepage, you can find a file (wsj00.txt) containing tokenized
English text.

Write a program wordcount.py that counts how often each word occurs in the file.

For instance,

    python3 wordcount.py wsj00.txt counts-wsj00.txt

should create a file 'counts-wsj00.txt' with the following content:

Mortimer	1
foul	1
Heights	4
four	13
spiders	1
Until	2
payoff	1
looking	7
...

The second column gives the total number of times the word occurs in the 
input file.

It is required to use exactly this format: 
word, tab (\t), number (\n)
word, tab (\t), number (\n)

Hint:

you can write such lines by concatenating strings using the + operator.

'''

import sys

def main():
    if len(sys.argv) != 3:
        print('Usage: python wordcount.py <input file> <output file>', file=sys.stderr)
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    
    #create a dict to keep the cound of words
    vocab = {}
    #read file
    with open(input_filename) as f:
        lines = f.readlines()
        for each_line in lines:
            for each_word in each_line.split(" "):
                if each_word in vocab:
                    vocab[each_word] = vocab[each_word] + 1
                else:
                    vocab[each_word] = 1

    with open(output_filename, 'a') as f:
        for each_vocab in vocab.keys():
            f.write( each_vocab + "\t" + str(vocab[each_vocab]) + "\n") 

if __name__ == '__main__':
    main()


