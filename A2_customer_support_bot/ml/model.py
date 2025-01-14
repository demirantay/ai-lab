import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Sample data
texts = [
    "I love this product!",
    "This is the worst experience ever.",
    "Amazing quality and great service.",
    "Terrible, I hate it here.",
    "The support team was very helpful.",
    "Worst decision of my life."
]
labels = [1, 0, 1, 0, 1, 0]  # 1 = Positive, 0 = Negative

# Step 1: Text processing
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(texts)

# Step 2: Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.2, random_state=42)

# Step 3: Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save the model and vectorizer
joblib.dump(model, "ml/model.pkl")
joblib.dump(vectorizer, "ml/vectorizer.pkl")
