import random


class Perceptron:
    def __init__(self, input_array, rate, class_zero, class_one):
        self.input_array = input_array
        self.class_zero = class_zero
        self.class_one = class_one
        self.rate = rate
        self.weights_array = []


    def initialize_weights_biases(self):
        for i in range(len(self.input_array)):
            i.insert(-1,-1)
            self.weights_array.append(random.sample(range(-1,2),len(i) -1))


    def learn(self):
        random.shuffle(self.input_array)
        for i in self.input_array:
            prediction = predict(i)
            correct = bool(i[-1])
            if prediction != correct:
                self.delta(correct,prediction,self.rate,i[:-1])


    def delta(self, correct, actual,rate, input):
        multi = (correct - actual) * rate
        input = [i * multi for i in input]
        self.weights_array = [w + i for w,i in zip(self.weights_array, input)]

    def predict(self, input):
        val = 0
        for var, weight in zip(input, self.weights_array):
            val += var * weight
        prediction = True if val > 0 else False
        return prediction

    def test(self, input_array):
        correct =  0
        for i in input_array:
            prediction = predict(i)
            class_name = self.class_one if predict(i) else self.class_zero
            print(f"Predicted: {class_name}")
            correct = bool(i[-1])
            if prediction == bool(correct):
                correct+=1
                print("Correct!")
            else:
                print("Incorrect!")
        print(f"Sucess rate: {float(correct/len(input_array))}" )