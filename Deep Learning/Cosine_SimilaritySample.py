
documents=(
    "Today its Sunday",
    "Tomorrow its Monday",
    "Yesterday it was Saturday",
    "We met on Sunday"
)

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#tone frequency Inverse document frequency
tfidf_vect = TfidfVectorizer()
tfidf_matrix = tfidf_vect.fit_transform(documents)
print(tfidf_matrix.shape)

print(cosine_similarity(tfidf_matrix[0:],tfidf_matrix))


