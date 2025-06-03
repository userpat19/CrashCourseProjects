"""You can create a Library Management System in Python that demonstrates:

✅ Duck Typing - Different book types (e.g., physical books, e-books) have a read method but are implemented differently.
✅ Instance Method - Used for managing book inventory at the object level.
✅ Static Method - Used for simple utility functions like checking ISBN validity.
✅ Class Method - Used for tracking the total number of books in the library."""


class Library():

    p_bookscount = 0
    e_bookscount = 0
    overall_bookcount = 0
    
    def __init__(self, book_name):
        self.name = book_name

    @classmethod
    def amountof_books(cls):
        return f"There are {cls.overall_bookcount} books in this Library including physical and virtual books."
    

    @staticmethod
    def isbn_validation(number_isbn):
        current = "2025"
        return f"Validity: {current in number_isbn}"
        



class Physical_Book(Library):
    
    def __init__(self, book_name):
        super().__init__(book_name)
        self.availability_state = True
        Library.p_bookscount += 1
        Library.overall_bookcount += 1  

    def read(self):
        return f"I am turning the pages of the book entitled {self.name}"
    
    def borrow_book(self):
        self.availability_state = False
        print(f"Book({self.name}): Borrowed")

    def return_book(self):
        self.availability_state = True
        print(f"Book({self.name}): Returned")

    def book_state(self):

        if self.availability_state:
            return f"The book is currently available in the library."
        
        return f"The book is not currently available in the library."
    
    @classmethod
    def physical_inventory(cls):
        return f"There is currently {cls.p_bookscount} physical books in the library."
    

class Virtual_Book(Library):
    
    def __init__(self, book_name):
        super().__init__(book_name)

        Library.e_bookscount += 1
        Library.overall_bookcount += 1   

    def read(self):
        return f"I am traversing the pages of the book {self.name} in my Computer"
    
    @classmethod
    def virtual_inventory(cls):
        return f"There is currently {cls.e_bookscount} virtual books in the library computer lab."
    

book1 = Physical_Book("Avatar The last airbender")
book2 = Virtual_Book("Solo Leveling")
book3 = Virtual_Book("Jobless Reincarnation")
book4 = Virtual_Book("Legend of korra")
book5 = Physical_Book("Avatar Lost days of appa")


print(Library.amountof_books())
print(Physical_Book.physical_inventory())
print(Virtual_Book.virtual_inventory())




