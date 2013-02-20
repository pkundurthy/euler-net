import itertools as it

numb = '0123456789'

L = []

for cc in it.permutations(numb,10):
	L.append(cc)
	print cc

L = sorted(L)

print L[999999]
