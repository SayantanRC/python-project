import manageDB as mdb
import os
import ipop


def main():

	ipop.cls()

	uok = False

	screen = "_________________________________________________________________\n" + "|\t\t\t\t\t\t\t\t|\n" + "|\tSign up to get exclusive benefits!\t\t\t|\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

	print(screen)

	name = ipop.getUserData([str], "||\tEnter name: ", "Wrong data!", True, ['x != ""'])

	while True:
		username = ipop.getUserData([str], "||\tEnter username: ", "Wrong data!", True, ['x != ""'])
		if mdb.checkUsernamePresence(username) == False:
			break
		else: print("Username already present, choose another username.")

	password = ipop.getUserData([str, int, float], "||\tEnter password: ", "Wrong data!", True, ['x != ""'])

	confirm = "Enter any character to confirm OR '!q' to cancel registration....\n"
	print(confirm)
	c = ipop.getUserData([str], '', 'Enter any character.')

	if c != None:
		try:
			mdb.add_user(name, username, password, '', '')
			alert = "'\nRegistration successful! Please login again..\n'"
			os.system("python3 main_menu.py " + alert)
		except:
			print('Registration unsuccessful..')
			exit(0)
	else:
		alert = "\nRegistration cancelled..\n"
		os.system("python3 main_menu.py")

if __name__ == '__main__':
	main()
