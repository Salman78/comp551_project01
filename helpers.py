import numpy as np
def linear_regression(X, Y):
    XT = np.transpose(np.copy(X))
    return np.matmul(np.linalg.inv(np.matmul(XT,X)), np.matmul(XT,Y))


def make_row(comment, row, X, Y, functions, numwords):
    new_row = [1]
    for fun in functions :
        new_row.append(fun(comment))
    new_row += count_words(numwords, comment)
    X[row] = new_row
    Y[row] = get_popularity(comment)

def count_words(numwords, comment):
    if (numwords > 0):
        to_ret = []
        file = open("RankedList.txt", "r")
        for i in range(numwords):
            str_l = file.readline().split()
            if len(str_l) > 0:
                to_ret.append(comment["text"].lower().count(str_l[0]))
            else :
                to_ret.append(0)
        file.close()
        return to_ret
    else :
        return []


def mid_freq_words(comment):
    text =comment["text"].lower()
    count = 0
    with open("MiddleFrequency.txt", "r") as f:
        for line in f:
            l = line.split()
            if len(l) > 0:
                count += text.count(l[0])

    return count

def get_popularity(comment):
    return comment["popularity_score"]

def get_children(comment):
    return comment["children"]

def get_controversiality(comment):
    return comment["controversiality"]

def get_is_root(comment):
    return 1 if comment["is_root"] else 0

def get_length(comment):
    return 1/len(comment["text"])


def get_punctuation(comment):
    periods = comment["text"].count('.')
    commas = comment["text"].count(',')
    return periods+commas

def get_links(comment):
    return comment["text"].count("http")

def get_youtube(comment):
    return comment["text"].count("youtube.com")+comment["text"].count("youtu.be")

def get_reddit(comment):
    return comment["text"].count("reddit.com") + comment["text"].count("redd.it")


def get_imgur(comment):
    return comment["text"].count("imgur.com")

def get_wikipedia(comment):
    return comment["text"].count("wikipedia.org")

def get_slang(comment):
    str = comment["text"].lower()
    return str.count("vs")

def true_error(X, W, Y):
    F = np.matmul(X, W)
    error_vector = np.square(F-Y)
    return np.sum(error_vector)/np.size(Y)

def do_regression(data, functions, numwords, expl):
    num_of_features = len(functions) + numwords + 1
    # Create matrix X
    training_X = np.empty([10000, num_of_features])
    # Create matrix Y
    training_Y = np.empty([10000, 1])

    for i in range(0, 10000):
        make_row(data[i], i, training_X, training_Y, functions, numwords)

    W = linear_regression(training_X, training_Y)

    validation_X = np.empty([1000, num_of_features])
    validation_Y = np.empty([1000, 1])

    for i in range(10000, 11000):
        make_row(data[i], i - 10000, validation_X, validation_Y, functions, numwords)

    print("For %s\n" % expl)
    training_error = true_error(training_X, W, training_Y)
    print("Error on training data : %f\n" % training_error)
    validation_error = true_error(validation_X, W, validation_Y)
    print("Error on validation data : %f\n" % validation_error)

    return (training_error, validation_error)