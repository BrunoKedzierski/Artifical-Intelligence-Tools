import csv as read_csv
import json
import pprint
from random import shuffle
import matplotlib.pyplot as plt

# training_set_path = input("Specify training set location:")
# test_set_path = input("Specify test set location:")
import numpy
import numpy as np
from matplotlib import colors
from matplotlib.cm import get_cmap

from KClassifier import KClassifier

training_set_path = 'iris.txt'
# test_set_path = 'iris_test.txt'

with open(training_set_path, 'r') as file:
    csv_training_file_content = read_csv.reader(file)
    training_rows = list(csv_training_file_content)

# with open(test_set_path, 'r') as file:
#    csv_test_file_content = read_csv.reader(file)
#    test_rows = list(csv_test_file_content)

training_rows = [list(map(float, vector[:-1])) for vector in training_rows]
# test_rows = [list(map(float, vector[:-1])) for vector in test_rows]

shuffle(training_rows)

classifier = KClassifier(training_rows, 3)
classifier.initialize_clusters()
classifier.group()



# 1. Choose your desired colormap
cmap = plt.get_cmap('tab20b')

# 2. Segmenting the whole range (from 0 to 1) of the color map into multiple segments
slicedCM = list(cmap(np.linspace(0, 1, 15)))
slicedCM = list(cmap(np.linspace(0, 1, 15)))

for k, v in classifier.clusters.items():
    print(f"Centroid coordinates: {k} \n Observations: {v} ")
    vals_x = []
    vals_y = []
    vals_y1 = []
    vals_x1 = []
    for li in v:
        vals_x.append(li[0])
        vals_y.append(li[1])
        vals_x1.append(li[2])
        vals_y1.append(li[3])
    centroid_x = k[0]
    centroid_y = k[1]
    centroid_x1 = k[2]
    centroid_y1 = k[3]
    plt.subplot(1, 2, 1)
    plt.xlabel("sepal lenght")
    plt.ylabel("sepal width")
    plt.scatter(vals_x, vals_y, color=slicedCM.pop())
    plt.scatter(centroid_x, centroid_y, color='k')
    plt.subplot(1, 2, 2)
    plt.xlabel("petal lenght")
    plt.ylabel("petal width")
    plt.scatter(vals_x1, vals_y1, color=slicedCM.pop())
    plt.scatter(centroid_x1, centroid_y1, color='k')

plt.subplots_adjust(left=0.125,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.5,
                    hspace=0.35)
plt.show()
