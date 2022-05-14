# Julia Martin Module 12 assignment 5-11-22
# Whatabook Project 

#import statements
import sys
import mysql.connector
from mysql.connector import errorcode

#mysql configuration 
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}
#create main menu function and display four choices
def main_menu():
    print("        --WhatABook Main Menu--")
    print("\n Please enter the number that corresponds with your desired choice \n")
    print("  1. View Books\n  2. View Store Locations\n  3. My Account\n  4. Exit Program\n")

#use try/except to prompt user of choice 
    try:
        choice = int(input('     Enter your choice:  '))

        return choice
    #use except if use enters an invalid choice
    except ValueError:
        print("\n You entered an invalid choice, program exiting.. \n")
        #close program
        sys.exit(0)

#create view books function
def view_books(_cursor):
    #create inner join query
    _cursor.execute("SELECT book_id, book_name, details, author from book")
    #return results
    books = _cursor.fetchall()
    #print results
    print("\n  -- BOOK LISTING --")

    # for loop to print each book result
    for book in books:
        print("  Book ID: {}\n  Book Name: {}\n  Details: {}\n  Author: {}\n".format(book[0], book[1], book[2], book[3]))

def view_locations(_cursor):

    _cursor.execute("SELECT store_id, locale from store")

    locations = _cursor.fetchall()

    print("\n  -- DISPLAYING STORE LOCATIONS --")

    for location in locations:
        print("  Store ID: {}\n  Locale: {}\n".format(location[0], location[1]))

def validate_user():

    # take user input and validate it as a user ID
    try:
        user_id = int(input('\n      Please enter your customer ID: '))

        if user_id < 0 or user_id > 3:
            print("\n  The customer ID you entered is invalid, exiting program \n")
            sys.exit(0)

        return user_id
    except ValueError:
        print("\n  You entered an invalid choice, exiting program \n")

        sys.exit(0)

def view_account_menu():
    # display the user account menu
    try:
        print("\n      -- Customer Menu --")
        print("        1. Wishlist\n        2. Add Book\n        3. Main Menu")
        account_option = int(input('        Please Enter the number corresponding with your choice: '))

        return account_option
    except ValueError:
        print("\n  The number entered is invalid\n")

        sys.exit(0)

def view_wishlist(_cursor, _user_id):

    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    
    wishlist = _cursor.fetchall()

    print("\n        -- WISHLIST ITEMS --")

    for book in wishlist:
        print("        Book Name: {}\n        Author: {}\n".format(book[4], book[5]))

def view_books_to_add(_cursor, _user_id):
    # query database for books not in a wishlist
    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))

    print(query)

    _cursor.execute(query)

    books_to_add = _cursor.fetchall()

    print("\n        -- AVAILABLE BOOKS --")

    for book in books_to_add:
        print("        Book Id: {}\n        Book Name: {}\n".format(book[0], book[1]))

def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

try:
    # connect to the whatabook database
    db = mysql.connector.connect(**config)  
    #use cursor for MySQL queries
    cursor = db.cursor()
    #print message
    print("\n  Welcome to the WhatABook Application! ")
    # display main menu
    user_selection = main_menu() 

    # while the user's selection is not 4
    while user_selection != 4:

        # if the user selects option 1, call the show_books method and display the books
        if user_selection == 1:
            view_books(cursor)

        # if the user selects option 2, call the show_locations method and display the configured locations
        if user_selection == 2:
            view_locations(cursor)

        # if the user selects option 3, call the validate_user method to validate the entered user_id 
        # call the show_account_menu() to show the account settings menu
        if user_selection == 3:
            my_user_id = validate_user()
            account_option = view_account_menu()

            # while account option does not equal 3
            while account_option != 3:

                # if the user selects option 1, call the view_wishlist() method to show the current users 
                # configured wishlist items 
                if account_option == 1:
                    view_wishlist(cursor, my_user_id)

                # if the user selects option 2, call the view_books_to_add function to show the user 
                # the books not currently configured in the users wishlist
                if account_option == 2:

                    # show the books not currently configured in the users wishlist
                    view_books_to_add(cursor, my_user_id)

                    # get the entered book_id 
                    book_id = int(input("\n        Enter the ID of the book you want to add: "))
                    
                    # add the selected book the users wishlist
                    add_book_to_wishlist(cursor, my_user_id, book_id)

                    # commit changes to the database
                    db.commit()

                    print("\n        Book id: {} was added to your wishlist!".format(book_id))

                # if the selected option is less than 0 or greater than 3, display an invalid user selection 
                if account_option < 0 or account_option > 3:
                    print("\n      Invalid option, please try again...")

                # display the account menu 
                account_option = view_account_menu()
        
        # if the user selection is less than 0 or greater than 4, display an invalid user selection
        if user_selection < 0 or user_selection > 4:
            print("\n      Invalid option, please try again...")
            
        # show the main menu
        user_selection = main_menu()

    print("\n\n  Program terminated...")

# use except to display message if error occurs
except mysql.connector.Error as err:
    

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    
    #end connection with MySQL
    db.close()








    