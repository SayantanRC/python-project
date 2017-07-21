import os
import sys
import manageDB as mdb
import ipop
import sys
import os
import calc

def main():

	ipop.cls()

	username = ''

	try:
		username = sys.argv[1]
		if mdb.checkUsernamePresence(username) == False: username = ''
	except: pass

	screen = "_________________________________________________________________\n" + "|\t\t\t\t\t\t\t\t|\n" + "|\tEnter source, destination, date and bus ID of journey\t|\n" + "|\tto get available seats before planning reservation\t|\n" + "|\tExample: Howrah to Haldia on 20/08/2017 in AC8\t\t|\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

	print (screen)
	print("\nEnter !q to cancel anytime.\n")

	while True:
		r = disp_seats()
		if r == 0:
			exit1(username)
			break
		else:
			ch = ipop.getUserData([int, str], "||\tEnter 1 to see more seat availabilities or !q for main menu.\n\t", "Wrong data.")
			if ch == 1: continue
			else:
				exit1(username)
				break


def exit1(un):
	if un == '':
		os.system("python3 main_menu.py")
	else:
		os.system("python3 logged_in_main_menu.py '" + un + "'")


def disp_seats():

	source = ipop.getUserData([str], "||\tEnter source of journey:\n||\t", "Wrong data")
	if source == None:
		return 0

	destination = ipop.getUserData([str], "||\tEnter destination of journey:\n||\t", "Wrong data")
	if destination == None:
		return 0

	
	while True:
		date = ipop.getUserData([str], "||\tEnter date of journey: (as DD/MM/YYYY format):\n||\t", "Wrong data")
		if date == None:
			return 0
		else:
			if calc.isValidTransactionDate(date):
				break
			else: print("Invalid date or wrong date format given.")

	buses = mdb.buses_between_stops(source, destination)
	if buses != []:
		bus_details = []
		for b in buses:
			n_seats = len(mdb.availableSeats(b, source, destination, date))
			bus_details.append((b, n_seats))
		bh = ['Bus ID', 'Seats available']
		print ("\nFollowing buses are available:")
		ipop.print_table((bh, bus_details))
		print()

	bus_id = ipop.getUserData([str], "||\tEnter bus ID:\n||\t", "Wrong data")
	if bus_id == None:
		return 0

	buses = mdb.buses_between_stops(source, destination)
	if bus_id not in buses:
		print ("This journey does not exist!!")
		return 1
	
	seats = mdb.availableSeats(bus_id, source, destination, date)
	if seats == []: print ("No more seats are available in this bus for the given date!")
	else:
		print("||\tAvailable seats are:")
		print(seats)
		return 1

if __name__ == '__main__':
	main()
