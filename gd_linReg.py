import numpy as np
from proj1 import training_X, training_Y

def gradient_descent(X, Y, data_points, features, weights, learning_rate, iterations):
    X_tran = X.transpose() #we transpose outside the loop for time complexity
    for i in range(0, iterations):
        hypothesis = np.dot(X, weights)  # column vector of hypothesis stored as contiguous block of elements

        loss = hypothesis - Y  # column vector loss stored as contiguous elements

        cost = np.sum(loss**2) / (2*data_points)
        epsilon = 1.000
        if(cost <= epsilon):
            break
        print("Iteration: %d | Cost: %f" % (i, cost)) #tracking MSE in every iteration

        gradient = np.dot(X_tran, loss) / data_points
        '''
        print('GRADIENT = ', gradient)
        print('Y SHAPE = ', np.shape(Y))

        print('HYPOTHESIS = ', np.shape(hypothesis))
        print('X SHAPE = ', np.shape(X))
        print('X_tran SHAPE = ', np.shape(X_tran))
        print('LOSS SHAPE = ', np.shape(loss))
        print('GRADIENT SHAPE = ', np.shape(gradient))
        '''
        weights = weights - learning_rate * gradient
    return weights


[N, m] = np.shape(training_X)
data_points = N
features = m

learning_rate = 0.0000281
iterations = 100000
X = training_X
Y = training_Y
Y = Y.reshape((np.shape(training_X)[0],))
weights = np.ones(features)

weights = gradient_descent(X, Y, data_points, features, weights, learning_rate, iterations)
print(weights)


