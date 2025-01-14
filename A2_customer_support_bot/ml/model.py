import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Sample data
texts = [
    "I love this product!",
    "This is the worst experience ever.",
    "Amazing quality and great service.",
    "Terrible, I hate it here.",
    "The support team was very helpful.",
    "Worst decision of my life."
]
labels = [1, 0, 1, 0, 1, 0]  # 1 = positive, 0 = negative

# Preprocess and train
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)
model = MultinomialNB()
model.fit(X, labels)

# Save model and vectorizer together
with open('ml/model.pkl', 'wb') as f:
    pickle.dump((model, vectorizer), f)

print("Model and vectorizer saved to 'ml/model.pkl'")
