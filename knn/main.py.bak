import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def calc_euclidean_distance(v1, v2):
    dist = v2 - v2
    dist = dist**2
    return dist

def knn_test_classifier(v_to_predict, training,k,index_of_outcome):
    training_no_outcome = training[0:index_of_outcome]
    v_to_predict= test[0:index_of_outcome]
    distances_list = []
    for vector in training_no_outcome:
        distances_list.append(calc_euclidean_distance(v_to_predict,vector))
    distances_list.sort()




iris_file = pd.read_csv("iris.csv")

train, test  = train_test_split(iris_file, test_size=0.3)

train_np_array = train.to_numpy()

test_np_array = test.to_numpu()