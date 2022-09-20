import re

outfile = open('sometext.txt','r')

dict = {}

count = 0
for words in outfile:
    word = re.sub("[^A-Za-z0-9 ]+", "", words)
    wordsplt = word.split()

    for text in wordsplt:
        if text in dict:
            dict[text]+=1

        else:
            dict[text] = 1

print(dict)