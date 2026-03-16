import pandas as pd
import pickle
import os

# Machine learning libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

# Create model folder if it doesn't exist
os.makedirs("model", exist_ok=True)

# Step 1: Load dataset
data = pd.read_csv("dataset/spam.csv")

# Step 2: Convert labels (ham = 0, spam = 1)
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

# Step 3: Separate input and output
X = data['message']   # Messages
y = data['label']     # Labels

# Step 4: Convert text messages to numerical features using TF-IDF
vectorizer = TfidfVectorizer(stop_words='english')
X_vectorized = vectorizer.fit_transform(X)

# Step 5: Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2, random_state=42
)

# Step 6: Train the Naive Bayes model
model = MultinomialNB()
model.fit(X_train, y_train)

# Step 7: Save trained model
pickle.dump(model, open("model/spam_model.pkl", "wb"))

# Step 8: Save vectorizer
pickle.dump(vectorizer, open("model/vectorizer.pkl", "wb"))

print("Model trained and saved successfully!")