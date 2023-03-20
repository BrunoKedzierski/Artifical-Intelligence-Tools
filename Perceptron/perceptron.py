import random


class Perceptron:
    def __init__(self, learning_data, learning_rate,n_epochs):
        self.learning_data = learning_data
        self.learning_rate = learning_rate
        self.weights = [random.uniform(0.0, 1.0) for _ in range(len(learning_data[1]) -1 )]
        self.bias = 0
        self.n_epochs = n_epochs
        print(self.weights)

    def predict(self,row):
        activation = self.bias
        for i in range(len(row)):
            activation += self.weights[i] * row[i]
        return 1.0 if activation >= 0 else 0.0

    def learn(self):
        random.shuffle(self.learning_data)
        for _ in range(self.n_epochs):
            for vector in self.learning_data:
                error_term = vector[-1] - self.predict(vector[0:-1])
                self.bias = self.bias + self.learning_rate * error_term
                for i in range(len(self.weights)):
                    self.weights[i] = self.weights[i] + self.learning_rate * error_term * vector[i]

    def test(self, test_data):
        success_no = 0
        for vector in test_data:
            prediction = self.predict(vector[:-1])
            print(f"Predicted: {prediction} , actual: {vector[-1]}")
            if prediction == vector[-1]:
                success_no += 1
        print(f"Number of sucesses: {success_no}")