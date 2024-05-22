# Library Management System

## Introduction
This README file provides an overview and detailed explanation of the core functions in the Library Management System project. This guide is intended to clarify components of the code, making it easier for anyone to understand the project and use its functions effectively.

## Project Overview
The Library Management System is designed to manage users, books, and borrowing records. The system includes functionality for adding new users and books, searching for books, borrowing books, and displaying all stored information.

## Functions

### 1. `check_file_exist()`
This function checks for the existence of necessary files (`users.bin`, `books.bin`, and `borrows.bin`) and creates them if they are missing.

### 2. `add_user()`
This function adds a new user to the system, collecting their first name, family name, nationality code, and index number.

### 3. `add_book()`
This function adds a new book to the system, collecting its title, author, subject, and year of publication.

### 4. `search_book()`
This function searches for a book by its ID.

### 5. `borrow()`
This function records the borrowing of a book by a user.

### 6. `show_all_info()`
This function displays all the information stored in the system, including users, books, and borrowing records.

## Administrative Functions

### 7. `design()`
This function prints a design line with a specified character and length.

### 8. `clear_screen()`
This function clears the terminal screen.

### 9. `admin_tools()`
This function provides administrative tools to show all information or return to the main menu.

## Main Menu
The `Menu()` function displays the main menu and allows users to choose different operations.

## Contributors
This project was made by the contributions of the following people:
- OTENG Tano Kojo : 3038220
- AFEAWO Sandy : 3020620
- ANKOMAH Kofi Junior : 3023620
- EREN-IIB Eric Kurbom : 3030720
- ZABAGA Mitchell : 3042620
- OBIRI YEBOAH Kwabena : 3036020
- NORMENYO Cletus Anita : 3035520
