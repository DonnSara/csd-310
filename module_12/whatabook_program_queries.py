import sys
import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "localhost",
    "database": "whatabook",
    "raise_on_warnings": True
}

def show_menu():
    """ Print the main menu """
    print("\n -- MAIN MENU -- \n\t1. Books\n\t2. Store Locations\n\t3. My Account\n\t4. Exit Program\n")
    try:
        option = int(input('Select a menu <Example 1 for book listing>: '))
        return option
    except ValueError:
        """ Handles errors that may come up """
        print("\n Invalid number entered, program terminated...\n")
        sys.exit(0)
    
def show_books(_cursor):
    """ Display books in database """
    _cursor.execute("SELECT book_id, book_name, author, details FROM book")
    books = _cursor.fetchall()
    print ("\n -- DISPLAYING BOOK LISTING --")
    for book in books:
        print("\n\tBook Name: {}\n\t Author: {}\n\t Details: {}\n".format(book[1], book[2], book[3]))
    
def show_locations(_cursor):
    """ Display locations in database """
    _cursor.execute("SELECT store_id, locale FROM store")
    locations = _cursor.fetchall()
    print("\n -- DISPLAYING STORE LOCATIONS --")
    for location in locations:
        print("\n\tLocale: {}\n".format(location[1]))

def validate_user():
    """ Validates user_id before using it """
    try:
        user_id = int(input("\n\tEnter a customer ID <Example 1 for user_id 1>: "))
        if user_id < 0 or user_id > 3:
            print("\n Invalid customer ID, program terminated...\n")
            sys.exit(0)
        return user_id
    except ValueError:
        """ Handle errors that may come up """
        print("\n Invalid number, program terminated...\n")
        sys.exit(0)
    
def show_account_menu():
    """ Display account menu """
    try:
        print("\n -- Customer Menu -- \n\t1. Wishlist\n\t2. Add Book\n\t3. Main Menu")
        account_option = int(input("\n\tSelect an account menu <Example 1 for wishlist>: "))
        return account_option
    except ValueError:
        """ Handle errors that may come up """
        print("\n Invalid number, program terminated...\n")
        sys.exit(0)
    
def show_wishlist(_cursor, _user_id):
    """ Display user wishlist """
    _cursor.execute("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_id, book.book_name, book.author FROM wishlist INNER JOIN user ON wishlist.user_id = user.user_id INNER JOIN book ON wishlist.book_id = book.book_id WHERE user.user_id = {}".format(_user_id))
    wishlist = _cursor.fetchall()
    print("\n -- DISPLAYING WISHLIST ITEMS --")
    for book in wishlist:
        print("\tBook Name: {}\n\tAuthor: {}\n".format(book[5], book[6])) # displays columns 6 & 7 which is the book name and author.
    
    
def show_books_to_add(_cursor, _user_id):
    """ Display books to add to wishlist """
    query_result = ("SELECT book_id, book_name, author, details FROM book WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id))
    print(query_result)
    _cursor.execute(query_result)
    books_to_add = _cursor.fetchall()
    print("\n -- DISPLAYING AVAILABLE BOOKS --")
    for book in books_to_add:
        print("\tBook ID: {}\n\tBook Name: {}\n".format(book[0], book[1]))
        
    
def add_book_to_wishlist(_cursor, _user_id, _book_id):
    """ Add book to user wishlist """
    _cursor.execute("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))
    
try:
    db = mysql.connector.connect(**config) # connect to database
    cursor = db.cursor()
    print("\n -- WhatABook Application --") # opening line
    user_option = show_menu()
    while user_option != 4: # ensure user selects valid menu option
        if user_option == 1:
            show_books(cursor)
        elif user_option == 2:
            show_locations(cursor)
        elif user_option == 3:
            my_user_id = validate_user()
            account_option = show_account_menu()
            while account_option != 3: # ensure user selects valid account option
                if account_option == 1:
                    show_wishlist(cursor, my_user_id)
                elif account_option == 2:
                    show_books_to_add(cursor, my_user_id)
                    book_id = int(input("\n\t Enter the book ID for the book you would like to add: "))
                    add_book_to_wishlist(cursor, my_user_id, book_id)
                    db.commit()
                    print("\n\tBook ID {} was added to your wishlist.".format(book_id))
                elif account_option < 0 or account_option > 3:
                    print("\n\tInvalid option, please retry...")
                account_option = show_account_menu()
        elif user_option < 0 or user_option > 4:
            print("\n\tInvalid option, please retry...")
        user_option = show_menu()
    print("\n\n\t Program terminated...")

except mysql.connector.Error as err:
    """ Handle any errors that may come up """
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)
        
finally:
    """ Close connection to MySQL (end of program) """
    db.close()
