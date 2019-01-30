import numpy as np, json
from helpers import make_row, linear_regression, mse, get_children, get_controversiality, get_is_root, get_length, get_punctuation, get_links, get_reddit, get_youtube, get_wikipedia, get_imgur, get_slang, do_regression, mid_freq_words
from helpers import get_numbers, is_question, num_curses, test
with open("proj1_data.json") as fp:
    data = json.load(fp)

functions = [get_children, get_controversiality, get_is_root]
numwords = 0


res_1 =do_regression(data, functions, 0, "simple features no words")
res_2 = do_regression(data, functions, 60, "simple features 60 words")
res_3 =do_regression(data, functions, 160, "simple features 160 words")
functions.append(test)
res_4 = do_regression(data, functions, 0, "+ 0 words")
res_5 = do_regression(data, functions, 60, "+ 60 words")
res_6 = do_regression(data, functions, 160, "+ 160 words")

print(res_4[1] - res_1[1])
print(res_5[1] - res_2[1])
print(res_6[1] - res_3[1])
