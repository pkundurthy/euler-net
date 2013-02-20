

def checkLeap(year):
	isLeap = False

	if year%4 == 0:
		isLeap = True

	if year%100 == 0:
		if year%400 == 0:
			isLeap = True
		else:
			isLeap = False

	return isLeap

def turnWeek(day):
	
	if day < 7:
		day += 1
	else:
		day = 1
	
	return day	

def advanceDate(Dict):

	MonthDays = {1:31,2:28,3:31,4:30,\
				 5:31,6:30,7:31,8:31,\
				 9:30,10:31,11:30,12:31}

	date = Dict['date']
	month = Dict['month']
	year = Dict['y']
	leap = checkLeap(year)

	if date == 28 and month == 2 and not leap:
		Dict['date'] = 1
		Dict['month'] += 1
		Dict['day'] = turnWeek(Dict['day'])
	elif date == 29 and month == 2 and leap:
		Dict['date'] = 1
		Dict['month'] += 1
		Dict['day'] = turnWeek(Dict['day'])
	elif date == 31 and month == 12:
		Dict['date'] = 1
		Dict['month'] = 1
		Dict['y'] += 1
		Dict['day'] = turnWeek(Dict['day'])
	elif date == 31 and month in [1,3,5,7,8,10]:
		Dict['date'] = 1
		Dict['month'] += 1
		Dict['day'] = turnWeek(Dict['day'])
	elif date == 30 and month in [4,6,9,11]:
		Dict['date'] = 1
		Dict['month'] += 1
		Dict['day'] = turnWeek(Dict['day'])
	else:
		Dict['date'] += 1
		Dict['day'] = turnWeek(Dict['day'])

	return Dict
				
DayWeek = \
 	{1:'Mon',2:'Tue',3:'Wed',\
	 4:'Thu',5:'Fri',6:'Sat',7:'Sun'}

NowDict = {'y':1900,'date':1,'month':1,'day':1}
FirstSunCount = 0
dc = 1
while NowDict['y'] < 2001:
	#print NowDict, dc
	if NowDict['y'] > 1900 and \
	   NowDict['date'] == 1 and NowDict['day'] == 7:
		FirstSunCount += 1
		#print NowDict
	NowDict = advanceDate(NowDict)
	dc += 1
	
print FirstSunCount, dc


	


