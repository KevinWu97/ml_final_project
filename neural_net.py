import numpy as np
import random
import decision_tree
import pandas as pd

class Network:
    # dont use political id, it's the y value
    #sizes will most likely be [77, 24, 7, 1], number of neurons at each layer
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        #[[24x1 list of numbers],[7x1 list of random numbers], [1x1 list of random numbers]]
        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        #zip ([77,24,7] and [24,7,1]) -> [(77,24), (24,7), (7,1)]
        #then it will produce a 24x77 list of numbers, a 7x24 list of numbers, and a 1x7 list of numbers
        #example: weights[1][5][2] will be the weight for the 6th neuron in the 2nd layer of neurons to the 3rd neuron in the 3rd layer
        self.weights = [np.random.randn(y, x)
                        for x, y in zip(sizes[:-1], sizes[1:])]

    def sigmoid(self, z):
        # np.exp calculates e^-z for each value in the list passed in
        return 1.0 / (1.0 + np.exp(-z))

    # derivative of sigmoid function
    def sigmoid_prime(self, z):
        return self.sigmoid(z) * (1 - self.sigmoid(z))

    #input passed in should be of size 78x1
    def getoutput(self, input):
        output = 0
        for b, w in zip(self.biases, self.weights):
            output = self.sigmoid(np.dot(w, input) + b)
        return output

    # training_data is an array of tuples (x, y) <- note, need to prune the x variables from the candidates first (x is a vector, y is a value)
    # epochs = how many rounds do we train for, good number is 1000
    # mini_batch_size = we pick out only a certain amount of data from the set to train on
    def gradient_descent(self, training_data, epochs, dtree_var, learning_rate,
            test_data=None):
        if test_data:
            n_test = len(test_data)
        n = len(training_data)
        for j in range(0, epochs):
            # replacing the shuffling and mini batches with using the decision tree to get the mini batches
            '''
            random.shuffle(training_data)
            batches = [
                training_data[k:k + batch_size]
                for k in range(0, n, batch_size)
            ]
            '''
            # use decision tree to split the data
            batches = []

            decision_tree.traverse_and_split(dtree_var, training_data, batches)

            # filter batches to get only columns with the relevant neural network variables (77)
            # before calling the update step method
            for batch in batches:
                batch = batch[['age','gender','anchoranswer1','anchoranswer2','anchoranswer3','anchoranswer4','reciprocityus','reciprocityother','allowedforbidden','quote','totalflagtimeestimations','totalnoflagtimeestimations','iatexpert',
                              'iatexpmath','iatexpall','totalexpmissed','artwarm','diseaseframinga','diseaseframingb','flagdv1','flagdv2','flagdv3','flagdv4','flagdv5','flagdv6','flagdv7',
                              'flagdv8','flagsupplement1','flagsupplement2','flagsupplement3','flagtimeestimate1','flagtimeestimate2','flagtimeestimate3','flagtimeestimate4', 'gamblerfallacya',
                              'gamblerfallacyb','iatexplicitart1','iatexplicitart2','iatexplicitart3','iatexplicitart4','iatexplicitart5','iatexplicitart6','iatexplicitmath1','iatexplicitmath2',
                              'iatexplicitmath3','iatexplicitmath4','iatexplicitmath5','iatexplicitmath6','imaginedexplicit1','imaginedexplicit2','imaginedexplicit3','imaginedexplicit4','major','mathwarm','moneyagea',
                              'moneyageb','moneygendera','moneygenderb','noflagtimeestimate1','noflagtimeestimate2','noflagtimeestimate3','noflagtimeestimate4','omdimc3','quotea','quoteb',
                              'scalesa','scalesb','sunkcosta','sunkcostb','sysjust1','sysjust2','sysjust3','sysjust4','sysjust5','sysjust6','sysjust7','sysjust8']].copy()
                batch = batch.values.tolist()
                self.update_mini_batch(batch, learning_rate)
            '''
            if test_data:
                # print "Epoch {0}: {1} / {2}".format(j, self.evaluate(test_data), n_test)
            else:
                # print "Epoch {0} complete".format(j)
            '''

    def update_mini_batch(self, batch, learning_rate):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        for x, y in batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x.transpose(), y)
            nabla_b = [nb + dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw + dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        self.weights = [w - (learning_rate / len(batch)) * nw
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = [b - (learning_rate / len(batch)) * nb
                       for b, nb in zip(self.biases, nabla_b)]

    # make sure to transpose the x vector
    def backprop(self, x, y):
        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        # feedforward
        activation = x
        activations = [x]  # list to store all the activations, layer by layer
        outputs = []  # list to store all the calculated outputs, layer by layer
        for b, w in zip(self.biases, self.weights):
            # how this is works is that each row in w represents the neuron in the next layer
            # so that row of weights corresponds with the neuron in that next layer
            # for some reason np.dot also transposes, so when you add b, you're adding
            # a bias for each neuron?
            o = np.dot(w, activation) + b.transpose()
            o = o.transpose()
            outputs.append(o)
            activation = self.sigmoid(o)
            activations.append(activation)
        # backward pass
        delta = self.cost_derivative(activations[-1], y) * self.sigmoid_prime(outputs[-1])
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())

        for l in range(2, self.num_layers):
            o = outputs[-l]
            sp = self.sigmoid_prime(o)
            delta = np.dot(self.weights[-l + 1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l - 1].transpose())
        return nabla_b, nabla_w

    '''
    def evaluate(self, test_data):
        test_results = [(np.argmax(self.feedforward(x)), y)
                        for (x, y) in test_data]
        return sum(int(x == y) for (x, y) in test_results)
    '''

    def cost_derivative(self, output_activations, y):
        return output_activations - y
