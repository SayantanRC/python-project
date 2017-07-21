
import ipop
import os
import sys
import manageDB as mdb

def main():

	ipop.cls()
	username = sys.argv[1]
	name = mdb.getNameFromUsername(username)

	screen = "_________________________________________________________________\n" + "|\t\t\t\t\t\t\t\t|\n" + "|\tHello administrator,\t\t\t\t\t\t\t|\n" + "|\t" + name + "\n" + "|\t\t\t\t\t\t\t\t|\n" + "|\tPlease select the appropriate table:\t\t\t|\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

	print(screen)
	print("||\t1. Reservation table")
	print("||\t2. Cancellation table")
	print("||\t3. Route table")
	print("||\t4. Fare chart")
	print("||\t5. Bus table")
	print("||")

	ip = ipop.getUserData([int], "||\tEnter table number: ", "Wrong data entered!", True, ["x in list(range(1,6))"], True)
	print()

	if ip != None:
		ipop.cls()
		mdb.adminDisplayTable(ip)
		p = input("\nPress any key to go to main menu....")

	exit1(username)
	
def exit1(un): os.system("python3 admin_page.py '" + un + "'")

if __name__ == '__main__':
	main()
