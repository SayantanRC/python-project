
import manageDB as mdb
import ipop
import os
import sys

def main():

	ipop.cls()

	back = "python3 main_menu.py"
	uok = False

	while True:
		username = ipop.getUserData([str], "||\tEnter username:\n||\t", "Wrong data!")
		if username == None:
			os.system(back)
			break
		else:
			if mdb.checkUsernamePresence(username):
				uok = True
				break
			else: print ("Username not present.")

	while uok:
		password = ipop.getUserData([str], "||\tEnter password:\n||\t", "Wrong data!")
		if password == None:
			os.system(back)
			break
		else:
			r = mdb.doesPasswordMatch(username, password)
			if r == 1:
				if mdb.verifyAdmin(username, password): os.system("python3 admin_page.py '" + username + "'")
				else: os.system("python3 logged_in_main_menu.py '" + username + "'")
				break
			elif r == -1: print ("Wrong password.")
			else:
				print("Error!")
				break

if __name__ == '__main__':
	main()

	
