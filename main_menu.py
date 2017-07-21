#!usr/bin/env python3

import ipop
import os
import sys

import manageDB as mdb

def main():

	ipop.cls()
	mdb.initialise()

	try:
		print(sys.argv[1])
	except: pass

	screen = "_________________________________________________________________\n" + "|\t\t\t\t\t\t\t\t|\n" + "|\tWelcome\t\t\t\t\t\t\t|\n" + "|\t\t\t\t\t\t\t\t|\n" + "|\tPlease select the appropriate option:\t\t\t|\n" + "|\t1) Bus time table\t\t\t\t\t|\n" + "|\t2) Buses between stops\t\t\t\t\t|\n" + "|\t3) Seat availability\t\t\t\t\t|\n" + "|\t\t\t\t\t\t\t\t|\n" + "|\tLogin and get access to\t\t\t\t\t|\n" + "|\tSeat booking\t\t\t\t\t\t|\n" + "|\tand much more...\t\t\t\t\t|\n" + "|\t\t\t\t\t\t\t\t|\n" + "|\tL) LOGIN\t\t\t\t\t\t|\n" + "|\tNot registered yet? Getting an account is easy\t\t|\n" + "|\tS) SIGN UP >>>>\t\t\t\t\t\t|\n" + "|\t\t\t\t\t\t\t\t|\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

	print(screen)

	p = "Enter option (1,2,3,L,S): "
	ip = ipop.getUserData([int, str], p, "Wrong data entered!", True, ["x in [1, 2, 3]", "x in ['L', 'S']"], True)
	if ip == 'L':
		os.system("python3 login_screen.py")
	elif ip == 'S':
		os.system("python3 sign-up_screen.py")
	elif ip == 1:
		os.system("python3 time_table_screen.py")
	elif ip == 2:
		os.system("python3 buses_between_stops.py")
	elif ip == 3:
		os.system("python3 seat_availability.py")

if __name__ == '__main__':
	main()
