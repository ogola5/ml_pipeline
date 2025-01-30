import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

def train():
    # Load cleaned data
    df = pd.read_csv("data/processed/cleaned_content.csv")
    
    # Example: Predict "subject" from "cleaned_content" (customize your target)
    X = df['cleaned_content']
    y = df['subject']  # Replace with your target (e.g., "grade", "topic")
    
    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer(max_features=1000)
    X_tfidf = vectorizer.fit_transform(X)
    
    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2)
    
    # Train a classifier
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)
    
    # Save model and vectorizer
    joblib.dump(model, "data/models/subject_classifier.pkl")
    joblib.dump(vectorizer, "data/models/tfidf_vectorizer.pkl")
    print(f"Model trained. Accuracy: {model.score(X_test, y_test):.2f}")

if __name__ == "__main__":
    train()