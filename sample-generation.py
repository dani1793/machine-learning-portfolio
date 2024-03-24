import numpy as np
import pandas as pd
import random

def generateData(mean, covariance_matrix, num_samples=2**20): 
    
    samples = np.random.multivariate_normal(mean, covariance_matrix, num_samples)
    return samples

# Set the mean and covariance matrix for the multivariate normal distribution
mean1 = [0, 0, 0, 0, 0]
covariance_matrix1 = [
    [1, 0.5, 0.3, 0.2, 0.1],
    [0.5, 1, 0.4, 0.3, 0.2],
    [0.3, 0.4, 1, 0.5, 0.3],
    [0.2, 0.3, 0.5, 1, 0.4],
    [0.1, 0.2, 0.3, 0.4, 1]
]  # Example covariance matrix


# Set the mean and covariance matrix for the multivariate normal distribution
mean2 = [5, 5, 7, 7, 8]
covariance_matrix2 = [
    [1, 0.2, 0.5, 0.15, 0.1],
    [0.2, 1, 0.8, 0.3, 0.2],
    [0.5, 0.8, 1, 0.6, 0.1],
    [0.15, 0.3, 0.6, 1, 0.4],
    [0.1, 0.2, 0.1, 0.4, 1]
]  # Example covariance matrix

# Set the mean and covariance matrix for the multivariate normal distribution
mean3 = [5, 3, 3, 2, 1]
covariance_matrix3 = [
    [1, 0.2, 0.5, 0.15, 0.1],
    [0.2, 1, 0.8, 0.31, 0.2],
    [0.5, 0.8, 1, 0.6, 0.53],
    [0.15, 0.31, 0.6, 1, 0.33],
    [0.1, 0.2, 0.53, 0.33, 1]
]  # Example covariance matrix


sample1 = generateData(mean1, covariance_matrix1)
sample2 = generateData(mean2, covariance_matrix3)
sample3 = generateData(mean2, covariance_matrix3)

samplesWithoutId = np.concatenate((sample1, sample2, sample3), axis=0)
print(samplesWithoutId.shape)
ids = np.arange(samplesWithoutId.shape[0])
np.random.shuffle(ids)

df = pd.DataFrame(samplesWithoutId, columns=['x1', 'x2', 'x3', 'x4', 'x5'])
df.insert(0, "ids", ids)

df.to_csv('multivariate_normal_data.csv', index=False)

print("Data saved successfully.")