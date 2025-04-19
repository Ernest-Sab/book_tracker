# Book Tracker
# This program allows you to track the books you read, including their authors, categories, and the number of pages read.
# It provides functionalities to add, remove, search for books, and update the number of pages read.

class Library():
    def __init__(self):
        self.books = []
        self.books_author = {}
        self.books_category = {}

    def add_book(self):
        print("\n|-----------------------------|")
        print("|          ADD A BOOK         |")
        print("|-----------------------------|\n")
        print("Please enter the following information:\n")
        name = str(input("Enter the name of the book: "))
        author = str(input("Enter the author of the book: "))
        pages = int(input("Enter the number of pages in the book: "))
        category = str(input("Enter the category of the book: "))

        if name in self.books:
            print(f"\nBook '{name}' already exists in the library.\n\n")

        else:
            book = Book(name, author, pages, category)
            self.books.append(book)

            if author in self.books_author:
                self.books_author[author].append(book.name)
            else:
                self.books_author[author] = [book.name]

            if category in self.books_category:
                self.books_category[category].append(book.name)
            else:
                self.books_category[category] = [book.name]
            
            print(f"\nBook '{name}' added to the library.\n")
            print(f'Your library has {len(self.books)} books.\n\n')
    
    def remove_book(self):
        print("\n|--------------------------------|")
        print("|          REMOVE A BOOK         |")
        print("|--------------------------------|\n")

        book_name = str(input("Please, enter the name of the book to remove: "))

        for book in self.books:
            if book.name == book_name:          
                self.books.remove(book)
                print(f"\nBook '{book_name}' removed from the library.\n")
                print(f'Your library has now {len(self.books)} books.\n\n')
            else:
                print(f"\nBook '{book_name}' not found in the library.\n\n")
        
    def book_info(self, book):
        print(f"Name: {book.name}")
        print(f"Author: {book.author}")
        print(f"Pages: {book.pages}")
        print(f"Category: {book.category}")
        print(f"Pages read: {book.pages_read}")
        print(f"Remaining pages: {book.remaining_pages}")
        print(f"Percentual read: {book.percentual}%\n\n")

    def search_book(self):
        print("\n|--------------------------------|")
        print("|          SEARCH A BOOK         |")
        print("|--------------------------------|\n")
        search_term = int(input("Which method do you want to search for a book? \n"
                                "1. By name \n"
                                "2. By author \n"
                                "3. By category \n\n"
                                "Choose an option: "))

        default_no = "\nOkay, no problem.\n\n"
        book_not_found = "\nBook not found in the library.\n\n"

        if search_term == 1:
            book_name = str(input("\nPlease, enter the name of the book to search: "))
            
            for book in self.books:
                if book.name == book_name:
                    print(f"\nBook '{book_name}' found in the library.")
                
                    information = str(input("\nDo you want to see the information of the book? (y/n): "))

                    if information == 'y':
                        self.book_info(book)
                        break
                    else:
                        print(default_no)
                        break
                else:
                    print(book_not_found)
            
        elif search_term == 2:
            author_name = str(input("\nPlease, enter the author of the book to search: "))

            if author_name in self.books_author:
                print(f"Books by '{author_name}': {self.books_author[author_name]}")
                
                information = str(input("\nDo you want to see the information of one of the books? (y/n): "))

                if information == 'y':
                    book_name = str(input("\nPlease, enter the name of the book to see the information: "))
                    
                    for book in self.books:
                        if book.name == book_name:
                            self.book_info(book)
                            break
                        else:
                            print(book_not_found)
                            break
                else:
                    print(default_no)
            else:
                print(f"\nNo books found by '{author_name}'.")
        
        elif search_term == 3:
            category_name = str(input("\nPlease, enter the category of the book to search: "))

            if category_name in self.books_category:
                print(f"\nBooks in '{category_name}' category: {self.books_category[category_name]}")
                
                information = str(input("\nDo you want to see the information of one of the books? (y/n): "))
                if information == 'y':
                    book_name = str(input("\nPlease, enter the name of the book to see the information: "))
                    
                    for book in self.books:
                        if book.name == book_name:
                            self.book_info(book)
                            break
                        else:
                            print(book_not_found)
                            break                           
                else:
                    print(default_no)
            else:
                print(f"\nNo books found in '{category_name}' category.")
                return False
        else:
            print("\nInvalid option. Please try again.")
            return False
        
class Book():
    def __init__(self, name, author, pages, category):
        self.name = name
        self.author = author
        self.pages = int(pages)
        self.category = category

        self.pages_read = 0
        self.remaining_pages = self.pages
        self.percentual = 0

    def update_pages_read(self):
        self.pages_read = int(input("How many pages have you read? "))

        if self.pages_read > self.pages:
            print("\nYou can't read more pages than the book has.")
            return False
        else:
            self.remaining_pages = self.pages - self.pages_read
            print(f"\nYou have {self.remaining_pages} pages left to read.")

            self.percentual_read(self.pages_read)

    def percentual_read(self, pages_read):
        self.percentual = (pages_read / self.pages) * 100
        print(f"You have read {self.percentual}% of the book.")

        if self.percentual >= 0 and self.percentual < 25:
            print("\nYou are just starting the book.\n Don't be lazy!\n")
        elif self.percentual >= 25 and self.percentual < 50:
            print("\nYou are getting into the book.\n Keep going!\n")
        elif self.percentual >= 50 and self.percentual < 75:
            print("\nYou are halfway through the book.\n")
        elif self.percentual >= 75 and self.percentual < 100:
            print("\nYou are almost done with the book.\nCome on! You can do it!\n")
        else:
            print("\nCongratulations! You have finished reading the book.")
        
        return self.percentual
    
class RunBookTracker():
    def __init__(self):
        print('''
|-----------------------------|
|       THE BOOK TRACKER      |
|         Version 1.0         |
|-----------------------------|
              ''')
        operation = int(input("\nWelcome to the Book Tracker! \n\n"
                                "This program allows you to create your personalized library.\n"
                                "You can also track the books you read, including their authors, categories, and the number of pages read.\n\n"
                                "Please, choose an operation you want to execute: \n"
                                "1. Add a book \n"
                                "2. Remove a book \n"
                                "3. Search for a book \n"
                                "4. Update pages read \n"
                                "5. List all books \n"
                                "6. Exit \n\n"
                                "Choose an option: "))
        
        library = Library()

        while operation != 6:
            if operation == 1:
                library.add_book()
            elif operation == 2:
                library.remove_book()
            elif operation == 3:
                library.search_book()
            elif operation == 4:
                print("\n|------------------------------------|")
                print("|          UPDATE PAGES READ         |")
                print("|------------------------------------|\n")
                book_name = str(input("Please, enter the name of the book to update: "))
                
                for book in library.books:
                    if book.name == book_name:
                        book.update_pages_read()
                        break
                    else:
                        print(f"Book '{book_name}' not found in the library.\n\n")
                        break
                
            elif operation == 5:
                print("\nBooks in the library:")
                for book in library.books:
                    print(f"- {book.name} by {book.author}\n\n")
            elif operation == 6:
                print("\nExiting the program. Goodbye!")
                break
            else:
                print("\nInvalid option. Please try again.")
            
            operation = int(input("\nChoose an option: \n"
                                  "1. Add a book \n"
                                "2. Remove a book \n"
                                "3. Search for a book \n"
                                "4. Update pages read \n"
                                "5. List all books \n"
                                "6. Exit \n"
                                "Choose an option: "))

RunBookTracker()