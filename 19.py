from nltk.wsd import lesk
from nltk.tokenize import word_tokenize

sentence = input("Enter sentence: ")
word = input("Enter word to disambiguate: ")

tokens = word_tokenize(sentence)

sense = lesk(tokens, word)

if sense:
    print("\nWord:", word)
    print("Synset:", sense.name())
    print("Definition:", sense.definition())
else:
    print("No sense found.")