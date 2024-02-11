#!/usr/bin/env python3
'''
NAME
    word_freq - Calculates word frequency in a text

SYNOPSIS
    word_freq [options] input_files
    options: 
        -m 20 : Show 20 most common
        -n : Alphabetical order
        -o : Number of occurrences (ascending)
        -p : Number of occurrences (descending)
        -q : Swap word and number position
Description'''

from jjcli import *
from collections import Counter
import re

cl = clfilter("qponm:",doc= __doc__)


def tokenizer(text):
   tokens = re.findall(r'\w+(?:\-\w+)?|[,;.:_?!—]+',text)
   return tokens


def my_print(content,option):
    if option=="-n":
        content = sorted(content, key=lambda x: x[0])
    if option=="-o":
        content = sorted(content, key=lambda x: x[1])
    if option=="-p":
        content = sorted(content, key=lambda x: x[1], reverse=True)
    
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
    if "-m" in cl.opt:
        my_print(ocorr.most_common(int(cl.opt.get("-m"))),"")
    else:
        if "-n" in cl.opt:
            option = "-n"
        elif "-o" in cl.opt:
            option = "-o"
        elif "-p" in cl.opt:
            option = "-p"
        elif "-q" in cl.opt:
            option = "-q"
        
        my_print(ocorr.items(),option)