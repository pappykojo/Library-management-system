"""Library Management System
"""
import os
from pickle import load, dump
from os import system 
from os.path import exists
from sys import exit as exit_

#_______________________________________________________________________________________________________________________________________________________
def check_file_exist():
    """Checks if files exist
    """

    if not exists("users.bin"):
        with open("users.bin", 'wb') as users:
            dump({}, users)

    if not exists("books.bin"):
        with open("books.bin", 'wb') as books:
            dump({}, books)

    if not exists("borrows.bin"):
        with open("borrows.bin", 'wb') as borrows:
            dump({}, borrows)

#_______________________________________________________________________________________________________________________________________________________
def add_user():
    """Add new user with
    first name, family name, nationality code, index number and user id
    """
    print('Add New User...')

    with open('users.bin', 'rb') as users:
        users_dict = load(users)

    fname = input('First Name(s): ').strip().title()
    fam_name = input('Family Name: ').strip().upper()
    code = input('Nationality Code: ').strip().upper()
    index_num = input('Index Number: ').strip()
    user_id = len(users_dict)

    users_dict[user_id] = [
        fname,
        fam_name,
        code,
        index_num
    ]

    with open('users.bin', 'wb') as users:
        dump(users_dict, users)

    print(fam_name,fname + " has been added successfully")
    input('Enter To Go Back...')

#_______________________________________________________________________________________________________________________________________________________
def add_book():
    """Add new book with
    title, author, subject, year and book id
    """
    print('Add New Book...')

    with open('books.bin', 'rb') as books:
        book_dict = load(books)

    title = input('Title: ').strip().title()
    author = input('Author: ').strip().title()
    subject = input('Subject: ').strip().capitalize()
    year = input('Year Published: ').strip()
    book_id = len(book_dict)

    book_dict[book_id] = [
        title, 
        author,
        subject,
        year
        ]

    with open('books.bin', 'wb') as books:
        dump(book_dict, books)

    print(f"Book {book_id} added successfully")
    input('Enter To Go Back...')

#_______________________________________________________________________________________________________________________________________________________
def search_book():
    """Search the book with Book ID
    """
    print('Search Book...')

    with open('books.bin', 'rb') as books:
        book_dict = load(books)

    book_id = int(input('Book ID: '))
    book = book_dict.get(book_id, "")
    print(*book, sep=', ')
    input('Enter To Go Back...')

#_______________________________________________________________________________________________________________________________________________________
def borrow():
    """Borrow the book with book title and user id
    """
    print("Borrow Book...")

    with open('borrows.bin', 'rb') as borrows:
        borrows_dict = load(borrows)

    user_id = input('User ID: ')
    title = input('Book Title: ')
    borrows_dict[user_id] = title

    with open('borrows.bin', 'wb') as borrows:
        dump(borrows_dict, borrows)

    input('Enter To Go Back...')

#_______________________________________________________________________________________________________________________________________________________
def show_all_info():
    """Showing information of users, books and borrows
    """

    users_dict = load(open('users.bin', 'rb'))
    books_dict = load(open('books.bin', 'rb'))
    borrows_dict = load(open('borrows.bin', 'rb'))

    print("------------------------- Users Information -------------------------")
    for user in users_dict:
        data = users_dict[user]
        name, info = data[:2], data[2:]
        print(f"{' '.join(name)}: {', '.join(info)}")
    print()
    print("------------------------- Books Information -------------------------")
    for book in books_dict:
        data = books_dict[book]
        name, info = data[0], data[1:]
        print(f"{name}: {', '.join(info)}")
    print()
    print("------------------------- Borrow Information -------------------------")
    for user_id in borrows_dict:
        book_title = borrows_dict[user_id]
        print(f"User({user_id}): {book_title}")

    print()
    input('Enter To Go Back to Main Menu...')

#_______________________________________________________________________________________________________________________________________________________
def design(char,no=1):
    design=str(char)*int(no)
    print(design.center(80))

#_______________________________________________________________________________________________________________________________________________________
def clear_screen():
    """Function to clear terminal
    """
    clear = lambda: os.system('cls')
    clear()
#_______________________________________________________________________________________________________________________________________________________
def admin_tools():
    design('*',25)
    design('A D M I N I S T R A T I V E        T O O L S',1)
    design('*',25)
    print()
    print('1. Show all information\n2. Go back to main menu')
    choice = int(input('Choice: '))
    print()
    if choice == 1:
        clear_screen()
        show_all_info()
    elif choice == 2:
        clear_screen()
        Menu()
    else:
        print('Enter a valid choice')
    
    
#_______________________________________________________________________________________________________________________________________________________
def Menu():
    design('*',75)
    design("L I B R A R Y           M A N  A G E R",1)
    design('*',50)
    print()
    print()

    design('*',25)
    design("Main Menu",1)
    design('*',25)
    print('''    1-Add User
    2-Add New Book
    3-Search Book
    4-Borrow a Book
    5-Administrative Tools
    0-Exit''')

function_dict = {
    0: exit_,
    1: add_user,
    2: add_book,
    3: search_book,
    4: borrow,
    5: admin_tools
}

choice = 1
while choice != 0:
    clear_screen()
    Menu()
    choice = input("Enter Choice: ")

    while choice not in ("0", "1", "2", "3", "4", "5"):
        print('Enter a valid choice')
        choice = input("Enter Choice: ")

    clear_screen()
    check_file_exist()

    choice = int(choice)
    option = function_dict[choice]
    option()







#This project was made by the contributions of the following people
'''
OTENG Tano Kojo :   3038220
AFEAWO Sandy :  3020620
ANKOMAH Kofi Junior :  3023620
EREN-IIB Eric Kurbom :   3030720
ZABAGA Mitchell :   3042620
OBIRI YEBOAH Kwabena :  3036020
NORMENYO Cletus Anita :  3035520


'''