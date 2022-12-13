class book:

    borrowed_books = {}
    reserved_books = {}

    def __init__(self,id,book_name):
        self.book_name = book_name
        self.id = id

    def borrow_book(self):
        book.borrowed_books[self.id] = self.book_name

    def reserve_book(self):
        book.reserved_books[self.id] = self.book_name

    def return_book(self):
        del book.borrowed_books[self.id]

    def show_2(self):
        print(book.borrowed_books)
        print(book.reserved_books)

class shelf:

    _shelf = {}

    def __init__(self,id,book_name):
        self.id = id
        self.book_name = book_name

    def populate_book(self):
        shelf._shelf[self.id] = self.book_name

    def remove_book(self):
        del shelf._shelf[self.id]

    def change_book_name(self,book_name):
        shelf._shelf[self.id] = book_name

    def show_3(self):
        print(shelf._shelf)

id = input("please enter your id: ")
name = input("please enter your name: ")
dt = input("please enter whether you are an admin or a user: ")

if dt == "admin" :
    
    print()
    print("hey you can populate, remove or change the details of any book on the shelf")
    print()

    while 1==1:
        yn = input("if you want to make any changes to the shelf type 'yes' if not enter any other key: ")

        if yn == "yes":
            ch = int(input("enter 1 to populate book, 2 to remove an existing book or 3 to change a book's details: "))

            if ch == 1:
                print()
                s1=input("enter the id of the book: ")
                s2=input("enter the name of the book: ")
                s = shelf(s1,s2).populate_book()

            elif ch == 2:
                print()
                s1=input("enter the id of the book: ")
                s2=input("enter the name of the book: ")
                s = shelf(s1,s2).remove_book()

            elif ch == 3:
                print()
                s1=input("enter the id of the book: ")
                s2=input("enter the name of the book: ")
                s = shelf(s1,s2).change_book_name(s2)

        else:
            break

    print()
    print("the shelf looks like -->")
    print(shelf._shelf)

if dt == "user" :
    
    print()
    print("hey you can borrow, return or reserve any book")

    while 1==1:
        print()
        yn = input("if you want to make any changes type 'yes' if not enter any other key: ")
        print()

        if yn == "yes":
            ch = int(input("enter 1 to borrow book, 2 to return a borrowed book or 3 to reserve a book: "))

            if ch == 1:
                print()
                s1=input("enter the id of the book: ")
                s2=input("enter the name of the book: ")
                s = book(s1,s2).borrow_book()

            elif ch == 2:
                print()
                s1=input("enter the id of the book: ")
                s2=input("enter the name of the book: ")
                s = book(s1,s2).return_book()

            elif ch == 3:
                print()
                s1=input("enter the id of the book: ")
                s2=input("enter the name of the book: ")
                s = book(s1,s2).reserve_book()

        else:
            break

    print()
    print("the borrowed books are -->")
    print(book.borrowed_books)

    print()
    print("the reserved books are -->")
    print(book.reserved_books)
        









    
        
