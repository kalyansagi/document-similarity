# import spacy library
import spacy

# load the nlp function from language model
nlp = spacy.load("en_core_web_lg")

corpus = "My name is venkat. I am studying NLP course at KSU!"

tokens = []
doc = nlp(corpus)
for token in doc:
    tokens.append(token)
print(tokens)
