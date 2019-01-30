import numpy as np, json
from helpers import make_row, linear_regression, true_error, get_children, get_controversiality, get_is_root, get_length, get_punctuation, get_links, get_reddit, get_youtube, get_wikipedia, get_imgur, get_slang, do_regression, mid_freq_words
with open("proj1_data.json") as fp:
    data = json.load(fp)

functions = [get_children, get_controversiality, get_is_root]
numwords = 0


do_regression(data, functions, 0, "simple features no words")
do_regression(data, functions, 60, "simple features 60 words")
do_regression(data, functions, 160, "simple features 160 words")
functions.append(get_length)
do_regression(data, functions, 0, "+ 0 words")
do_regression(data, functions, 60, "+ 60 words")
do_regression(data, functions, 160, "+ 160 words")
