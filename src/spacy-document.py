# import spacy library
import spacy

# load the nlp function from language model
nlp = spacy.load("en_core_web_lg")

# take 2 documents for simple similarity check
doc1 = nlp("I am venkat")
doc2 = nlp("venkat is studying nlp")
print("similarity using spacy is ", doc1.similarity(doc2))
