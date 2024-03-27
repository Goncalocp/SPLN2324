#!/usr/bin/env python3

import spacy, sys
from spacy import displacy

with open(sys.argv[1]) as file:
    content = file.read()

nlp = spacy.load("pt_core_news_lg")

doc = nlp(content)
# displacy.serve(doc, style='dep')

with doc.retokenize() as retokenizer:
    for entity in doc.ents:
        retokenizer.merge(entity)

friends = {}

print("TOKEN   POS   LEMMA   DEP")
print('-' * 27)
for sentence in doc.sents:
    names = []
    for token in sentence:
        
        if token.is_space:
            continue
        
        if token.pos_ == 'PROPN':
            print(f"{str(token)}   {token.pos_}   {token.ent_type_}   {token.dep_}")
            current_name = str(token)

            for name in names:
                if current_name != name:
                    if (current_name,name) not in friends:
                        if (name,current_name) in friends:
                            friends[(name,current_name)] += 1
                        else:
                            friends[(current_name,name)] = 1
                    else:
                        friends[(current_name,name)] += 1
                        
            if current_name not in names:
                names.append(current_name)    

        else:
            print(f"{str(token)}   {token.pos_}   {token.lemma_}   {token.dep_}")
        
    print()

print(friends)