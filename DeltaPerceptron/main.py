import csv as read_csv

training_set_path = input("Specify training set location:")
test_set_path = input("Specify test set location:")

with open(training_set_path, 'r') as file:
    csv_training_file_content = read_csv.reader(file)
    training_rows = list(csv_training_file_content)


with open(test_set_path, 'r') as file:
    csv_test_file_content = read_csv.reader(file)
    test_rows = list(csv_test_file_content)


perceptron = perceptron(training_rows[1:], 0.01, 'Iris-virginica', 'Iris-versicolor')

for i in range(0,500):
    perceptron.learn()

perceptron.test(test_rows[1:])