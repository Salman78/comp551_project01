import numpy as np, json, helpers, matplotlib.pyplot as plt, gd_linReg
with open("proj1_data.json") as fp:
    data = json.load(fp)

file = open("words.txt", "r")
words = []
for i in range(160):
    words.append(file.readline())
file.close()

gd_linReg.gradient_descent_algorithm(10000, data, 4 , 0.003, 50000, words)
gd_linReg.gradient_descent_algorithm(10000,data, 64,  0.003, 50000, words)
gd_linReg. gradient_descent_algorithm(10000, data, 164,  0.003, 50000, words)
functions = [helpers.get_children, helpers.get_controversiality, helpers.get_is_root]
res_0_words = helpers.do_regression(data, functions, 0, "only the base features, no words", words)
res_60_words = helpers.do_regression(data, functions, 60, "only the base features, 60 words", words)
res_160_words = helpers.do_regression(data, functions, 160, "only the base features, 160 words", words)

res_60_words_log = helpers.do_regression(data, functions+[helpers.log_children], 60, "base features+ the log of the children , 60 words", words)
res_60_words_square = helpers.do_regression(data, functions+[helpers.square_children], 60, "base features+ the square of the children , 60 words", words)
res_60_words_length = helpers.do_regression(data, functions+[helpers.check_length], 60, "base features+ check on text lenght, 60 words", words)




# Creating the final model
# Create matrix X
training_X = np.empty([10000, 67])
# Create matrix Y
training_Y = np.empty([10000, 1])
functions = [helpers.get_children, helpers.get_controversiality, helpers.get_is_root, helpers.log_children, helpers.square_children, helpers.check_length]

for i in range(10000):
    helpers.make_row(data[i], i, training_X, training_Y, functions, 60, words)
W = helpers.linear_regression(training_X, training_Y)

validation_X = np.empty([1000, 67])
validation_Y = np.empty([1000, 1])
for i in range(1000):
    helpers.make_row(data[10000+i], i, validation_X, validation_Y, functions, 60, words)
test_X = np.empty([1000, 67])
test_Y = np.empty([1000, 1])
for i in range(1000):
    helpers.make_row(data[11000+i], i, test_X, test_Y, functions, 60, words)
print("Model error on the training set : %f"% helpers.mse(training_X, W, training_Y))
print("Model error on the validation set : %f"% helpers.mse(validation_X, W, validation_Y))
print("Model error on the test set : %f"% helpers.mse(test_X, W, test_Y))


