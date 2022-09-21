

infile = open('sometext.txt','r')
infileread = infile.read()
wordscount = infileread.split()

dict = {}

count = 0
for words in wordscount:
    if words in dict:
        dict[words]+=1
    else:
        dict[words] = 1

print(dict)