class Perceptron:
    def __init__(self, input_array, weights_array, rate, classes):
        self.input_array = input_array
        self.weights_array = weights_array
        self.classes = classes
        self.rate = rate

    def learn(self):
        for i in self.input_array:
            val = 0
            for var, weight in zip(i, self.weights_array):
                val += var * weight
            val += self.bias * -1
            prediction = True if val > 0 else False
            correct = bool(i[-1])
            if prediction != correct:
                self.delta(correct,prediction,self.rate,i[:-1])


    def delta(self, correct, actual,rate, input):
        multi = (correct - actual) * rate
        input = [i * multi for i in input]
        self.weights_array = [w + i for w,i in zip(self.weights_array, input)]