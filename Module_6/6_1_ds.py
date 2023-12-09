#NAÏVE BAYES CLASSIFICATION

#Demonstrate application of Naïve Bayes Using Python

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Sample data for text classification 
#with text samples and corresponding labels
corpus = [
    ("I love Python", "positive"),
    ("Naive Bayes is interesting", "positive"),
    ("I dislike bugs", "negative"),
    ("Machine learning is fascinating", "positive"),
    ("I hate errors", "negative")
]

# Separate text and labels
X, y = zip(*corpus)

# Convert text data to a bag-of-words representation
'''Use CountVectorizer to convert the
 text data into a bag-of-words representation (X_bow), which
 represents each document as a vector of word frequencies.'''
vectorizer = CountVectorizer()
X_bow = vectorizer.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_bow, y, test_size=0.2, random_state=42)

# Create a Naive Bayes classifier
#Create a Multinomial Naive Bayes classifier,
#which is commonly used for text classification tasks.
nb_classifier = MultinomialNB()

# Train the classifier
nb_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = nb_classifier.predict(X_test)
'''Calculate the accuracy and generate a 
   classification report for evaluating the performance of the model.'''

# Evaluate the performance
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print("Accuracy:", accuracy)
print("\nClassification Report:")
print(report)
