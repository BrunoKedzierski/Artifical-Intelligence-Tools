from operator import itemgetter

#Caluclate euclidean distance between two vectors
def calc_euclidean_distance(v1, v2):
    sum = 0

    for pos1, pos2 in zip(v1, v2):

        sum += (float(pos2) - float(pos1)) ** 2
    return sum


def classify_k_nearest_neighbors(v1, training_set, k, categories):
    calculated_distances = []
    for traing_observation in training_set:
        distance_sum = calc_euclidean_distance(v1[0:-1], traing_observation[0:-1])
        calculated_distances.append([distance_sum,traing_observation[-1]])
    category_count = dict.fromkeys(categories,0)
    calculated_distances.sort()

    for row in calculated_distances[0:k]:
        category_count[row[1]] +=1
    sorted_keyes = sorted(category_count.items(), key = itemgetter(1), reverse = True)
    return sorted_keyes[0][0]
