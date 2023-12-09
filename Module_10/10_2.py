
#Demonstrate HOW you’ll apply PRINCIPAL COMPONENTS ANALYSIS Using Python
#PCA is a dimensionality reduction technique commonly 
#used for feature extraction and visualization.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.show()

from sklearn.datasets import load_breast_cancer
cancer=load_breast_cancer()
# cancer.keys()
# print(cancer['DESCR'])

df=pd.DataFrame(cancer['data'],columns=cancer['feature_names'])
print(df.head(5))
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

#The data is standardized using 
# StandardScaler to have a mean of 0 and a standard deviation of 1.
scaler=StandardScaler()
print(scaler.fit(df))
scaled_data=scaler.transform(df)
# print(scaled_data)

#PCA is applied with the request for two principal 
# components and the transformed data is stored in x_pca
from sklearn.decomposition import PCA
pca=PCA(n_components=2)
print(pca.fit(scaled_data))
x_pca=pca.transform(scaled_data)

print(scaled_data)
print(x_pca)

plt.figure(figsize=(8,6))
plt.scatter(x_pca[:,0],x_pca[:,1],c=cancer['target'])
plt.xlabel('First principle component')
plt.ylabel('Second principle component')
plt.show()