
import ipop
import os
import sys
import manageDB as mdb

def main():

	ipop.cls()
	username = sys.argv[1]
	name = mdb.getNameFromUsername(username)

	screen = "_________________________________________________________________\n" + "|\t\t\t\t\t\t\t\t|\n" + "|\tHello,\t\t\t\t\t\t\t|\n" + "|\t" + name + "\n" + "|\t\t\t\t\t\t\t\t|\n" + "|\tPlease select the appropriate option:\t\t\t|\n" + "|\t1) Bus time table\t\t\t\t\t|\n" + "|\t2) Buses between stops\t\t\t\t\t|\n" + "|\t3) Seat availability\t\t\t\t\t|\n" + "|\t\t\t\t\t\t\t\t|\n" + "|\t\t\t\t\t\t\t\t|\n" + "|\tStart your journey...\t\t\t\t\t|\n" + "|\t4) Book a seat\t\t\t\t\t\t|\n" + "|\t5) Cancel a seat\t\t\t\t\t|\n" + "|\t\t\t\t\t\t\t\t|\n" + "|\tYour activities\t\t\t\t\t\t|\n" + "|\t6) Your reservations\t\t\t\t\t|\n" + "|\t7) Your cancellations\t\t\t\t\t|\n" + "|\t\t\t\t\t\t\t\t|\n" + "|\tNot " + name + "?\n" + "|\tL) Logout\t\t\t\t\t\t|\n" + "|\t\t\t\t\t\t\t\t|\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

	print(screen)

	p = "Enter option (1-7,L): "
	ip = ipop.getUserData([int, str], p, "Wrong data entered!", True, ["x in list(range(1,8))", "x == 'L'"], True)

	if ip == 'L':
		os.system("python3 main_menu.py")
	elif ip == 1:
		os.system("python3 time_table_screen.py '" + username + "'")
	elif ip == 2:
		os.system("python3 buses_between_stops.py '" + username + "'")
	elif ip == 3:
		os.system("python3 seat_availability.py '" + username + "'")
	elif ip == 4:
		os.system("python3 add_reservation.py '" + username + "'")
	elif ip == 5:
		os.system("python3 add_cancellation.py '" + username + "'")
	elif ip == 6:
		os.system("python3 your_reservations.py '" + username + "'")
	elif ip == 7:
		os.system("python3 your_cancellations.py '" + username + "'")

if __name__ == '__main__':
	main()
