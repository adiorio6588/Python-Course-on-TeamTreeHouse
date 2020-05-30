Challenge Task 1 of 2

Create a new Board subclass named TicTacToe. Have it automatically be a 3x3 board by automatically setting values in the __init__.

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = []
        for y in range(self.height):
            for x in range(self.width):
                self.cells.append((x, y))

# MY CODE BELOW
class TicTacToe(Board):
    def __init__(self):
        super().__init__(width = 3,height = 3)

Challenge Task 2 of 2

Now make all Board instances iterable so we can loop through their cells attribute. If you need help, refer back to the Emulating Builtins video.

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = []
        for y in range(self.height):
            for x in range(self.width):
                self.cells.append((x, y))

# MY CODE BELOW           
    def __iter__(self):
        for cell in self.cells:
            yield cell

class TicTacToe(Board):
    def __init__(self):
        super().__init__(width = 3,height = 3)



I'd like to compare songs by their length (measured in whole seconds). Add the required methods for ==, <, >, <=, and >=

class Song:
    def __init__(self, artist, title, length):
        self.artist = artist
        self.title = title
        self.length = length

# MY CODE BELOW  

    def __int__(self):
        return int(self.length)

    def __eq__(self, other):
        return int(self) == other

    def __gt__(self, other):
        return int(self) > other

    def __lt__(self, other):
        return int(self) < other

    def __ge__(self, other):
        return int(self) >= other

    def __le__(self, other):
        return int(self) <= other


Challenge Task 1 of 2

Create a new class in dice.py named D20 that extends Die. It should automatically have 20 sides and will not need any arguments to create.

import random


class Die:
    def __init__(self, sides=2):
        if sides < 2:
            raise ValueError("Can't have fewer than two sides")
        self.sides = sides
        self.value = random.randint(1, sides)
        
    def __int__(self):
        return self.value
      
    def __add__(self, other):
        return int(self) + other
    
    def __radd__(self, other):
        return self + other
    

class D20(Die):
    def __init__(self):
        super().__init__(sides=20) 

class D20(Die): # The new class D20 and inherits its attributes from Die by placing the argument of Die in the ()s. 
    def __init__(self): # Doesn't need anything extra since it's inheriting attributes from Die class
       super().__init__(sides=20) # by using the super() method we create an instance of __init__ and override the sides of Die to be equal to 20


Challenge Task 2 of 2

In the hands.py file import the D20 class from dice.py. Create a classmethod named roll. It should take take the number of dice as an argument. Inside the roll classmethod create an empty list. Append a D20 to your list equal to the number of dice given as an argument to the roll classmethod. Then return the list of D20s. For example, if Hand.roll(2) is called, it would return a list with two D20s inside.

from dice import D20:

class Hand(list):

    def __init__(self, size=0, die_class=D20)
        self.size = size
        super().__init__()
        for _ in range(size):
            self.append(die_class())

    @classmethod
    def roll(cls, size=2):
        return cls(size)

    @property
    def total(self):
        return sum(self)