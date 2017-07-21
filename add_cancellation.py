import sys
import manageDB as mdb
import os
import ipop
import calc

def main():

	ipop.cls()

	username = sys.argv[1]

	screen = "_________________________________________________________________\n" + "|\t\t\t\t\t\t\t\t|\n" + "|\tWelcome to seat cancellation.\t\t\t\t|\n" + "|\tYou will need to provide the ticket number\t\t|\n" + "|\tof every reservation you wish cancel\t\t\t|\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

	print (screen)

	while True:
		ticket_no = ipop.getUserData([str], "||\tEnter ticket number\n||\t", "Wrong data")
		details = mdb.ticketDetails(ticket_no, 1)
		if details == None:
			print("Ticket number does not exist.")

		elif username != details[2]: print("This ticket belongs to a different customer.")

		elif calc.isValidTransactionDate(details[5]):

			username = details[2]
			route_id = details[0]
			bus_id = details[1]
			starting = details[3]
			ending = details[4]
			reservation_date = details[5]
			amount = details[7]

			tickString = "_________________________________________________________________\n" + "||\n" + "||\tReservation in bus ID: " + bus_id + "\n" + "||\tOn route ID: " + route_id + "\n" + "||\tJourney starting from: " + starting + "\n" + "||\tJourney ending at: " + ending + "\n" + "||\tOn date: " + reservation_date + '\n' + "||\tNumber of reservations = 1" + '\n||\n' + "||\tTicket numbers:\n" + '||\t' + ticket_no + '\n' + "||\tTotal amounting to: " + str(amount) + '\n' + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

			print(tickString+'\n')

			p = input("To cancel this ticket, press any key or !q to go back....")
			if p != '!q':
				if (mdb.add_cancellation(ticket_no) != 1):
					print ("Ticket could not be cancelled.")
				else: print ("Ticket cancelled.")
		
		else:
			print("This ticket cannot be cancelled.")

		ip = ipop.getUserData([int, str], "Enter 1 to enter another ticket number, !q to go to main menu.", "Wrong data")
		if ip == 1:
			continue
		else:
			exit1(username)
			break

def exit1(un): os.system("python3 logged_in_main_menu.py '" + un + "'")

if __name__ == '__main__':
	main()
