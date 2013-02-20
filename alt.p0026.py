
import numpy as np

def get_multi(factor,num):

	numarr = np.arange(10)
	arr_check = num * numarr
	diff = factor - arr_check
	#print arr_check
	#print diff, factor
	#print diff
	diff[np.where(diff < 0)] = 999
	return numarr[np.argmin(diff)]

def get_factor(number,div):

	nstr = str(number)
	dstr = str(div)
	slc = 0

	grow = nstr[0]
	for i in range(len(nstr)-1):
		#print i, grow, nstr[i]
		if int(grow) < div:
			grow += nstr[i+1]
			slc = i+2
		else:
			break

	return grow, slc

def div1(number,div):

	oStr = ''
	diff = 999
	maxLen = 1000

	while diff != 0 and len(oStr) < maxLen:
		f1, slc = get_factor(number,div)
		f2 = get_multi(int(f1),div)
		diff = int(f1)-f2*div
		oStr += str(f2)
		nStr = str(number)
		number = int(str(diff)+nStr[slc:])
		#print number, f1, f2*div, diff,'|', f2

	return oStr

MaxList = {}
for d in range(1,30,1):
	out = div1(int('1'+2000*'0'),d)
	if len(out) == 1000:
		print d
		MaxList[d] = out

print len(MaxList.keys())

"""
num = 10188
numStr = str(num)
f1,s1 = get_factor(num,12)
f2 = get_multi(int(f1),12)
d = str(f2)
dd = int(f1)-f2*12
print f1, s1, numStr[s1:],  f2*12, f2, int(f1)-f2*12
"""

"""
def ldiv1(denom):

	number = int('1'+200*'0')
	
	string = ''
	while multi > 0:
		factor = get_factor(number,denom) 
		multi = get_multi(float(factor),denom)
		string += multi

	

print ldiv1(12)

"""



"""
for d in np.arange(1,1001,1):
	divs = np.float64(1.0)/np.float64(d)
	p = divs*(10**1)
	pw = 2
	while p%10 != 0 and pw < 200:
		p = int(divs*(10**pw))
		pw += 1
		#print divs, pw, p
	print d, pw, len(str(p)), p
"""		
	



