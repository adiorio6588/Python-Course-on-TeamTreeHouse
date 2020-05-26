class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return '{} by {}'.format(self.title, self.author)


class Bookcase:
    def __init__(self, books=None):
        self.books = books
        
    @classmethod
    def create_bookcase(cls, book_list):
        books = []
        for title, author in book_list:
            books.append(Book(title, author))
        return cls(books)



# OUIZ
# Let's practice using @classmethod!
# Create a class method in Letter named from_string that takes a string like "dash-dot" and creates an instance with the correct pattern (['_', '.']).

# class Letter:
#     def __init__(self, pattern=None):
#         self.pattern = pattern
      
#     def __iter__(self):
#         yield from self.pattern
      
#     def __str__(self):
#         output = []
#         for blip in self:
#             if blip == '.':
#                 output.append('dot')
#             else:
#                 output.append('dash')
#         return '-'.join(output)
    
    
#     @classmethod
#     def from_string(cls, my_string):
#         my_list = my_string.split("-")
#         output = []
#         for element in my_list:
#             if element == "dash":
#                 output.append("_")
#             else:
#                 output.append(".")
#         return cls(output)
    

# class S(Letter):
#     def __init__(self):
#          pattern = ['.', '.', '.']
#          super().__init__(pattern)