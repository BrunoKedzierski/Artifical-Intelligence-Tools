import csv as read_csv
from random import shuffle
from knn_classifier import classify_k_nearest_neighbors


k = int(input("Specify the number of neighbors (k):"));

training_set_path = input("Specify training set location:")
test_set_path = input("Specify test set location:")

with open(training_set_path, 'r') as file:
    csv_training_file_content = read_csv.reader(file)
    training_rows = list(csv_training_file_content)


with open(test_set_path, 'r') as file:
    csv_test_file_content = read_csv.reader(file)
    test_rows = list(csv_test_file_content)

shuffle(training_rows[1:])
shuffle(test_rows[1:])

#outcome categories
categories = set()

for row in training_rows:
    categories.add(row[4])

correct = 0
for row in test_rows[1:]:
    guess = classify_k_nearest_neighbors(row,training_rows[1:],k, categories)
    if( guess == row[4]):
        print(f"Predicted: {guess}, actual: {row[4]}: Prediction Correct !")
        correct += 1
    else:
        print(f"Predicted: {guess}, actual: {row[4]}: Prediction Incorrect :(")
print(f"Prediction accuracy: {round(correct/(len(test_rows)-1) * 100,2)}%")

ans = input("Do you want to classify a new vector?(y/n): ")
while ans == 'y':
    a,b,c,d = input("Enter 4 coordinates separated by space: ").split(" ")
    k = int(input("Enter k value: "))
    vec = [a,b,c,d]
    prediction = classify_k_nearest_neighbors(vec,training_rows[1:],k,categories)
    print(f"Predicted category: {prediction}")