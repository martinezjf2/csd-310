"""
          Title: what_a_book.py
          Name: Alynna Rem
          Date: 13 May 2022
          Description: WhataBook console program that ingerfaces with the whatabook MySQL database
"""

""" import statements """
import sys
import mysql.connector
from mysql.connector import errorcode

""" database configuration object """
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

# define method to show menu
def show_menu():
	# print -- Main Menu --
	print("\n   -- Main Menu --\n")
	# print options from User Interface Requirements
	print ("   1. View Books\n   2. View Store Locations\n   3. My Account\n   4. Exit Program\n")
    
    # use try and except to prompt the user for their option, then read and validate the number entered corresponds to an option.
	try:
		menu_option = int(input("Please enter the number that corresponds with your menu option: "))
		return menu_option

	# display a ValueError with an error message if the number entered is invalid.
	except ValueError: 
		print("\n The number entered does not correspond to an option listed above, program terminated... \n")
		sys.exit(0)


# define method to show books
def show_books(_cursor):
	# execute inner join query
	_cursor.execute("SELECT book_id, book_name, author, details FROM book")

	# get results from cursor object
	books = _cursor.fetchall()

	# print -- Displaying Book Listing --
	print("\n\n   -- Displaying Book Listing --\n")

	# for loop to iterate over the book data set and display the results
	for book in books:
		print("     Book ID: {}\n     Book Name: {}\n     Author: {}\n     Details: {}\n".format(book[0], book[1], book[2],book[3]))

# define method to show locations
def show_locations(_cursor):
	_cursor.execute("SELECT store_id, locale, hours from store")

	# get results from cursor object
	locations = _cursor.fetchall()

	# print -- Displaying Store Locations --
	print("\n\n   -- Displaying Store Locations --\n")

	# for loop to iterate over the location data set and display the results
	for location in locations:
		print("     Store_ID:{}\n     Locale: {}\n     Hours: {}\n\n".format(location[0], location[1], location[2]))

# define method to validate user ID
def validate_user():

	# use try and except to read and validate the user id.
	try:
		user_id = int(input("\nEnter your user ID: "))

		# if user ID entered is invalid, display an error message.
		if user_id < 0 or user_id > 3:
			print("\nThe user ID you've entered is invalid, terminating program...")
			sys.exit(0)

		return user_id
	except ValueError:
		print("\nThe user ID you've entered is invalid, terminating program...")
		sys.exit(0)

# define method to show account menu
def show_account_menu():

	# use try and except to read and validate user's option from user's account menu.
	try:
		print("\n\n   -- Account Menu --\n")
		print("   1. Wishlist\n   2. Add Book\n   3. Main Menu\n")
		account_menu_option = int(input("Please enter the number that corresponds with your option: "))

		return account_menu_option
	except ValueError:
		print("\n The number you've entered is invalid, terminating program..")
		sys.exit(0)

# define method to show wishlist
def show_wishlist(_cursor, _user_id):

	# execute inner join to display user wishlist
	_cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " +
		            "FROM wishlist " +
		            "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))

	# get the results from the cursor object
	wishlist = _cursor.fetchall()

	# print -- Displaying Wishlist Items --
	print("\n\n   -- Displaying Wishlist Items --\n")

	# for loop to iterate over the wishlist data set and display results.
	for book in wishlist:
		print("     Book Name: {}\n     Author: {}\n".format(book[4], book[5]))

# define method to show books excluded from user's wishlist.
def show_books_to_add(_cursor, _user_id):

    # execute query to return a list of books excluded from user's wishlist.
	_cursor.execute("SELECT book_id, book_name, author, details " +
                    "FROM book " +
                    "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
    
    # get the results from the cursor object
	books_to_add = _cursor.fetchall()

    # print -- Displaying Available Books --
	print("\n\n -- Displaying Available Books --\n")

	# for loop to iterate over the books excluded from user's wishlist
	for book in books_to_add:
		print("     Book ID: {}\n     Book Name: {}\n     Author: {}\n     Details: {}\n".format(book[0], book[1], book[2],book[3]))

# define method to add book to wishlist
def add_book_to_wishlist(_cursor, _user_id, _book_id):
	_cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))


""" The following will execute the program with try/except to catch any other errors """

try:

	# connect to the WhatABook database
	db = mysql.connector.connect(**config)

	# cursor for MySQL queries
	cursor = db.cursor()

	# print welcome message to user
	print("\n  Welcome to the WhatABook Application! ")

	# call the main menu method.
	user_selection = show_menu()

	# while the user's selection is not 4 (Exit Program)
	while user_selection != 4:

		# if user enters option 1, call the show_books method
		if user_selection == 1: 
			show_books(cursor)

		# if user enters option 2, call the show_locations method
		if user_selection == 2:
			show_locations(cursor)

		# if user enters option 3, call the validate_user method
		# Then call the show_account_menu() method
		if user_selection == 3:
			my_user_id = validate_user()
			account_menu_option = show_account_menu()

			# while account option does not equal 3
			while account_menu_option != 3:

				# if user enters option 1, call the show_wishlist() method
				if account_menu_option == 1:
					show_wishlist(cursor, my_user_id)

				# if user enters option 2, call the show_books_to_add() method
				if account_menu_option == 2:

					# display books excluded from user's wishlist
					show_books_to_add(cursor, my_user_id)

					# get the entered book_id
					book_id = int(input("\n   Enter the Book ID of the book you want to add: "))

					# call the add_book_to_wishlist method and add the book to the user's wishlist
					add_book_to_wishlist(cursor, my_user_id, book_id)

					# commit the changes to the database
					db.commit()

					print("\n     Book ID: {} was added to your wishlist!".format(book_id))

				# if the selected option is invalid (less than 0 or greater than 3), display error
				if account_menu_option < 0 or account_menu_option > 3:
					print("\n The number you've entered is invalid, please retry...")

				# show the main menu
				account_menu_option = show_account_menu()

		# if the user selection is less than 0 or greater than 4, display an invalid user selection
		if user_selection < 0 or user_selection > 4: 
			print("\n The number you've entered is invalid, please retry...")

		# show the main menu
		user_selection = show_menu()

	print("\n\n Program terminated...")

# handle errors
except mysql.connector.Error as err:

	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("  The supplied username or password are invalid")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("  The specified database does not exist")
	else:
		print(err)

# close the connection to MySQL
finally:
    db.close()








    





















