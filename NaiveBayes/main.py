from random import shuffle
import csv



def decision_attributes(observations):
    list_of_classes = [x[-1] for x in observations]
    return set(list_of_classes)


def count_prior(observations):
    list_of_classes = [x[-1] for x in observations]
    set_of_classes = set(list_of_classes)
    occ_count = dict()
    for c in set_of_classes:
        occ_count[c] = list_of_classes.count(c)
    return  occ_count

def posterior_for_decision(att,decision, observations):
    cnt = 0;
    denom = count_prior(observations)[decision]
    for vector in observations:
        if(vector[:-1]) == decision)

def sep_by_class(observations):
    classes = dict()
    for obs in observations:
        cls = obs[-1]
        if cls not in classes:
            classes[cls] = list()
        classes[cls].append(obs[0:-1])
    return classes
def get_attributes(observations):
    attributes = set()
    for ob in observations:
        attributes.update(ob[0:-1])
    return attributes

def calculate_conditionals(attributes,separated_observations,priors):
    outcomes = set(separated_observations.keys())
    conditionals = dict()
    for out in outcomes:
        conditionals[out] = list()
        flat_list = [item for sublist in separated_observations[out] for item in sublist]
        for att in attributes:
            conditionals[out].append((att,flat_list.count(att)/priors[out]))
    print(conditionals)

def extract_attributes(observations):
    attributes = dict()
    colnames = observations[0]
    for colname in colnames:
        attributes[colname] = set()

    for ob in observations[1:]:
        for i in range(len(ob)):
            attributes[colnames[i]].add(ob[i])
    return  attributes




training_set_path = "bayes_trainingset.csv"
test_set_path = "bayes_testset.csv"

with open(training_set_path, 'r') as file:
    csv_training_file_content = csv.reader(file)
    training_rows = list(csv_training_file_content)


with open(test_set_path, 'r') as file:
    csv_test_file_content = csv.reader(file)
    test_rows = list(csv_test_file_content)

print(training_rows[1:])
print(count_prior(training_rows[1:]))