''' 2. Extracting noun phrases (3 Points)

Consider the file "wsj00-pos-oneline" that contains POS tagged text. In this
file, POS information is encoded as follows:

Pierre/NNP Vinken/NNP ,/, 61/CD years/NNS old/JJ ,/, will/MD join/VB 
the/DT board/NN as/IN a/DT nonexecutive/JJ director/NN Nov./NNP 29/CD ./.
...

Implement program that reads this file and prints all noun phrases that occur
in the text. To keep things simple, take noun phrases to be the following 
sequence of words/parts of speech:

    DT + zero or more JJ + NN

where DT is the POS for determiners like "the" or "a", JJ is the POS for
adjectives, and NN is the pos for nouns.

Example:

python3 regexp2.py

should ** print **:

the/DT board/NN 
a/DT nonexecutive/JJ director/NN
a/DT nonexecutive/JJ director/NN
this/DT British/JJ industrial/JJ conglomerate/NN
...

'''

import sys
import re


PATTERN = '([A-Z|a-z]+?)\/(.+?)$'
def extract_noun_phrases(line):
    '''
    Algorithm:
    Iterate over each word of line. Apply regex on the word. As soon as you find a DT, that means you are at a potential match.
    Then increment the temporary index (current_temp_index), and look at the pos of next word.
    If the pos is JJ then then noun phrase continues...and keep looking ahead.
    If the pos is NN then the noun phrase is complete. append the string that is created till now to the each_line_noun_phrases list
    '''    

    #A list which will contain all noun phrases of the current line
    each_line_noun_phrases = []
    
    #Split the line by spaces
    line = line.split(" ")

    #iterate over each word
    for each_word_index, each_word in enumerate(line):
        each_word_noun_phrase = ""
        
        #will use this variable to get the word that we want to work on. we will update it inside the whille loop too. 
        current_temp_index = each_word_index
        while True:
            
            word_to_search = line[current_temp_index]

            match = re.search(PATTERN, word_to_search)
            if match:
                # current_temp_index == each_word_index means if this is the first iteration of while loop and we are at the current for loop's word
                # and since noun phrases start with DT thats why it has to be DT
                # current_temp_index > each_word_index means if we have already seen a DT and this is not the first iteration of while loop
                # and the only other possiblities of noun phrases are NN and JJ...and NN is handled in a separate condition so this can only be JJ
                # ^^^  In both cases append the current temp word to word's noun phrase and 
                # increase the current_temp_index to continue looking for rest of the noun phrase 
                if (current_temp_index == each_word_index and match.group(2) == "DT") or (current_temp_index > each_word_index and match.group(2) == "JJ"):
                    each_word_noun_phrase = each_word_noun_phrase + " " + word_to_search
                    current_temp_index += 1

                # current_temp_index > each_word_index means if we have already seen a DT and this is not the first iteration of while loop
                # and the only other possiblities of noun phrases are NN and JJ...and JJ is already handled so this can only be NN. 
                # and NN is the the end of noun phrase.
                # so append the current temp word to word's noun phrase 
                # and break the while lop.

                elif current_temp_index > each_word_index and match.group(2) == "NN":                    
                    each_word_noun_phrase = each_word_noun_phrase + " " + word_to_search
                    each_word_noun_phrase = each_word_noun_phrase.strip()  #this is because of the way we add space while appending the next word (in the first line of both if and elif)
                    each_line_noun_phrases.append(each_word_noun_phrase)
                    break
                
                #if you find any other pos tag, break the while loop
                else:
                    break

            #if dont find any regex match then break the while loop. because each word in noun phrase will have a POS tag
            else:
                break

    return each_line_noun_phrases

def main():
    with open('wsj00-pos-oneline.txt') as f:
        noun_phrases = []
        for each_line in f:
            each_line_noun_phrases = extract_noun_phrases(each_line+' ')
            noun_phrases.append(each_line_noun_phrases)
            
            print("Line Text : ", each_line)
            print("Noun phrases of this line: ", each_line_noun_phrases)
            print()

if __name__ == '__main__':
    main()
