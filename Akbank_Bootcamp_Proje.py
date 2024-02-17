import os
import csv


class Library:
    def __init__(self, file_location):
        self.file = open(file_location, "a+")
        self.file_name = os.path.basename(file_location)
        self.file_loc = file_location

    def list_books(self):
        self.file.seek(0)
        lines = self.file.read().splitlines()
        for i in lines:
            element = i.split(",")
            print(f"Book:{element[0]}, Author: {element[1]}")

    def add_book(self):
        title = input("Enter the book title? ")
        author = input("Enter the author? ")
        year = input("Enter the release year? ")
        page = input("Enter the number of pages ")
        self.file.seek(0)
        lines = self.file.read().splitlines()
        book_added = False

        for index, val in enumerate(lines):
            element = val.split(",")
            if element[0] == title:
                book_added = True

        if book_added == True:
            print("\nThis book has already been added in library")
        else:
            self.file.write(f"\n{title},{author},{year},{page}")
            self.file.flush()
            print(f"{title} book has added successfully")

    def remove_book(self):
        title = input("Enter the book title you want to delete ")
        self.file.seek(0)
        lines = self.file.read().splitlines()
        self.file.truncate(0)

        for index, val in enumerate(lines):
            element = val.split(",")
            if element[0].lower() == title.lower():
                lines.remove(lines[index])

        for index, val in enumerate(lines):
            if index != len(lines) - 1:
                self.file.write(f"{lines[index]}\n")
            else:
                self.file.write(f"{lines[index]}")
            self.file.flush()

    def __del__(self):
        self.file.close()


lib = Library(r"D:\Desktop\akbank\Bootcamp Proje\books.txt")
continuous = True
while continuous == True:
    user_input = input(
        "\n*** MENU ***\n1)List Books\n2)Add Book\n3)Remove Book\nq)Quit\nEnter your choice: "
    )
    if user_input == "1":
        lib.list_books()
    elif user_input == "2":
        lib.add_book()
    elif user_input == "3":
        lib.remove_book()
    elif user_input == "Q" or user_input == "q":
        continuous = False
        print("Logged out")
        break
    else:
        print("Your input is invalid!")
