import numpy as num

file0 = open('file.01.p0011.txt','r').readlines()

array = []
ll = []
for line in file0:
	ll.append(map(int,line.split()))

array = num.array(ll)
shape = num.shape(array)
print array
maxprod = 0
max_str = ''
array.T

def direction(ix,iy,direc):

	x0s = ix,ix,ix,ix
	xplus = ix,ix+1,ix+2,ix+3
	xminus = ix,ix-1,ix-2,ix-3
	y0s = iy,iy,iy,iy
	yplus = iy,iy+1,iy+2,iy+3
	yminus = iy,iy-1,iy-2,iy-3
	
	if direc == 'north':
		x0,x1,x2,x3 = x0s
		y0,y1,y2,y3 = yminus
	if direc == 'south':	
		x0,x1,x2,x3 = x0s
		y0,y1,y2,y3 = yplus

	if direc == 'east':
		x0,x1,x2,x3 = xplus
		y0,y1,y2,y3 = y0s

	if direc == 'west':
		x0,x1,x2,x3 = xminus
		y0,y1,y2,y3 = y0s

	if direc == 'north-east':
		x0,x1,x2,x3 = xplus
		y0,y1,y2,y3 = yminus

	if direc == 'south-east':
		x0,x1,x2,x3 = xplus
		y0,y1,y2,y3 = yplus

	if direc == 'south-west':
		x0,x1,x2,x3 = xminus
		y0,y1,y2,y3 = yplus

	if direc == 'north-west':
		x0,x1,x2,x3 = xminus
		y0,y1,y2,y3 = yminus

	return (x0,x1,x2,x3), (y0,y1,y2,y3)


dlist = ['north','north-east','east','south-east','south','south-west','west','north-west']		
for ix in range(shape[0]):
	for iy in range(shape[1]):
		for direc in dlist:
			(x0,x1,x2,x3), (y0,y1,y2,y3) = direction(ix,iy,direc)

			try:
				t0 = array[x0,y0]
				t1 = array[x1,y1]
				t2 = array[x2,y2]
				t3 = array[x3,y3]
				prod = t0*t1*t2*t3
			except:
				t0,t1,t2,t3 = 0,0,0,0
				prod = 0

			if prod > maxprod:
				maxprod = prod
				max_str = str(ix),str(iy),direc,str(t0),str(t1),str(t2),str(t3)
		
			print (ix,iy), direc, prod, maxprod, max_str

print maxprod
