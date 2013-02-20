
import numpy as np
import itertools as it

def isAbundFunc(Number):
	
	isAbund = False
	Sum = 1
	fac = 2
	while True:
		if fac > float(Number)/2.0:
			break
		else:
			if Number%fac == 0:
				Sum += fac
			fac += 1
		if Sum > Number:
			isAbund = True
			break
	
	return isAbund

i=1
abund = []
sumT = 0
"""
OutFile = open('abund.p0023.txt','w')
while i < 28123:
	#for num in abund:
	#	if i-num in abund and i in abund:
	#		pass
	#	else:
	#		SumT += i
	#isAbund = isAbundFunc(i)
	if isAbundFunc(i):
		abund.append(i)
		print >> OutFile, i
	i += 1
	print i
OutFile.close()
"""


FileD = open('abund.p0023.txt','r').readlines()
abund = []
for line in FileD:
	abund.append(int(line))
abund = np.array(abund)

"""
OutFile2 = open('sums.p0023.txt','w')
for cc in it.combinations_with_replacement(abund,2):
	SumC = cc[0] + cc[1]
	if SumC < 28123:
		print cc
		print >> OutFile2, SumC
OutFile2.close()
import sys
sys.exit()
"""

FileD = open('sums.p0023.txt','r').readlines()
sumNum = []
for line in FileD:
	sumNum.append(int(line))
sumNum = np.array(list(set(sumNum)))

sumT = 0
i = 1
while i < 28123:
	if i not in sumNum:
		sumT += i
		print i, sumT
	i+= 1

print sumT



""" Two interesting solutions
def main():
   # Find the sum of all positive integers that cannot be written as the sum of two abundant numbers
   # NOTE: Only evaluate integers under 20162
   # NOTE: every EVEN integer greater than 46 is the sum of two abundant numbers

   # finds abundantNumbers under 20162
   print "Finding Abundant Numbers"
   abundantNumberList = findAbundantNumbers()
   abundantNumberList.sort()

   # creates an odd abundant numbers list and some small evens to lower number of additions
   print "Truncating List"
   oddList = set()
   for number in abundantNumberList:
      if number%2!=0 or number < 46:
         oddList.add(number)
   oddList = list(oddList)
   oddList.sort()

   # finds the possible sums of abundant numbers
   print "Finding Possible Sums"
   possibleSums = set()
   for number2 in oddList:
      for number in abundantNumberList:
         tempSum = number + number2
         if tempSum > 20162: break
         possibleSums.add(tempSum)

   # finds all positive integers that cannot be written as the sum of two abundant numbers
   notSums = set()
   for i in xrange(1, 20162):
      if not i in possibleSums:
         notSums.add(i)
   notSums = list(notSums)
   notSums.sort()

   # prints sum of all positive integers that cannot be written as the sum of two abundant numbers
   print "Answer:", sum(notSums)


def findAbundantNumbers():
   abundantNumbers = set()
   for i in xrange(12, 20162):
      if sum(findProperDivisors(i)) > i: abundantNumbers.add(i)
   return list(abundantNumbers)


def findProperDivisors(n):
   divisorList = list(set(reduce(list.__add__,
      ([i, n/i] for i in xrange(1, int(n**0.5) + 1) if n % i == 0))))

   #sorts and takes off the last divisor (itself)
   divisorList.sort()
   return divisorList[:-1]

if __name__ == '__main__':
   main()

---------------------------------------------------

def problem23():
    
    def d(n):
    
        m, s = n ** 0.5, 1
        if m == int(m): s -= int(m)
        m = int(m//1) + 1
        for i in xrange(2, m):
            if n%i == 0: s += i + (n/i)
        return s
    
    a, s = set(), 0
    for i in xrange(1, 20612):
        if d(i) > i: a.add(i)
        if not any((i - j) in a for j in a): s += i
    return s

"""

