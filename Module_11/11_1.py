#LOGISTIC REGRESSION MODELLING

# Train a logistic regression classifier to predict whether a flower is iris virginica or not


#How to Perform Logistic Regression Using Python
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt
iris = datasets.load_iris()

''''Loads the Iris dataset using datasets.load_iris() 
and extracts the feature X (petal width) and
 target y (1 if Iris virginica, else 0)'''
X = iris["data"][:, 3:]
y = (iris["target"] == 2).astype(int)

# Train a logistic regression classifier
#Makes a prediction for a new 
#example with petal width 2.6 (clf.predict([[2.6]])) and prints the result.
clf = LogisticRegression()
clf.fit(X,y)
example = clf.predict(([[2.6]]))
print(example)

# Using matplotlib to plot the visualization
X_new = np.linspace(0,3,1000).reshape(-1,1)
y_prob = clf.predict_proba(X_new)
print(y_prob)
plt.plot(X_new, y_prob[:,1], "g-", label="virginica")
plt.show()

