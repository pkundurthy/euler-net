
def ndigit(number):

	return len(str(number))



F = [1,1]
ndig = ndigit(F[-1])
term = 2
while ndig < 1000:
	N = F[0] + F[1]
	F[0] = F[1]
	F[1] = N
	ndig = ndigit(F[-1])
	term += 1
	print N, ' | ', term



	

