import pandas as pd
import matplotlib.pyplot as plt
from joblib import load

from data_prep import data_prep
from iforest import isolation_forest

def two_d_plot(X, top_indices):
    '''Visualizing anomalies using PCA reduction'''
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import StandardScaler

    X = StandardScaler().fit_transform(X)
    pca = PCA(n_components=2)
    X = pca.fit_transform(X)

    plt.scatter(X[:, 0], X[:, 1], s=2)
    plt.scatter(X[top_indices, 0], X[top_indices, 1], c='r', s=10)
    plt.show()

def anomaly_output():
    '''Outputting and plotting top anomalies'''
    top_count = 5 

    df = pd.read_csv('ueba.csv')
    X = data_prep(df).to_numpy() # data preprocessing

    #iforest = isolation_forest(X) if necessary to train again
    iforest = load("iforest.joblib") # already trained model

    anomaly_scores = list(zip(list(range(X.shape[0])), iforest.score_samples(X))) # No. of a record and its anomaly score
    anomaly_scores.sort(key=lambda t: t[1])

    top_indices = [r_s[0] for r_s in anomaly_scores[:top_count]] # indices of top anomalies
    top_scores = [r_s[1] for r_s in anomaly_scores[:top_count]] # scores of top anomalies
    
    anomaly_report = pd.DataFrame({'# of record': top_indices, 'Anomaly score': top_scores})
    print(anomaly_report)

    two_d_plot(X, top_indices) # plotting inliers and outliers

if __name__ == '__main__':
    anomaly_output()