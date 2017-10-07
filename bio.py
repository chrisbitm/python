# N DA HOUSE
# Version 1.6

# Person <==> Description 
#
# Use this program to add household
# members and add a humorous description 
# about them

# A demonstration of using a Dictionary
# in Python


# IMPORTS
import os	# Makes Python interact with OS command line

# VARIABLES
ppl = {}			#	A Dictionary containing entries created by the user
choice = None

# CONSTANTS
EXIST = "This Person already exists!"	# If entries exist
INVALID = "This is an invalid selection."	# Invalid Menu Choice
SOMETHING = "Please type something"		# If nothing is typed at prompt
NODATA = "This person is not in the database"	# If entry doesn't exist
NOEXIST = "This person does not exist"		# 
# Game
while choice != "0":
	print("""								
	Welcome to 'N' DA HOUSE			

Add an entry for each individual 	
that lives in your current residence
including yourself

You can even give a humorous
description about them.

Please Enter a number 0-4 to get started!

		0:  Exit
		1:  Add Entry(s)
		2:  View Entry(s)
		3:  Redefine Entry(s)
		4:  Delete Entry(s)
	""")

	choice = input("Menu Choice:  ")	# Menu Choice 0-4
	
	# Exits the program
	if choice == "0":
		input("\n\n" + "Press the Enter key to close winodw")	# Adds two whitelines and inputs key to exit
	
	# Adds a Person to the database
	elif choice == "1":
		print("\n" + "Enter a name of the person "
		"to add " + "to the database.")
		name = input("\n" "Name of Person:  ")
		while True: 
			if name == "":
				print("Please Enter a name \n")
				name  = input("Name of Person: ")
			else:
				break
		name = name.capitalize()
		if name.capitalize() in ppl:
			print("\t",EXIST)
			input("\n" + "Press the Enter key to return to menu.")
			os.system("cls")
		else:
			desc = input("Description:  ")
			if desc == "":
				desc = "None"
			ppl[name] = desc
			print("\n" + " [Person Added Sucessfully]")
			input("Press the Enter key to return to menu.")
			os.system("cls")
		
	
	
	# Views the database 
	elif choice == "2":
		for name in ppl:
			print("\n", name, end="\t \n") # Prints all Persons in database with 1 tab whitespace
		if not ppl:
			print("No Entries in Database...")
			input("\n" + "Press the Enter key to return to menu.")
			os.system("cls")
		else:
			print("\n" + "Above is a list of all the Persons \n"
					"that "
		           "you have defined.  Type in the name that you "
				   "wish to view.")
			name = input("\n" + "Lookup who?:  ")
			name = name.capitalize()
			if name.capitalize() in ppl:
				desc = ppl[name]
				print("\n Name:\t       " + name,"\n Description: ",desc)
				input("\n" + "Press the Enter key to return to menu.")
				os.system("cls")
			else:
				print("That name doesn't exist.  Try creating it.")
				input("\n" "Press the Eneter key to return to menu.")
				os.system("cls")
				
	# Revise the Description to a Person
	elif choice == "3":
		for name in ppl:
			print("\n", name, end="\t \n") # Prints all Persons in database with 1 tab whitespace
		if not ppl:
			print("No Entries in Database...")
			input("\n" + "Press the Enter key to return to menu.")
			os.system("cls")
		else:
			print("\n" + "Above is a list of all the Persons \n"
					"that "
		           "you have defined.  Type in the name that you "
				   "wish to view.")
			name = input("\n" + "Revise Description for who?:  ")
			name = name.capitalize()
			
			while True:
				desc = input("Description:  ")
				if desc == "":
					desc = "None"
				else:
					ppl[name] = desc
					print("\n" + " [Revision Sucessfull]")
					input("Press the Enter key to returns to menu.")
					os.system("cls")
					break
					
					
					
	elif choice == "4":
		for name in ppl:
			print("\n", name, end="\t \n") # Prints all Persons in database with 1 tab whitespace
		if not ppl:
			print("No Entries in Database...")
			input("\n" + "Press the Enter key to return to menu.")
			os.system("cls")
		else:
			print("\n" + "Above is a list of all the Persons \n"
					"that "
		           "you have defined.  Type in the name that you "
				   "wish to view.")
			name = input("\n" + "Delete who?:  ")
			name = name.capitalize()
			while name.capitalize() not in ppl:
				print("Name not in database")
				name = input("\n" + "Delete who?:  ")
			del ppl[name.capitalize()]	
			print("\n" + " [Delete Sucessfull]")
			input("Press the Enter key to returns to menu.")
			os.system("cls")
			
		
# Release Notes
# Oct. 5 2017 [20:26] : New Program
# Oct. 6 2017 [21:07] : Framework Complete
# 