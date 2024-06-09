import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.classify import NaiveBayesClassifier
import csv

# Download stopwords
nltk.download('stopwords')
nltk.download('punkt')

# Load dataset
with open('expanded_dataset.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Skip header row
    reviews = [(row[0], row[1]) for row in reader]

# Preprocess reviews
stop_words = set(stopwords.words('english'))
tokenized_reviews = [(dict([(word, True) for word in word_tokenize(review[0].lower()) if word.isalpha() and word not in stop_words]), review[1]) for review in reviews]

# Splitting data into training and testing
train_data = tokenized_reviews[:int(0.8 * len(tokenized_reviews))]
test_data = tokenized_reviews[int(0.8 * len(tokenized_reviews)):]

# Train the model
classifier = NaiveBayesClassifier.train(train_data)

# Test the model
accuracy = nltk.classify.accuracy(classifier, test_data)
print(f"Accuracy: {accuracy}")

# Predict sentiment
def predict_sentiment(text):
    words = word_tokenize(text.lower())
    words = [word for word in words if word.isalpha() and word not in stop_words]
    return classifier.classify(dict([word, True] for word in words))

# Test the predict_sentiment function
test_sentence = "GREAT"
print(f"'{test_sentence}' is {predict_sentiment(test_sentence)}")
