

dictWordNum = {0:'',1:'one',2:'two',3:'three',4:'four',\
			   5:'five',6:'six',7:'seven',8:'eight',\
			   9:'nine',10:'ten',11:'eleven',12:'twelve',\
			  13:'thirteen',14:'fourteen',15:'fifteen',\
			  16:'sixteen',17:'seventeen',18:'eighteen',\
              19:'nineteen',20:'twenty',30:'thirty',\
			  40:'forty',50:'fifty',60:'sixty',\
			  70:'seventy',80:'eighty',90:'ninety',\
			  100:'hundred',1000:'thousand'}

sumLetters = 0
count = 0
word = ''
for i in range(1,1001,1):
	intStr = str(i)
	if len(str(i)) == 1:
		word = dictWordNum[i]
		count = len(word.strip())
		sumLetters += count
	if len(str(i)) == 2:
		if i < 20:
			word = dictWordNum[i]
			count = len(word.strip())
		else:
			word1 = dictWordNum[int(intStr[0]+'0')]
			word2 = dictWordNum[int(intStr[1])]
			word = word1+word2
			count = len(word.strip())
		sumLetters += count
	if len(str(i)) == 3:
		word1 = dictWordNum[int(intStr[0])] 
		word2 = dictWordNum[100]
		word3 = ''
		word4 = ''
		word5 = ''
		word6 = ''
		newint = int(intStr[-2:])
		newintStr = str(newint)
		if newint < 1:
			pass
		elif newint < 20:
			word3 = 'and'
			word4 = dictWordNum[newint]
		else:
			word3 = 'and'
			word5 = dictWordNum[int(newintStr[0]+'0')]
			word6 = dictWordNum[int(newintStr[1])]
		
		word = word1+word2+word3+word4+word5+word6
		count = len(word.strip())
		sumLetters += count
	if len(str(i)) == 4:
		sumLetters += len('onethousand')
		count = len('onethousand')
		word = 'one thousand'

	print i, word, count



print sumLetters	 
