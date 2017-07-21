
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

	fdate = ''
	tdate = ''
	cat = 0
	t = ''
	

	while True:
		print("\tCatagories:\n\t1. Sort according to bus IDs\n\t2. According to route IDs\n\t3. According to actual routes\n")
		cat = ipop.getUserData([int], "||\tEnter category: ", "Wrong data entered!", True, ["x in [1,2,3]"], True)
		if cat == None:
			exit1(username)
			break

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
		
		print("\tType:\n\tr. See reservations\n\tc. See cancellations\n")
		t = ipop.getUserData([str], "||\tEnter type: ", "Wrong data entered!", True, ["x in ['r', 'c']"], True)
		if t == None:
			exit1(username)
			break

		print()
		h, c, t = mdb.order_rc_by_catagories(cat, fdate, tdate, t)
		ipop.print_table((h,c))
		print("\nTotal count: " + str(t) + '\n')

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
