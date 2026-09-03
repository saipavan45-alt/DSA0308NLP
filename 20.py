from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

n = int(input("Enter number of documents: "))

documents = []

for i in range(n):
    documents.append(input("Enter document " + str(i + 1) + ": "))

query = input("Enter search query: ")

vectorizer = TfidfVectorizer()

tfidf = vectorizer.fit_transform(documents)
query_vector = vectorizer.transform([query])

scores = cosine_similarity(query_vector, tfidf)[0]

ranking = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)

print("\nDocument Ranking:")

for index, score in ranking:
    print("Document", index + 1, "Score:", round(score, 4))