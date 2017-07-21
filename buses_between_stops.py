import os
import sys
import manageDB as mdb
import ipop

def main():

	ipop.cls()

	username = ''

	try:
		username = sys.argv[1]
		if mdb.checkUsernamePresence(username) == False: username = ''
	except: pass

	screen = "_________________________________________________________________\n" + "|\t\t\t\t\t\t\t\t|\n" + "|\tEnter source and destination to get avilable buses\t|\n" + "|\tExample: Howrah to Asansol etc...\t\t\t|\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

	print (screen)

	bbslist = []

	if username != '':
		try:
			storedbbs = mdb.get_user_activity(username, 'buses_between_stops')
			if storedbbs != '':
				storedbbs = storedbbs.split('\n')
				bbslist = list(enumerate(storedbbs, start=1))
				print ("||\tYour previous searches:\n")
				h = ['Choice', 'Buses between stops']
				tup = (h, bbslist)
				ipop.print_table(tup)
				print ("||\tYou can enter these choices in starting field.\n")
		except: pass


	while True:
		r = disp_bbs(username, bbslist)
		if r == 0:
			exit1(username)
			break
		else:
			ch = ipop.getUserData([int, str], "||\tEnter 1 for another search or !q for main menu.\n\t", "Wrong data.")
			if ch == 1: continue
			else:
				exit1(username)
				break


def exit1(un):
	if un == '':
		os.system("python3 main_menu.py")
	else:
		os.system("python3 logged_in_main_menu.py '" + un + "'")

def disp_bbs(un, bbslist):

	buses = []
	source = ''
	destination = ''
	chflag = 0

	source = ipop.getUserData([str, int], "||\tEnter source or previous search option (if available)\n||\tor !q to cancel: ", "Wrong data")

	if source == None:
		return 0
	for (i, d) in bbslist:
		if source == i:
			source = d.split('_')[0]
			destination = d.split('_')[1]
			chflag = 1
			break

	if chflag == 0:
		destination = ipop.getUserData([str, int], "||\tEnter destination of journey or !q to cancel: ", "Wrong data")
		if destination == None:
			return 0

	buses = mdb.buses_between_stops(source, destination, un)
	if buses == []:
		print ("This route does not exist.")
		return 1
	else:
		l = []
		print('\nFollowing buses are available:')
		print('From ' + source + ' to ' + destination)
		for b in buses:
			l.append((b, mdb.getBusType(b), mdb.getTime(b, source, destination), mdb.getFare(b, source, destination)))
		h = ['Bus ID', 'Bus type', 'Journey time', 'Journey fare']
		ipop.print_table((h, l))
		return 1

if __name__ == '__main__':
	main()
