import pandas as pd
import os

def collect_feedback(feedback_data):
    """Append feedback data to a CSV for retraining."""
    feedback_file = "data/processed/feedback.csv"
    
    if os.path.exists(feedback_file):
        df = pd.read_csv(feedback_file)
    else:
        df = pd.DataFrame(columns=["doc_id", "correct_subject", "feedback_text"])
    
    df = pd.concat([df, pd.DataFrame([feedback_data])])
    df.to_csv(feedback_file, index=False)
    print("Feedback saved.")

# Example usage:
if __name__ == "__main__":
    feedback = {
        "doc_id": "Grade9_math_syllabus",
        "correct_subject": "Mathematics",  # Corrected label
        "feedback_text": "This syllabus was misclassified as Physics."
    }
    collect_feedback(feedback)