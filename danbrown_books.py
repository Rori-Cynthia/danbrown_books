class Book:
    pass
        


book1 = Book()
book2 = Book()
book1.author = "Dan Brown"
book1.title = "Inferno"
book2.author = "Dan Brown"
book2.title = "The Da Vinci Code"
book2.year_of_publishment = 2003
print(book1.__dict__)
print(book2.__dict__)