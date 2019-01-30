import json  # we need to use the JSON package to load the data, since the data is stored in JSON format

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
            if containsPunctuation(word): #does the word contain punctuation?
                baseWord = removePunctuation(word) #if so, it needs to be removed
                index = aList.index(word)
                aList[index]=baseWord
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

    sortedList = list(sortedDictionary)
    #print(sortedList)#Print the list words, sorted from most commonly used to least commonly used
    return sortedList
