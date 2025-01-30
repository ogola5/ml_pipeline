import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

def retrain():
    # Load existing data
    df = pd.read_csv("data/processed/cleaned_content.csv")
    
    # Load feedback data
    feedback_df = pd.read_csv("data/processed/feedback.csv")
    merged_df = pd.merge(df, feedback_df, on="doc_id", how="left")
    
    # Update labels using feedback
    merged_df['subject'] = merged_df['correct_subject'].combine_first(merged_df['subject'])
    
    # Retrain the model
    vectorizer = joblib.load("data/models/tfidf_vectorizer.pkl")
    X = vectorizer.transform(merged_df['cleaned_content'])
    y = merged_df['subject']
    
    model = joblib.load("data/models/subject_classifier.pkl")
    model.fit(X, y)  # Full retraining (replace with partial_fit for incremental learning)
    
    # Save updated model
    joblib.dump(model, "data/models/subject_classifier.pkl")
    print("Model retrained with feedback data.")

if __name__ == "__main__":
    retrain()