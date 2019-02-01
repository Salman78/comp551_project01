import json  # we need to use the JSON package to load the data, since the data is stored in JSON format

# import nltk

def containsPunctuation(var):
    if not var.find('!')==-1 or not var.find('?')==-1 or not var.find('.')==-1 or not var.find(',')==-1 \
            or not var.find(':') == -1 or not var.find(';')==-1 or not var.find('(')==-1 or not var.find(')')==-1 \
            or not var.find('[') == -1 or not var.find(']')==-1 or not var.find('*')==-1 \
            or not var.find('{') == -1 or not var.find('}')==-1 or not var.find('"')==-1:
        return True
    else:
        return False

def removePunctuation(word):
    word = word.replace("!", "")
    word = word.replace("?", "")
    word = word.replace(";", "")
    word = word.replace(":", "")
    word = word.replace(",", "")
    word = word.replace(".", "")
    word = word.replace("(", "")
    word = word.replace(")", "")
    word = word.replace("*", "")
    word = word.replace("]", "")
    word = word.replace("[", "")
    word = word.replace("}", "")
    word = word.replace("{", "")
    word = word.replace('"', "")
    return word

def getRankedList():
    with open("proj1_data.json") as fp:
        data = json.load(fp)

    masterDictionary={}
    for x in range(0,11999):
        aList = data[x]['text'].casefold().split() #split the text of a comment by its spaces

        for word in aList: #Look for words with punctuation and split that
            index = aList.index(word)
            '''
            if containsPunctuation(word): #does the word contain punctuation?
                baseWord = removePunctuation(word) #if so, it needs to be removed
                #index = aList.index(word)
                aList[index]=baseWord
            '''
            #the entries in this cleaned up list of words need to be counted for the master dictionary
            #value = masterDictionary.get(aList[index])
            if masterDictionary.get(aList[index])==None:#If the word isn't present in the master dictionary
                masterDictionary.update({aList[index]:1}) #The master needs to be updated with a new entry
            else: #otherwise, the word is already present, and its value needs to be appended
                masterDictionary.update({aList[index]:masterDictionary.get(aList[index])+1})
    #now that all the words have been counted and placed in the master dictionary, the most popular ones must be determined

    sortedDictionary={}
    s = [(k, masterDictionary[k]) for k in sorted(masterDictionary, key=masterDictionary.get, reverse=True)]
    for k, v in s:
        sortedDictionary.update({k:v})
    #sortedDictionary.pop('')
    sortedList = list(sortedDictionary)
    print(sortedDictionary)
    #print(sortedList)#Print the list words, sorted from most commonly used to least commonly used
    return sortedList

'''
def count_adjectives(comment):
    counter=0;
    try:
        text = nltk.word_tokenize(comment) #tokenizes the words in the comment
    except:
        return 0
    result = nltk.pos_tag(text) #produces a list of tuples that identifies properties of each word
    for x in range(0,len(result)):
        if not result[x][1].find("JJ")==-1:#if any adjective is found
            counter = counter+1 #augment counter
    return counter
'''
with open("proj1_data.json") as fp:
    data = json.load(fp)

print(data[0])
'''
for x in range(0,20):
    print(count_adjectives(data[x].get('text').lower()))
'''
'''
#fo = open("ranked_comments.txt", "w")
#print(data[0])
pop_dic = {}
for x in range(0, 11999):
    pop_dic.update({data[x].get('text'):data[x].get('popularity_score')})

sortedDictionary={}
s = [(k, pop_dic[k]) for k in sorted(pop_dic, key=pop_dic.get, reverse=True)]
for k, v in s:
    sortedDictionary.update({k:v})
aList = list(sortedDictionary)
for y in range(0,20):
    print("%s\n", aList[y])

''
text = 'This is a table. We should table this offer. The table is in the center.'
text = nltk.word_tokenize(text)
result = nltk.pos_tag(text)
result = [i for i in result if i[0].lower() == 'table']

print(result[0][1]) # [('table', 'NN'), ('table', 'VB'), ('table', 'NN')]
''
''
aList = getRankedList()
fo = open("500Words_Unfiltered.txt", "w")
count = 0;
limit = 500
for i in range(0, limit):
    try:
        fo.write("%s\n" %aList[i])
    except:
        count=count+1
        limit=limit+1
        print("Found weird character: %d\n", count)
fo.close()
''
''
#The following commented block will produce a list of links. Most of the links are dead ends.
with open("proj1_data.json") as fp:
    data = json.load(fp)

for x in range(0, 11999):
    aList = data[x]['text'].casefold().split()  # split the text of a comment by its spaces
    for word in aList:  # Look for words with punctuation and split that
        index = aList.index(word)
        if not word.find("http")== -1:  # does the word contain a link?
            print(word)
'''