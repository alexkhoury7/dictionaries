infile = open('info_security.txt','r')
infiles = infile.read()
words = infiles.strip()

outfile = open('encrypted.txt','w')

codes = {'A':'2', 'a':'$', 'B':'@', 'b':'0', 'C':'*', 'c':'&', 'D':'5', 'd':'#', 'E':'!', 'e':'7', 'F':'<', 'f':'/', 'G':'?',
'g':'[', 'H':'+', 'h':')', 'I':'{', 'i':'(', 'J':'%', 'j': '~', 'K':'a','k':'^', 'L':'8', 'M':'.', 'm':',', 'N':'6', 'n':'3', 
'O':'s', 'o':'&', 'P':'|', 'p':']', 'Q':'%#', 'q':'^^', 'R':'g', 'r':'!!', 'S':'`', 's':'~~', 'T':'=', 't':'))', 'U':'nn', 
'u':'44', 'V':'||', 'v':'xx', 'W':'12', 'w':'h', 'X':'90', 'x':'--', 'Y':'++', 'y':'[[', 'Z':'76', 'z':'gg'}

encrypt = ''
for alph in words:
    if alph in codes:
        encrypt += codes[alph]
    else:
        encrypt +=  alph

print(encrypt)
outfile.write(encrypt)
outfile.close()