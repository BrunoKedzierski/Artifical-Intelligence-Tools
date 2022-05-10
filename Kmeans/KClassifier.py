import itertools
from random import sample


def calc_euclidean_distance(v1, v2):
    sum_distance = 0
    for pos1, pos2 in zip(v1, v2):
        sum_distance += (float(pos2) - float(pos1)) ** 2
    return sum_distance


def calculate_centroid(members):
    partial_sum = [sum(e) for e in zip(*members)]
    return tuple([e / len(members) for e in partial_sum])


def closest_centroid(vector, centroids):
    distances = {}
    for centroid in centroids:
        distances[calc_euclidean_distance(vector,centroid)] = centroid
    return tuple(distances[min(distances.keys())])

def squared_error(cluster):
    sum = 0

    for v1,v2 in itertools.combinations(cluster, 2):
        sum+= calc_euclidean_distance(v1,v2)**2
    return sum


class KClassifier:

    def __init__(self, observations, k):
        self.observations = observations
        self.k = k
        self.clusters = {}
        self.cluster_indexes = []

    def initialize_clusters(self):
        self.cluster_indexes = sample(range(0, len(self.observations)), self.k)
        self.clusters.clear()
        for i in self.cluster_indexes:
            ls = [self.observations[i]]
            self.clusters[tuple(self.observations[i])] = ls

    def group(self):
        while True:
            prev_clusters = self.clusters
            for k, v in list(self.clusters.items()):
                if len(v) != 1:
                    self.clusters[calculate_centroid(v)] = self.clusters.pop(k)
            self.clusters = {key: [] for key in self.clusters
                            }
            for ob in self.observations:
                closest_centr = closest_centroid(ob, self.clusters.keys())
                self.clusters[closest_centr].append(ob)
            if sorted(self.clusters.values()) == sorted(prev_clusters.values()):
                break
            for k, v in self.clusters.items():
                print(f"Centroid coordinates: {k} \n Observations: {v}  \n Squared error {squared_error(v)}")

