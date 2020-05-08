import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import random


MAX_CLUSTERS = 10
cmap = cm.get_cmap('tab10', MAX_CLUSTERS)
feature_columns = ['gdp_per_capita', 'total_cases_per_M', 'pop_65']
data = pd.read_csv("../creating_dataset/data/dev_corona 2.0.csv")[feature_columns].to_numpy()
data_countries = data[:, 0:3].astype(np.float)

def min_max_scale(data):
    mins = np.nanmin(data, axis=0)
    maxs = np.nanmax(data, axis=0)
    return np.divide(np.subtract(data, mins), np.subtract(maxs, mins))

def elbow_point_plot(cluster, errors):
    plt.clf()
    plt.plot(cluster, errors)
    plt.xlabel('Number of Clusters')
    plt.ylabel('Inertia')
    plt.show()

def calculate_means(data, centroid_indices):
    # this gives mean of each feature for each cluster
    feature_means = [np.nanmean(data[centroid_indices == i], axis=0) for i in range(4)]
    return feature_means

def visualize_countries_clusters(data, centroids=None, centroid_indices=None):
    def plot_countries(fig, color_map=None):
        x, y, z = np.hsplit(data, 3)
        fig.scatter(x, y, z, c=color_map)

    def plot_clusters(fig):
        x, y, z = np.hsplit(centroids, 3)
        fig.scatter(x, y, z, c="black", marker="x", alpha=1, s=200)

    plt.clf()
    cluster_plot = centroids is not None and centroid_indices is not None

    ax = plt.figure().add_subplot(111, projection='3d')
    colors_s = None

    if cluster_plot:
        if max(centroid_indices) + 1 > MAX_CLUSTERS:
            print(f"Error: Too many clusters. Please limit to fewer than {MAX_CLUSTERS}.")
            exit(1)
        colors_s = [cmap(l / MAX_CLUSTERS) for l in centroid_indices]
        plot_clusters(ax)

    plot_countries(ax, colors_s)

    ax.set_xlabel(feature_columns[0])
    ax.set_ylabel(feature_columns[1])
    ax.set_zlabel(feature_columns[2])

    # Helps visualize clusters
    plt.gca().invert_xaxis()
    plt.show()

def main():
    country_data = min_max_scale(data_countries)
    visualize_countries_clusters(country_data)

    inertias = []
    cluster = [n for n in range(2, MAX_CLUSTERS)]
    for i in range(2, MAX_CLUSTERS):
        kmeans = KMeans(n_clusters=i).fit(country_data)
        inertias.append(kmeans.inertia_)

    elbow_point_plot(cluster, inertias)

    kmeans_best = KMeans(n_clusters=3).fit(country_data)
    visualize_countries_clusters(country_data, centroids=kmeans_best.cluster_centers_, centroid_indices=kmeans_best.labels_)
    calculate_means(data, kmeans_best.labels_)

if __name__ == '__main__':
    main()