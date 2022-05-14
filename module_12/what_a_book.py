


# Jeffrey Martinez
# Module 12.3 Assignment
# May 12, 2022




import sys
import mysql.connector
from mysql.connector import errorcode
from termcolor import cprint

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

# db = mysql.connector.connect(**config)

# try:
#     db = mysql.connector.connect(**config)
    
#     print("\nDatabase user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
#     input("\n\nPress any key to continue...\n\n")
    
# except mysql.connector.Error as err:
#     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#         print("The supplied username or password are invalid")
#     elif err.errno == errorcode.ER_BAD_DB_ERROR:
#         print("The specified database does not exist")
#     else:
#         print(err)
        
# cursor = db.cursor()

# To display a user’s Wishlist you will need to use two INNER JOINs to combine the user and book tables.
# Store, Book, Wishlist, User.
# To add a book to the users wishlist you will need to capture the selected book_id and user_id.
# To view a list of books not in the users wishlist you will need to use the NOT IN operator with a nested query.
# WHERE book_id NOT IN ( SELECT book_id FROM wishlist WHERE user_id = ).
# If you get stuck, the course's GitHub repository has an SQL script that includes all of the SQL queries. But, again, only use this as a last resort. To truly learn these topics, you will need to make an effort and try to complete the project on your own.

def print_choice_options():
    print("1. View Books")
    print("2. View Locations")
    print("3. View My Account")
    print("4. Exit\n\n")
    

def show_menu():
    cprint("\n\nChoose from the following options \n", "blue")
    print_choice_options()
    
    try:
        users_choice = int(input("You chose: "))
        return users_choice
    except ValueError:
        cprint("Invalid number, Please choose one of the following", "red")
        print_choice_options()
    

    
def show_books(_cursor):
    
    _cursor.execute("SELECT book_id, book_name, author, details from book")
    books = _cursor.fetchall()
    cprint("\n\nDISPLAYING LIST OF BOOKS  ", "blue")
    
    for book in books:
        print(f"\nBook Name: {book[0]}")
        print(f"Author: {book[1]}")
        print(f"Details: {book[2]}")
    print("\n")
             
        
    
def show_locations(_cursor):
    _cursor.execute("SELECT store_id, locale from store")
    stores = _cursor.fetchall()
    cprint("\n\nDISPLAYING STORE LOCATIONS  \n\n", "blue")
    
    for location in stores:
        print(f"Locale: {location[1]}")
        
             
    
def validate_user():
    try:
        user = int(input("\nPlease enter your customer id: "))
        if user < 0 or user > 3:
            cprint("\n\nInvalid User, please try again\n", "red")
            validate_user()
        return user
    except ValueError:
        cprint("Invalid Number, closing the program...", "red")
        sys.exit(0)
    
    
    
def show_account_menu():
    try:
        cprint("\n\nPlease choose from the following options: \n", "blue")
        print(f"\n1. Wishlist")
        print(f"2. Add Book")
        print(f"3. Main Menu\n")
        option = int(input("You chose: "))
        return option
    except ValueError:
        cprint("Invalid Number, closing the program...","red")
        sys.exit(0)
        
    
def show_wishlist(_cursor, _user_id):
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " + 
                    "FROM wishlist " + 
                    "INNER JOIN user ON wishlist.user_id = user.user_id " + 
                    "INNER JOIN book ON wishlist.book_id = book.book_id " + 
                    "WHERE user.user_id = {}".format(_user_id))
    wishlist = _cursor.fetchall()
    cprint(" \n\n DISPLAYING WISHLIST ITEMS  ","blue")
    
    for book in wishlist:
        print(f"\nBook Name: {book[4]}")
        print(f"Author: {book[5]}")
    print("\n")


def show_books_to_add(_cursor, _user_id):
    query = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
    _cursor.execute(query)
    add_books = _cursor.fetchall()
    cprint("\n\nAVAILABLE BOOKS  \n", "blue")
    
    for book in add_books:
        print(f"\nBook ID: {book[0]}")
        print(f"Book Name: {book[1]}")
    print("\n")   
    
    
def check_book_id(_cursor, _user_id):
    book = int(input("\nEnter the id of the book you want to add: "))
    
    _cursor.execute("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {}) AND book_id = {}".format(_user_id, book))
    data = _cursor.fetchall()
    
  
    if not data:
        cprint("\n\nBOOK ID NOT FOUND IN THE DATABASE", "red")
        check_book_id(_cursor, _user_id)
    else:
        return book
   
       
    
def add_book_to_wishlist(_cursor, _user_id, _book_id):
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))

try:
    db = mysql.connector.connect(**config) 
    cursor = db.cursor() 
    cprint("\nWelcome to the WhatABook Application! ", "blue")
    
    user_selection = show_menu() 

    while user_selection != 4:

        if user_selection == 1:
            show_books(cursor)

        if user_selection == 2:
            show_locations(cursor)

        if user_selection == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()

            while account_option != 3:

                if account_option == 1:
                    show_wishlist(cursor, my_user_id)

                if account_option == 2:
                    show_books_to_add(cursor, my_user_id)
                    checked_book = check_book_id(cursor, my_user_id)
                    
                    if checked_book:
                        add_book_to_wishlist(cursor, my_user_id, checked_book)
                        db.commit() 
                        cprint(f"\nBook ID: {checked_book} was successfully added to your wishlist!", "green")

                if account_option < 0 or account_option > 3:
                    cprint("\nInvalid option, please retry...", "red")

                account_option = show_account_menu()
        
        if user_selection < 0 or user_selection > 4:
            cprint("\nInvalid option, please retry...", "red")
       
        user_selection = show_menu()

    cprint("\n\nThank You for joining WhatABook. Have a nice day!\n\n", "green")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        cprint("  The supplied username or password are invalid","red")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        cprint("The specified database does not exist", "red")
    else:
        print(err)
finally:
    db.close()
    