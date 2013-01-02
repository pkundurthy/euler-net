

# pythagorean triplet
import numpy as num

for a in range(1,1000,1):
	for b in range(a+1,1000,1):
		if b > a:
			c = num.sqrt(a**2 + b**2)
			if c%num.floor(c) == 0:
				#triplet found
				if a + b + c == 1000:
					print a,b,c, a*b*c
