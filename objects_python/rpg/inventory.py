class Inventory:
    def __init__(self):
        self.slots = []
        
    def add(self, item):
        self.slots.append(item)
        
    def __len__(self):
        return len(self.slots)
    
    def __contains__(self, item):
        return item in self.slots
    
    def __iter__(self):
        yield from self.slots

# QUIZ
# Let's make our Letter class better for our Morse code challenge. Add an __iter__ method to the Letter class so the letter's pattern can be iterated through. You'll want to use yield or yield from.
# Do not convert the pattern to dots and dashes in __iter__.

# class Letter:
#     def __init__(self, pattern=None):
#         self.pattern = pattern

#     def __str__(self):
#         output = []
#         for blip in self.pattern:
#             if blip == '.':
#                 output.append('dot')
#             else:
#                 output.append('dash')
#         return '-'.join(output)

#     def __iter__(self):
#         yield from self.pattern



# class S(Letter):
#     def __init__(self):
#          pattern = ['.', '.', '.']
#         super().__init__(pattern)
