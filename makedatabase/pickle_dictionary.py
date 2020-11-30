import re, random, pickle

def random_from_dict(d, n):
    random_dict = {} 
    for i in range(n):
        k, v = random.choice(list(d.items()))
        random_dict[k] = v 
    return random_dict


def sktdict_to_dict(in_lines):
    logfile = open('logfile2.txt','w', encoding='utf8')
    words = {}
    for line1 in in_lines:
        # cleaning steps
        line2 = re.sub(r"\t"," ", line1)
        line3 = line2.rstrip()
        line4 = re.sub(r",+$","", line3)
        # print('line4')
        # print(line4)
        line = re.sub(r",,",",", line4)
        # split and parse info steps 
        tmp = line.split(',')
        if len(tmp) < 4:
            # if not tmp[0] or not tmp[1] or not tmp[2] or not tmp[3]:
            logfile.write('ERROR: INDEX OUT OF RANGE')
            logfile.write(', '.join(tmp))
            logfile.write('\n')
            # print('ERROR: INDEX OUT OF RANGE', file=open('logfile.txt', 'a', encoding='utf8'))
            #print(tmp, file=open('logfile.txt', 'a', encoding='utf8'))
            continue 
        #print(tmp, file=open('logfile.txt', 'a', encoding='utf8'))
        word_no = tmp[0]
        word = tmp[1] + ' ' + tmp[2] + '.'
        definitions = '; '.join(tmp[3:len(tmp)])
        flashcard = word + ', ' + definitions
        words[word_no] = flashcard
    logfile.close()
    return words

# some additional functions to create flashcards from random selections from the dictionary 
# randomly select n words from dictionary with between l and k definitions

def definition_count(v):
    count = len(v.split(';'))
    print('count:' + v + '*' + str(count))
    return count

def random_from_dict_limited(d, n, l, m):
    random_dict = {} 
    for i in range(n):
        k, v = random.choice(list(d.items()))
        count = definition_count(v)
        # print(l, count, m)
        if l <= count and count <= m:
            random_dict[k] = v 
    return random_dict


# MAIN

# read into a list all the entries from a small extract of the DCS Sanskrit dictionary 
infile = open ("C:\\PYTHON\\FLASHCARDS_FROM_DICTIONARY_2\\dictionary.csv", "r", encoding='utf8')
in_lines = infile.readlines() 
infile.close()
in_lines.pop(0)

# create a python dict from a list 
words = sktdict_to_dict(in_lines)

# PICKLED DICTIONARY:
# what is inside:
# flashcard = word + ', ' + definitions
# words[word_no] = flashcard
print('PICKLING DICTIONARY')
filename = 'sktdictionary.bin'
outfile = open(filename,'wb')
pickle.dump(words,outfile)
outfile.close()

quit() 

# unpickling dictionary 
binary_file = open('sktdictionary.bin', mode='rb')
pickled_dictionary = pickle.load(binary_file)
binary_file.close()
print(pickled_dictionary)
