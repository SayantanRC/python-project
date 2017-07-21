import time
import datetime

def isValidTransactionDate(date):

	nowstring = time.strftime('%Y %m %d')
	nowstring = nowstring.split(' ')
	dtnow = datetime.datetime(int(nowstring[0]), int(nowstring[1]), int(nowstring[2]))

	try:
		datelist = date.split('/')
		dtdate = datetime.datetime(int(datelist[2]), int(datelist[1]), int(datelist[0]))
	except: dtdate = None

	if len(date) == 10 and dtdate != None and dtdate >= dtnow: return True
	else: return False

def isPreviousDate(date):

	nowstring = time.strftime('%Y %m %d')
	nowstring = nowstring.split(' ')
	dtnow = datetime.datetime(int(nowstring[0]), int(nowstring[1]), int(nowstring[2]))

	try:
		datelist = date.split('/')
		dtdate = datetime.datetime(int(datelist[2]), int(datelist[1]), int(datelist[0]))
	except: dtdate = None

	if len(date) == 10 and dtdate != None and dtdate <= dtnow: return True
	else: return False

def compareDates(date1, date2):

	try:
		dt1list = date1.split('/')
		dt2list = date2.split('/')
		dtdate1 = datetime.datetime(int(dt1list[2]), int(dt1list[1]), int(dt1list[0]))
		dtdate2 = datetime.datetime(int(dt2list[2]), int(dt2list[1]), int(dt2list[0]))
	except: return False

	if len(date1) == len(date2) == 10 and dtdate1 <= dtdate2: return True
	else: return False
