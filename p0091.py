
import numpy as num
import itertools as iter

pi = num.pi
class vect:
	
	def __init__(self,x1,y1,x2,y2):
		self.x = x2-x1
		self.y = y2-y1
		self.mag = num.sqrt(self.x**2 + self.y**2)

def checkAngle(x1,y1,x2,y2):
	
	angle = False
	vec01 = vect(0,0,x1,y1)
	vec10 = vect(x1,y1,0,0)
	vec02 = vect(0,0,x2,y2)
	vec20 = vect(x2,y2,0,0)
	vec12 = vect(x1,y1,x2,y2)
	vec21 = vect(x2,y2,x1,y1)

	if vec01.mag != 0 or vec02.mag !=0 or\
	   vec10.mag != 0 or vec12.mag !=0 or\
	   vec20.mag != 0 or vec21.mag != 0:
		dot_a = (vec01.x*vec02.x + vec01.y*vec02.y)/\
				(vec01.mag*vec02.mag)
		dot_b = (vec10.x*vec12.x + vec10.y*vec12.y)/\
				(vec10.mag*vec12.mag)
		dot_c = (vec20.x*vec21.x + vec20.y*vec21.y)/\
				(vec20.mag*vec21.mag)
		a = num.arccos(dot_a)
		b = num.arccos(dot_b) 
		c = num.arccos(dot_c)
		if (a+b+c)*180/pi == 180e0:
			if a*180/pi == 90 or\
			   b*180/pi == 90 or\
			   c*180/pi == 90:
				angle = True
				print x1,y1,x2,y2, a*180/pi,b*180/pi,c*180/pi

	return angle


vert0 = (0,0)
boxrange = (0,50)
count = 0
point_list = xrange(boxrange[0],boxrange[1]+1,1)

for it1 in iter.product(point_list,point_list):
	x1 = it1[0]
	y1 = it1[1]
	for it2 in iter.product(point_list,point_list):
		x2 = it2[0]
		y2 = it2[1]
		if x1 == 0 and y1 == 0:
			pass
		elif x1 == x2 and y1 == y2:
			pass
		elif x2 == 0 and y2 == 0:
			pass
		else:
			l01 = (x1-0)**2 + (y1-0)**2
			l02 = (x2-0)**2 + (y2-0)**2
			l12 = (x2-x1)**2 + (y2-y1)**2
			if (l01 + l02) == l12 or \
		       (l02 + l12) == l01 or \
		       (l12 + l01) == l02:
				print (0,0), (x1,y1), (x2,y2)
				count += 1

print count/2
				




