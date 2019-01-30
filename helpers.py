import numpy as np, math
def linear_regression(X, Y):
    XT = np.transpose(np.copy(X))
    return np.matmul(np.linalg.inv(np.matmul(XT,X)), np.matmul(XT,Y))


def make_row(comment, row, X, Y, functions, numwords, words):
    new_row = [1]
    for fun in functions :
        new_row.append(fun(comment))
    new_row += count_words(numwords, comment, words)
    X[row] = new_row
    Y[row] = get_popularity(comment)

def count_words(numwords, comment, words):
    if (numwords > 0):
        to_ret = []
        for i in range(numwords):
            str_l = words[i]
            if str_l[-1] == '\n':
                to_ret.append(comment["text"].count(str_l[:-1]))
            else :
                to_ret.append(to_ret.append(comment["text"].count(str_l)))
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

def test(comment):
    return 1 if comment["text"] == "[deleted]" else 0
    # numwords = len(comment["text"].split())
    # return 1 if numwords >= 10 else 0
    # return 1 if len(comment["text"]) > 21 else 0

def is_question(comment):
    return comment["text"].count("?")

def num_curses(comment):
    text = comment["text"].lower()
    return 1 if (text.count(" r/")+text.count(" /r/") > 0) else 0

def get_numbers(comment):
    text = comment["text"]
    count = text.count("1")+text.count("2")+text.count("3")+text.count("4")+text.count("5")+text.count("6")+text.count("7")+text.count("8")+text.count("9")+text.count("0")
    return 1 if count > 0 else 0

def get_punctuation(comment):
    periods = comment["text"].count('.')
    commas = comment["text"].count(',')
    colons = comment["text"].count(':')
    semicolons = comment["text"].count(';')
    excls = comment["text"].count('!')
    quests = comment["text"].count('?')
    return 1 if periods+commas+colons+semicolons+excls+quests > 3 else 0

def get_links(comment):
    words = comment["text"].split()
    cap = [word for word in words if word.isupper() and word != "I"]
    return len(cap)

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

def mse(X, W, Y):
    F = np.matmul(X, W)
    error_vector = (Y-F)
    squared_error = np.matmul(np.transpose(error_vector), error_vector)
    return (squared_error)/np.size(Y)

def do_regression(data, functions, numwords, expl):
    num_of_features = len(functions) + numwords + 1
    file = open("Unfiltered.txt", "r")
    words = []
    for i in range(numwords):
        words.append(file.readline())
    file.close()
    # Create matrix X
    training_X = np.empty([10000, num_of_features])
    # Create matrix Y
    training_Y = np.empty([10000, 1])

    for i in range(0, 10000):
        make_row(data[i], i, training_X, training_Y, functions, numwords, words)

    W = linear_regression(training_X, training_Y)

    validation_X = np.empty([1000, num_of_features])
    validation_Y = np.empty([1000, 1])

    for i in range(10000, 11000):
        make_row(data[i], i - 10000, validation_X, validation_Y, functions, numwords, words)

    print("For %s\n" % expl)
    training_error = mse(training_X, W, training_Y)
    print("Error on training data : %f\n" % training_error)
    validation_error = mse(validation_X, W, validation_Y)
    print("Error on validation data : %f\n" % validation_error)

    return (training_error, validation_error)