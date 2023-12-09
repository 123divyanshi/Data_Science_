#DIMENSION REDUCTION
#Demonstrate How you will  Identify Multicollinearity R/Python

import pandas as pd
import numpy as np

# Load the iris dataset from sklearn
from sklearn.datasets import load_iris

# Load the iris dataset
iris = load_iris()
iris_data = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Display the first few rows of the dataset
print(iris_data.head())

# Create a correlation matrix
correlation_matrix = iris_data.corr()

# Display the correlation matrix
print(correlation_matrix)

# Check for high correlations (threshold can be adjusted)
threshold = 0.5  # Adjust the threshold value
#Here, a threshold value of 0.5 is set. The np.where function is used to find 
#indices where the absolute correlation values are greater than the threshold.
high_correlations = np.where(np.abs(correlation_matrix) > threshold)

# Filter for pairs of features with high correlations
high_corr_list = [(correlation_matrix.columns[x], correlation_matrix.columns[y]) for x, y in zip(*high_correlations) if x != y and x < y]

# Print pairs of highly correlated features
if not high_corr_list:
    print("No pairs of highly correlated features found with the given threshold.")
else:
    print("Pairs of highly correlated features:")
    for pair in high_corr_list:
        print(pair)

