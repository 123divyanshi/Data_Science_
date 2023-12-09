#How to Perform Binning Based on Predictive Value Using Python

#This Python code demonstrates how to perform binning
# based on predictive values using a decision tree classifier.

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Sample data
np.random.seed(42)
data = pd.DataFrame({
    'Feature': np.random.randn(1000),  # Replace this with your actual feature
    'Target': np.random.choice([0, 1], size=1000)  # Replace this with your actual target variable
})

#The data is split into training and testing sets.

train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

X_train = train_data[['Feature']]
y_train = train_data['Target']

#A decision tree classifier is trained on the training data.
classifier = DecisionTreeClassifier(max_depth=3)
classifier.fit(X_train, y_train)

#Predicting probabilities and performing binning:
test_data['Predicted_Probability'] = classifier.predict_proba(test_data[['Feature']])[:, 1]
bin_edges = [0, 0.25, 0.5, 0.75, 1.0]

test_data['Binned_Feature'] = pd.cut(test_data['Predicted_Probability'], bins=bin_edges, labels=['Very Low','Low', 'Medium', 'High'])

# Display the results
print(test_data[['Feature', 'Predicted_Probability', 'Binned_Feature', 'Target']])