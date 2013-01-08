
import numpy as np


fileObj = open('file.01.p0018.txt','r').readlines()

DictTree = {}
NLev = len(fileObj)

for iL in range(NLev):
	line = fileObj[iL]
	maplist = map(int, line.split())
	Nmap = len(maplist)
	DictTree[iL] = {}
	for iR in range(Nmap):
		TR = iL-1,iR
		TL = iL-1,iR-1
		BR = iL+1,iR+1
		BL = iL+1,iR
		if iL == 0:
			TR = None,None
			TL = None,None
		if iL == NLev-1:
			BR = None,None
			BL = None,None
		if iR == 0:
			TL = None,None
		if iR == Nmap-1:
			TR = None,None
 
		DictTree[iL][iR] = {'v':maplist[iR],\
						    'tr':TR,'tl':TL,\
							'br':BR,'bl':BL,\
							'visited':False}

iL = 0
iR = 0
maxSum = 0
sumN = 0
typeDef = 'bl'
while True:
	sumN += DictTree[iL][iR]['v']
	DictTree[iL][iR]['visited'] = True
	iL,iR = DictTree[iL][iR][typeDef] 
	if iL == None and iR == None:
		if sumN > maxSum:
			maxSum = sumN
		sumN -= DictTree[iL][iR]['v']
		iL,iR = DictTree


print sumN



	


