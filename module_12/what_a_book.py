


import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

# db = mysql.connector.connect(**config)

try:
    db = mysql.connector.connect(**config)
    
    print("\nDatabase user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
    input("\n\nPress any key to continue...\n\n")
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)
        
cursor = db.cursor()

# To display a user’s Wishlist you will need to use two INNER JOINs to combine the user and book tables.
# Store, Book, Wishlist, User.
# To add a book to the users wishlist you will need to capture the selected book_id and user_id.
# To view a list of books not in the users wishlist you will need to use the NOT IN operator with a nested query.
# WHERE book_id NOT IN ( SELECT book_id FROM wishlist WHERE user_id = ).
# If you get stuck, the course's GitHub repository has an SQL script that includes all of the SQL queries. But, again, only use this as a last resort. To truly learn these topics, you will need to make an effort and try to complete the project on your own.



def main():
    print("this is main")
    
def show_menu():
    print("show Menu")
    
def show_books(_cursor):
    print("Show books")
    
def show_locations(_cursor):
    print("Show Locations")
    
def validate_user():
    print("validate User")
    
def show_account_menu():
    print("show account menu")
    
def show_wishlist(_cursor, _user_id):
    print("show wishlist by user_id")

def show_books_to_add(_cursor, _user_id):
    print("Show books to add")
    
def account_menu():
    print("display account menu")
    


# Use variables to capture the user’s entry for user_id
# Use variables to capture the user’s entry for book_id