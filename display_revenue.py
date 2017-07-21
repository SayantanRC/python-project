
import ipop
import os
import sys
import manageDB as mdb
import calc

def main():

	ipop.cls()
	username = sys.argv[1]
	name = mdb.getNameFromUsername(username)

	fdate = ''
	tdate = ''

	screen = "_________________________________________________________________\n" + "|\t\t\t\t\t\t\t\t|\n" + "|\tHello administrator,\t\t\t\t\t\t\t|\n" + "|\t" + name + "\n" + "|\t\t\t\t\t\t\t\t|\n" + "|\tPlease select the appropriate option:\t\t\t|\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

	print(screen)
	print("||\t1. Print entire table")
	print("||\t2. Print revenue between two dates")
	print("||")

	ip = ipop.getUserData([int], "||\tEnter option: ", "Wrong data entered!", True, ["x in [1,2]"], True)
	print()

	if ip != None:
		ipop.cls()
		if ip == 1:
			h, c, t = mdb.getRevenue()
			ipop.print_table((h, c))
			print('\nTotal revenue: ' + str(t))
			p = input("\nPress any key to go to main menu....")
			exit1(username)
		elif ip == 2:
			while True:

				print("||\tEnter a 'from' date (DD/MM/YYYY): ")
				fdate = reqdate()
				if fdate == '':
					exit1(username)
					break

				print("||\tEnter a 'to' date (DD/MM/YYYY): ")
				tdate = reqdate()
				if tdate == '':
					exit1(username)
					break

				if calc.compareDates(fdate, tdate):
					h, c, t = mdb.getRevenue(fdate, tdate)
					ipop.print_table((h, c))
					print('\nTotal revenue: ' + str(t))
					p = input("\nPress any key to go to main menu....")
					exit1(username)
					break
				else:
					print("The 'from' date is later than 'to' date.\nEnter 1 to re-enter the dates !q to quit")
					p = ipop.getUserData([int, str], "", "")
					if p == 1: continue
					else: break

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
