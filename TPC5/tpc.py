import spacy

nlp = spacy.load("pt_core_news_lg")

text = ('''O Daniel e o André foram a Ponte de Lima a pé.''')
doc = nlp(text)

with doc.retokenize() as retokenizer:
    for entity in doc.ents:
        retokenizer.merge(entity)
    
print("TOKEN            POS       LEMMA\n===============================")
for token in doc:
    print(f"{str(token):<15} {token.pos_:<10} {token.lemma_}")