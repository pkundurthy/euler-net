
import itertools as iter
import numpy as num

listNum = []
for it in iter.permutations('0123456789',10):
	x = "".join(list(it))
	if int(it[1]+it[2]+it[3])%2 == 0 and \
	   int(it[2]+it[3]+it[4])%3 == 0 and \
	   int(it[3]+it[4]+it[5])%5 == 0 and \
	   int(it[4]+it[5]+it[6])%7 == 0 and \
	   int(it[5]+it[6]+it[7])%11 == 0 and \
	   int(it[6]+it[7]+it[8])%13 == 0 and \
	   int(it[7]+it[8]+it[9])%17 == 0:
		print x
		listNum.append(int(x))

listNum = num.array(listNum)
print listNum
print num.sum(listNum)

	



