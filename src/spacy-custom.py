# import spacy and language libraries
import spacy
from spacy.language import Language


# my custom component that classifies the parts of speech for each token in given corpus
@Language.component("custom_component")
def custom_component(doc):
    print("part-of-speech tags are:", [token.pos_ for token in doc])
    if len(doc) < 5:
        print("Given corpus is small.")
    return doc


# load the nlp function from language model
nlp = spacy.load("en_core_web_lg")
# adding custom component in the pipeline
print(nlp.pipe_names)
nlp.add_pipe("custom_component")
# sample corpus
doc = nlp("venkat is studying nlp")
