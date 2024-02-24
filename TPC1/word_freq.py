#!/usr/bin/env python3
'''
NAME
    word_freq - Calculates word frequency in a text

SYNOPSIS
    word_freq [options] input_files

DESCRIPTION

    options: 
        -m 20 : Show 20 most common
        
        -n : Alphabetical order

        -o : Number of occurrences (ascending)
        
        -p : Number of occurrences (descending)
        
        -q : Swap word and number position
        
        -r s : Number of occurrences of words with the substring s
        
        -s : Ignore case
'''

from jjcli import *
from collections import Counter
import re

cl = clfilter("sr:qponm:",doc= __doc__)


def tokenizer(text):
   tokens = re.findall(r'\w+(?:\-\w+)?|[,;.:_?!—]+',text)
   return tokens


def merge_words(content):
    result_dict = {}
    
    for word, occurrences in content:
        word_lower = word.lower()
        if word_lower in result_dict:
            result_dict[word_lower]['occurrences'] += occurrences
        else:
            result_dict[word_lower] = {'word': word, 'occurrences': occurrences}
    
    result_list = [(word_info['word'], word_info['occurrences']) for word_info in result_dict.values()]
    
    return result_list


def my_print(content,option,substring=""):
    
    if option=="-n":
        content = sorted(content, key=lambda x: x[0])
    elif option=="-o":
        content = sorted(content, key=lambda x: x[1])
    elif option=="-p":
        content = sorted(content, key=lambda x: x[1], reverse=True)
    elif option=="-r":
        content = [(word, occurrence) for word, occurrence in content if substring in word]
        content = sorted(content, key=lambda x: x[1], reverse=True)
    elif option=="-s":
        content = merge_words(content)
        content = sorted(content, key=lambda x: x[0])
        
    max_word_length = max(len(word) for word, _ in content)
    max_occurrence_length = max(len(str(occurrence)) for _, occurrence in content)
    
    for word, occurrence in content:
        if option == "-q":
            print(f'{word:<{max_word_length}}  {occurrence:>{max_occurrence_length}}')
        else:
            print(f'{occurrence:>{max_occurrence_length}}    {word:<{max_word_length}}')


for txt in cl.text():
    
    word_list = tokenizer(txt) 
    ocorr = Counter(word_list)
    option = next(iter(cl.opt.keys()), None)
    
    if option == "-m":
        my_print(ocorr.most_common(int(cl.opt.get("-m"))),"")
    elif option == "-r":
        my_print(ocorr.items(),option,cl.opt.get("-r"))
    else:
        my_print(ocorr.items(),option)