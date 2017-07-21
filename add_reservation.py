import os
import sys
import manageDB as mdb
import ipop
import calc

def main():

	ipop.cls()

	username = sys.argv[1]

	screen = "_________________________________________________________________\n" + "|\t\t\t\t\t\t\t\t|\n" + "|\tWelcome to seat reservation.\t\t\t\t|\n" + "|\tYou will be guided through the reservation process.\t|\n" + "|\tPlease enter the relevant information as asked.\t\t|\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

	print (screen)

	print ("\nOn entering the start and end of your journey\nwe will automatically list the available buses for you to choose.\nYou can quit the process anytime by entering !q\n")

	routeFlag = False
	dateFlag = False
	seatFlag = False
	seatReserveFlag = False

	source = ''
	destination = ''
	bus_id = ''
	date = ''
	n = 0
	seats = []
	bookedSeats = []
	fare = 0
	amount = 0

	ts = '00:00'
	te = '00:00'

	tickets = []

	while True:
		date = ipop.getUserData([str], "||\tEnter date of journey: (as DD/MM/YYYY format):\n||\t", "Wrong data")
		if date == None:
			return 0
		else:
			if calc.isValidTransactionDate(date):
				dateFlag = True
				break
			else: print("Invalid date or wrong date format given.")


	while dateFlag:

		source = ipop.getUserData([str], "||\tEnter source:\n||\t", "Wrong data")
		if source == None:
			exit1(username)
			break
		destination = ipop.getUserData([str], "||\tEnter destination:\n||\t", "Wrong data")
		if destination == None:
			exit1(username)
			break
		buses = mdb.buses_between_stops(source, destination)
		if buses == []:
			print ("Sorry, this route does not exist. Press 1 to re-enter start and destination, !q to cancel and go to main menu.")
			p = ipop.getUserData([str, int], "", "Wrong data")
			if p == 1: continue
			else:
				exit1(username)
				break
		else:
			bus_details = []
			for b in buses:
				bus_type = mdb.getBusType(b)
				bus_fare = mdb.getFare(b, source, destination)
				n_seats = len(mdb.availableSeats(b, source, destination, date))
				bus_details.append((b, bus_type, bus_fare, n_seats))
			bh = ['Bus ID', 'Type', 'Fare', 'Seats available']
			print ("\nFollowing buses are available:")
			ipop.print_table((bh, bus_details))
			print()
			bus_id = ipop.getUserData([str], "||\tEnter bus id:\n||\t", "Choose among the available buses.", True, ['x in ' + str(buses)], True)
			if bus_id == None:
				exit1(username)
			else: routeFlag = True
			break


	if routeFlag:
		print ("Almost there....")
		while True:
			n = ipop.getUserData([int], "||\tEnter number of seats to be reserved:\n||\t", "Wrong data")
			if n == None:
				exit1(username)
			else:
				seats = mdb.availableSeats(bus_id, source, destination, date)
				if n > len(seats):
					print("The requested number of seats is currently not available in " + bus_id + " on " + date)
					p = ipop.getUserData([int, str], "||\tEnter 1 to decrease number of seats or !q to cancel:\n||\t", "Wrong data")
					if p == 1: continue
					else:
						exit1(username)
						break
				else:
					seatFlag = True
					break


	if seatFlag:
		p = ipop.getUserData([str], "||\tEnter S to manually select seats or any other key for automatic selection:\n||\t", "Wrong data")
		if p == None:
			exit1(username)
		elif p == 'S' or p == 's':
			print ("||\tAvailable seats are:")
			print (seats)
			print ("||\tEnter seat numbers for " + str(n) + " reservations")
			for i in range(n):
				s = ipop.getUserData([int], "", "Wrong data", True, ['x in ' + str(seats)], True)
				if s == None:
					exit1(username)
				bookedSeats.append(s)
		else:
			for i in range(n):
				s = seats[i]
				bookedSeats.append(s)
		seatReserveFlag = True
		print ("||\tBooked seats are: " + str(bookedSeats) + '\n')

	if seatReserveFlag:
		fare = mdb.getFare(bus_id, source, destination)
		amount = n*fare
		print("||\tAll set! Total Fare = " + str(n) + " * " + str(fare) + " = " + str(amount))
		print("||\tPress any key to book. !q to cancel")
		p = input()
		if p == None:
			exit1(username)
		else:
			for bs in bookedSeats:
				tickets.append(mdb.add_reservation(bus_id, username, source, destination, date, bs, fare) + '\t' + str(bs))

			timetable = mdb.bus_timetable(bus_id)
			for place, time in timetable:
				if source == place: ts = time
				if destination == place: te = time

			ticket_print(username, tickets, bus_id, mdb.getRouteFromBusID(bus_id), source, destination, date, n, amount, ts, te)
		
		
def ticket_print(un, tickets, bus_id, route_id, source, destination, date, n, amount, ts, te):

	ticketsConcat = ''
	for t in tickets:
		ticketsConcat = ticketsConcat + "||\t" + t + '\n'

	tickString = "_________________________________________________________________\n" + "||\n" + "||\tReservation in bus ID: " + bus_id + "\n" + "||\tOn route ID: " + route_id + "\n" + "||\tJourney starting from: " + source + "\n" + "||\tJourney ending at: " + destination + "\n" + "||\tOn date: " + date + '\n' + "||\tJourney from: " + ts + " to " + te + '\n' + "||\tNumber of reservations = " + str(n) + '\n||\n' + "||\tTicket numbers:\t\tSeat no:\n" + ticketsConcat + '||\n' + "||\tTotal amounting to: " + str(amount) + '\n' + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"

	ipop.cls()
	print (tickString + '\n')
	print ("Please note down the ticket numbers.\n")
	p = input("Press any key to go to main menu....")
	exit1(un)

def exit1(un): os.system("python3 logged_in_main_menu.py '" + un + "'")

if __name__ == '__main__':
	main()
