import spacy

nlp = spacy.load("en_core_web_sm")

sentence = input("Enter sentence: ")

doc = nlp(sentence)

print("\nNoun Phrases and Meanings:")

for chunk in doc.noun_chunks:
    print("Noun Phrase:", chunk.text)
    print("Root:", chunk.root.text)
    print("Meaning:", "Entity or concept represented by '" + chunk.text + "'")
    print()