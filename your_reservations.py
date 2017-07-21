import sys
import os
import manageDB as mdb
import ipop

def main():

	ipop.cls()

	username = sys.argv[1]

	screen = "_________________________________________________________________\n" + "|\t\t\t\t\t\t\t\t|\n" + "|\tThis page lists all the reservations done\t\t|\n" + "|\tfrom this account.\t\t\t\t\t|\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

	print (screen)

	data = mdb.get_user_activity(username, 'reservations')
	if data == None or data == '':
		print ("No reservation data available in this account.")
		p = input("Press any key to go to main menu...")
		exit1(username)
	else:
		lines = data.split('\n')
		m = []
		for line in lines:
			m.append(tuple(line.split('_')))

		h = ['Ticket no.', 'Reserved on', 'Bus ID', 'Source', 'Destination', 'Journey date', 'Seat no.', 'Amount']

		ipop.print_table((h, m))

		p = input("\nPress any key to go to main menu...")
		exit1(username)
	

def exit1(un): os.system("python3 logged_in_main_menu.py '" + un + "'")

if __name__ == '__main__':
	main()
