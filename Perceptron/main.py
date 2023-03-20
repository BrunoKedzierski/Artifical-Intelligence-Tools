import csv as read_csv
from random import shuffle

from perceptron import Perceptron

#training_set_path = input("Specify training set location:")
#test_set_path = input("Specify test set location:")

training_set_path = 'iris_training.txt'
test_set_path = 'iris_test.txt'

with open(training_set_path, 'r') as file:
    csv_training_file_content = read_csv.reader(file)
    training_rows = list(csv_training_file_content)


with open(test_set_path, 'r') as file:
    csv_test_file_content = read_csv.reader(file)
    test_rows = list(csv_test_file_content)


training_rows = [ list(map(float, vector)) for vector in training_rows[1:]]
test_rows = [ list(map(float, vector)) for vector in test_rows[1:]]

shuffle(training_rows)
shuffle(test_rows)
perceptron = Perceptron(training_rows,1,1)
perceptron.learn()
perceptron.test(test_rows)


