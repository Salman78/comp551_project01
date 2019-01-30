from text_processing import getRankedList

my_list = getRankedList()

with open('words.txt', 'w') as f:
    for i in range(500):
        f.write("%s\n" % my_list[i])