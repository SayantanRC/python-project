
import ipop
import os
import sys
import manageDB as mdb
import calc

def main():

	ipop.cls()
	username = sys.argv[1]
	name = mdb.getNameFromUsername(username)

	screen = "_________________________________________________________________\n" + "|\t\t\t\t\t\t\t\t|\n" + "|\tHello administrator,\t\t\t\t\t|\n" + "|\t" + name + "\n" + "|\t\t\t\t\t\t\t\t|\n" + "|\tSee report on reservation/cancellation\t\t\t|\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

	print(screen)

	bid = ''
	rid = ''
	source = ''
	destination = ''
	t = ''
	
	print("\tEnter ATLEAST bus ID, or route ID or source or destination or their combination.\n")

	while True:
		bid = input("||\tEnter bus ID (leave blank to include all buses): ")
		if bid == '!q':
			exit1(username)
			break
		elif bid == '':
			rid = input("||\tEnter route ID (leave blank to include all routes): ")
			if rid == '!q':
				exit1(username)
				break

		source = input("||\tEnter source (leave blank to include all sources): ")
		if source == '!q':
			exit1(username)
			break

		destination = input("||\tEnter destination (leave blank to include all destinations): ")
		if destination == '!q':
			exit1(username)
			break

		t = input("||\tEnter 'r' for reservation or 'c' for cancellation: ")
		if t == '!q':
			exit1(username)
			break

		print()
		h, c = mdb.order_rc_by_month(t, rid, bid, source, destination)
		if c == []:
			print("\nData unavailable.")
		else:
			ipop.print_table((h,c))

		print()
		c = ipop.getUserData([int, str], "||\tEnter 1 for re-search, !q to cancel: ", "Wrong data entered!")
		if c != 1:
			exit1(username)
			break

	
def reqdate():
	d = ''
	while True:
		d = ipop.getUserData([str], '||\t', "Wrong data entered!")
		if d == None:
			return ''
		else:
			if calc.isPreviousDate(d) == False:
				print("Wrong date format or future date entered. Re-enter date or !q to cancel.")
				continue
			else: return d

def exit1(un): os.system("python3 admin_page.py '" + un + "'")

if __name__ == '__main__':
	main()
