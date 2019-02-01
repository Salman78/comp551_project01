import numpy as np
import timeit
import helpers

def gradient_descent(training_X, training_Y, learning_rate, iterations):
    [N, m] = np.shape(training_X)
    data_points = N
    features = m

    X = training_X
    Y = training_Y
    Y = Y.reshape((np.shape(training_X)[0],))
    weights = np.ones(features)

    weights = gradient_descent(X, Y, data_points, features,  learning_rate, iterations)
    return weights

def gradient_descent_algorithm(data_points,data,  features, learning_rate, iterations, words):
    X =  np.empty([10000, features])
    Y = np.empty([10000, 1])

    functions = [helpers.get_children, helpers.get_controversiality, helpers.get_is_root]
    for i in range(10000):
        helpers.make_row(data[i], i, X, Y, functions, features-4, words)

    X_tran = X.transpose() #we transpose outside the loop for time complexity
    weights = np.ones([features, 1])
    start = timeit.default_timer()
    for i in range(0, iterations):
        hypothesis = np.dot(X, weights)

        loss = hypothesis - Y

        cost = np.sum(loss**2) / (data_points)
        epsilon = 1.005
        upper_bound = 100000000000
        if(cost <= epsilon or cost >= upper_bound):
            break
        # print("Iteration: %d | Cost: %f" % (i, cost)) #tracking MSE in every iteration

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
    stop = timeit.default_timer()
    print("Gradient descent with {0} words found MSE : {1} in {2} seconds".format((features-4), cost, (stop-start)))
    return weights



