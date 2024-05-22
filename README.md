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
# How to Use the Repository

## Prerequisites
Before using this Library Management System, ensure you have the following installed on your system:
- Python 3.x
- Git

## Clone the Repository
First, clone the repository to your local machine using the following command:

```bash
git clone <repository_url>
```

Replace `<repository_url>` with the actual URL of the repository.

## Navigate to the Project Directory
Change your current directory to the project directory:

```bash
cd <project_directory>
```

Replace `<project_directory>` with the name of the directory where the repository was cloned.

## Run the Program
To start the Library Management System, execute the following command in your terminal:

```bash
python library_management_system.py
```

This will launch the program and display the main menu.

## Main Menu
The main menu provides several options for interacting with the system:

1. **Add User**: Allows you to add a new user to the system.
2. **Add New Book**: Allows you to add a new book to the system.
3. **Search Book**: Allows you to search for a book by its ID.
4. **Borrow a Book**: Allows a user to borrow a book by providing their user ID and the book title.
5. **Administrative Tools**: Provides additional tools for administrators, such as displaying all information stored in the system.
6. **Exit**: Exits the program.

Use the corresponding number to select an option from the menu.

## Detailed Functionality

### 1. Add User
To add a new user, select option `1` from the main menu. You will be prompted to enter the following details:
- First Name(s)
- Family Name
- Nationality Code
- Index Number

The system will then generate a user ID and save the new user’s information.

### 2. Add New Book
To add a new book, select option `2` from the main menu. You will be prompted to enter the following details:
- Title
- Author
- Subject
- Year Published

The system will generate a book ID and save the new book’s information.

### 3. Search Book
To search for a book, select option `3` from the main menu. You will be prompted to enter the book ID. The system will then display the book’s details.

### 4. Borrow a Book
To borrow a book, select option `4` from the main menu. You will be prompted to enter the user ID and the book title. The system will record the borrowing information.

### 5. Administrative Tools
To access administrative tools, select option `5` from the main menu. You will have the following choices:
- Show all information: Displays all user, book, and borrowing information.
- Go back to main menu: Returns to the main menu.

### 6. Exit
To exit the program, select option `0` from the main menu.

## Contributors
This project was made by the contributions of the following people:
- OTENG Tano Kojo : 3038220
- AFEAWO Sandy : 3020620
- ANKOMAH Kofi Junior : 3023620
- EREN-IIB Eric Kurbom : 3030720
- ZABAGA Mitchell : 3042620
- OBIRI YEBOAH Kwabena : 3036020
- NORMENYO Cletus Anita : 3035520
