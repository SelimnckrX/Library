




class Library:

    def __init__(self):
        self.file_path = "books.txt"
        self.file = open(self.file_path, "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()

        if not books:
            print("No books available.")
        else:
            for book in books:
                book_info = book.split(',')
                print(f"Title: {book_info[0]}, Author: {book_info[1]}")

    def add_book(self):
        title = input("Enter book title: ")

        while True:
            author = input("Enter a valid input (only characters): ")
        
        
            if not author.isalpha():
                print("Invalid input! Please enter only characters.")
            else:
                break
         
            
        
        while True:
            try:
                date = int(input("Enter release date (must be an integer): "))
                break
            except ValueError:
                print("Release date must be an integer. Please enter a valid integer.")

        
        while True:
            try:
                num_pages = int(input("Enter number of pages (must be an integer): "))
                break
            except ValueError:
                print("Number of pages must be an integer. Please enter a valid integer.")

        book_info = f"{title},{author},{date},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        title_to_remove = input("Enter the title of the book to remove: ")
        books = self.file.readlines()
        self.file.seek(0)
        self.file.truncate()

        removed = False
        for book in books:
            if title_to_remove not in book:
                self.file.write(book)
            else:
                removed = True

        if removed:
            print("Book removed successfully.")
        else:
            print("Book not found.")

lib = Library()

while True:
    print("*** MENU***")
    print("1) List Books")
    print("2) Add Book")
    print("3) Remove Book")
    print("q) Quit")
    
    choise = input("Enter your choise: ")
    
    if choise =="1":
        lib.list_books()
    
    elif choise =="2":
        lib.add_book()
    
    elif choise == "3":
        lib.remove_book()
        
    
    elif choise == "q":
        break
    
    else:
        print("Invalid choice. Please enter 1,2,3 and q")
            
            
            
            
            
            
            
            
            
            
            
            
            
            