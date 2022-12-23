class publisher:

    def __init__(self):

        self.publish = input("Enter name of publisher : ")

    def display(self):

        print(f"Name of the publisher : {self.publish}")

class book(publisher):

    def __init__(self):

        self.title = input("Enter title of book : ")
        self.author = input("Enter name of author : ")

        super().__init__()

    def display(self):
        
        print(f"\nName of the book : {self.title}")
        print(f"Name of the author : {self.author}")

        super().display()

class python(book):

    def __init__(self):

        super().__init__()

        self.price = input("Enter price of book : ")
        self.pages = input("Enter number of pages in book : ")

    def display(self):

        super().display()

        print(f"Price of the book : {self.price}")
        print(f"Number of pages in book : {self.pages}")

obj = python()

obj.display()

    
