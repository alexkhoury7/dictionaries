infile = open('bookofJohntext.txt','r')
infileread = infile.read()
wordscount = infileread.split()

words_dict = dict()

for word in wordscount:
    if word in words_dict:
        words_dict[word] = words_dict[word]+1
    else:
        words_dict[word] = 1
    
print('Father:',words_dict['Father'])
print('God:',words_dict['God'])
print('Christ:',words_dict['Christ'])
print('Spirit:',words_dict['Spirit'])
print('spirit:',words_dict['spirit'])
print('life:',words_dict['life'])
print('man:',words_dict['man'])