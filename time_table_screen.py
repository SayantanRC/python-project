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

	screen = "_________________________________________________________________\n" + "|\t\t\t\t\t\t\t\t|\n" + "|\tEnter bus ID to see time-table\t\t\t\t|\n" + "|\tExample: S1, V10, AC5, SL2 etc...\t\t\t|\n" + "|\t\t\t\t\t\t\t\t|\n" + "|\tDon't know bus id? Enter R to see buses between stops.\t|\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

	print (screen)

	ttlist = []

	if username != '':
		try:
			storedtt = mdb.get_user_activity(username, 'time_tables')
			if storedtt != '':
				storedtt = storedtt.split('\n')
				ttlist = list(enumerate(storedtt, start=1))
				print ("||\tYour previous searches:\n")
				h = ['Choice', 'Bus ID']
				tup = (h, ttlist)
				ipop.print_table(tup)
				print ("||\tYou can enter these choices in place of bus ID.\n")
		except: pass


	while True:
		r = disp_tt(username, ttlist)
		if r == 0:
			exit1(username)
			break
		elif r == -1:
			buses_bet_stops(username)
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

def buses_bet_stops(un):
	if un == '':
		os.system("python3 buses_between_stops.py")
	else:
		os.system("python3 buses_between_stops.py '" + un + "'")


def disp_tt(un, ttlist):

	bus_id = ipop.getUserData([str, int], "||\tEnter bus ID or !q to cancel: ", "Wrong data")

	if bus_id == 'R':
		return -1
	elif bus_id == None:
		return 0
	for (i, b) in ttlist:
		if bus_id == i:
			bus_id = b
			break

	tt = mdb.bus_timetable(bus_id, un)

	if tt == []:
		print ("Bus with this ID does not exist.")
		return 1
	else:
		h = ['Bus stop', 'Time']
		c = tt
		tup = (h,c)
		print ("\nTime table for: " + bus_id)
		ipop.print_table(tup)
		return 1

if __name__ == '__main__':
	main()
