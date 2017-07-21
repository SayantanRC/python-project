
import ipop
import os
import sys
import manageDB as mdb

def main():

	ipop.cls()
	username = sys.argv[1]
	name = mdb.getNameFromUsername(username)

	screen = "_________________________________________________________________\n" + "|\t\t\t\t\t\t\t\t|\n" + "|\tHello administrator,\t\t\t\t\t|\n" + "|\t" + name + "\n" + "|\t\t\t\t\t\t\t\t|\n" + "|\tPlease select the appropriate option:\t\t\t|\n" + "|\t1) Print tables\t\t\t\t\t\t|\n" + "|\t2) Print revenue\t\t\t\t\t|\n" + "|\t3) Sort reservation/cancellation catagory-wise\t\t|\n" + "|\t4) Sort reservation/cancellation month-wise\t\t|\n" + "|\t\t\t\t\t\t\t\t|\n" + "|\tL) Logout\t\t\t\t\t\t|\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

	print(screen)

	p = "Enter option (1-4,L): "
	ip = ipop.getUserData([int, str], p, "Wrong data entered!", True, ["x in list(range(1,5))", "x == 'L'"], True)

	if ip == 1:
		os.system("python3 display_tables.py '" + username + "'")
	if ip == 2:
		os.system("python3 display_revenue.py '" + username + "'")
	if ip == 3:
		os.system("python3 sort_rc_cat.py '" + username + "'")
	if ip == 4:
		os.system("python3 sort_rc_month.py '" + username + "'")
	elif ip == 'L':
		os.system("python3 main_menu.py")

if __name__ == '__main__':
	main()
