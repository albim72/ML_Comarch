import numpy as np

class SimpleNeuralNetwork:

    def __init__(self):
        np.random.seed(1)
        self.weights = 2*np.random.random((3,1)) - 1

    #funkcja aktywacji sigmoid
    def sigmoid(self,x):
        return 1/(1+np.exp(-x))

    #różniczka z funkcji aktywacji
    def d_digmoid(self,x):
        return x*(1-x)

    def propagation(self,inputs):
        return self.sigmoid(np.dot(inputs.astype(float),self.weights))

    def backword_propagation(self,propagtion_result,train_input,train_output):
        error = train_output - propagtion_result
        self.weights += np.dot(train_input.T,error*self.d_digmoid(propagtion_result))

    def train(self,train_input,train_output,train_iters):
        for _ in range(train_iters):
            propagation_result = self.propagation(train_input)
            self.backword_propagation(propagation_result,train_input,train_output)
