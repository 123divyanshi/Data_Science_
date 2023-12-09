#8 "k mean clustering"
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv("incomee.csv")

# Drop unnecessary columns
df = df.drop(columns=['Name', 'Unnamed: 3'], errors='ignore')

# Visualize the data
#This code creates a scatter plot to visualize the relationship between 'Age' and 'Income($)'.
plt.scatter(df.Age, df['Income($)'])
plt.xlabel('Age')
plt.ylabel('Income($)')
plt.title('Scatter plot of Age vs Income')
plt.show()

# Use KMeans for clustering
''' It specifies n_clusters=3 to create three clusters and n_init=10 
to run the k-means algorithm with 10 different centroid seeds to find the best initialization'''
numeric_cols = df.select_dtypes(include=['number']).columns
kmeans = KMeans(n_clusters=3, n_init=10)
kmeans.fit(df[numeric_cols])

# Add a new column 'Cluster' to the dataframe to store the cluster assignment
'''The cluster assignments are stored in a new column 'Cluster' in the DataFrame.
 Each row now has a label indicating which cluster it belongs to based on the k-means clustering.'''
df['Cluster'] = kmeans.labels_

# Visualize the clusters
plt.scatter(df.Age, df['Income($)'], c=df['Cluster'], cmap='rainbow')
plt.xlabel('Age')
plt.ylabel('Income($)')
plt.title('KMeans Clustering Result')
plt.show()

# Display the clustered data
print(df)

