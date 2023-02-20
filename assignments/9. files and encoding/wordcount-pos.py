
'''

Counting tagged words (3 points)

On the lecture's homepage, you can find a part-of-speech (POS) tagged version of the 
file from the third exercise (wsj00-pos.txt), where each line contains a single token consisting
of a word and its POS tag, separated by '/'.

Write a program wordcount-pos.py that counts how often each word occurs in the file,
and how often it has been tagged with which POS.
The counts should be written to a new file, which is also given on the command line.

For instance,

    python3 wordcount-pos.py wsj00-pos.txt counts-wsj00-pos.txt

should produce a output like this:

Mortimer	1	NNP	1
foul	1	JJ	1
...
reported	16	VBN	7	VBD	9
...
before	26	RB	6	IN	20
...
allow	4	VB	2	VBP	2
...

The second column gives the total number of times the word occurs in the 
input file.

It is required to use exactly this format: 
word, tab (\t), number, tab, POS, tab, number, tab, POS, tab, number, ...
word, tab (\t), number, tab, POS, tab, number, tab, POS, tab, number, ...

Hint:

* To split a word/pos pair into two separate strings (word and pos), you can
  use pair.rsplit('/', 1); you can use the following code to assing the word
  and the pos of a word-pos pair to two distinct variables in one step:
  
  word, pos = token.rsplit('/', 1)

'''

import sys

def main():
    if len(sys.argv) != 3:
        print('Usage: python poscount.py <input file> <output file>', file=sys.stderr)
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    # your code
    
    #create a dict to keep the cound of words.
    # it is a nested dictionary i.e each value is itself a dictionary. and inner dictioanry keys are pos tags and inner dictionary values are counts of pos tags for this specific word.
    # there is a key "count" in inner dictionary which represent the total count of the word
    vocab = {}
    
    #read file
    with open(input_filename) as f:
        lines = f.readlines()

        for each_line in lines:
            #because there are some lines which are empty
            if "/" in each_line:
                # get word and pos from each line and for pos remove the \n which every line has
                word, pos = each_line.split("/")[0], each_line.split("/")[1][:-2]
                #if the word is already in the vocab dictionary
                if word in vocab:
                    
                    vocab[word]["count"] += 1
                    #check if this word/pos tag has already been seen 
                    if pos in vocab[word]:
                        vocab[word][pos] += 1
                    #if word is there but pos is seen for the first time with this word then add the pos to this word dictionary item
                    else:
                        vocab[word][pos] = 1
                #if word hasnt been seen before then add the word and its pos to the vocab
                else:
                    vocab[word] = {"count":1, pos:1}

    # Open the output file for writing
    with open(output_filename, 'w') as f:
        # Iterate over the words and counts in the dictionary
        for word, counts in vocab.items():
            # Write the word and total count to the output file
            f.write(f"{word}\t{counts['count']}")
            # Iterate over the POS tags and counts for the word
            for pos, count in counts.items():
                # Skip the total count for the word
                if pos == 'count':
                    continue
                # Write the POS tag and count to the output file
                f.write(f"\t{pos}\t{count}")
            # Add a newline after each word
            f.write("\n")



if __name__ == '__main__':
    main()


