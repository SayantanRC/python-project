import sys
import os
import manageDB as mdb
import ipop

def main():

	ipop.cls()

	username = sys.argv[1]

	screen = "_________________________________________________________________\n" + "|\t\t\t\t\t\t\t\t|\n" + "|\tThis page lists all your payment methods.\t\t|\n" + "|\tYou can add or delete some of them\t|\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

	print (screen)

	data = mdb.get_user_detail(username, 'payments')
	if data == None or data == '':
		print ("No payment methods available in this account.")
	else:
		lines = data.split('\n')
		m = list(enumerate(lines, start=1))

		h = ['Option', 'Payment method']

		ipop.print_table((h, m))
	

def exit1(un): os.system("python3 logged_in_main_menu.py '" + un + "'")

if __name__ == '__main__':
	main()
