import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Paths to saved model and vectorizer
MODEL_PATH = "clf_richer_model.pkl"
VECTORIZER_PATH = "vectorizer.pkl"

# Load the trained model and vectorizer
with open(MODEL_PATH, "rb") as model_file:
    clf = pickle.load(model_file)

with open(VECTORIZER_PATH, "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

def preprocess_text_basic_v2(text):
    tokens = text.lower().split()
    return " ".join(tokens)

def determine_sentiment(text):
    # Preprocess the text
    preprocessed_text = preprocess_text_basic_v2(text)
    # Convert the text to a TF-IDF vector
    text_vector = vectorizer.transform([preprocessed_text])
    # Predict sentiment using the trained model
    prediction = clf.predict(text_vector)[0]
    
    return prediction

if __name__ == "__main__":
    sample_review = "it was average"
    sentiment = determine_sentiment(sample_review)
    print(f"The sentiment of the review is: {sentiment}")
