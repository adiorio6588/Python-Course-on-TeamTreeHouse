class NumString:
    def __init__(self, value):
        self.value = str(value)
        
    def __str__(self):
        return self.value
    
    def __int__(self):
        return int(self.value)
    
    def __float__(self):
        return float(self.value)
    
    def __add__(self, other):
        if '.' in self.value:
            return float(self) + other
        return int(self) + other
    
    def __radd__(self, other):
        return self + other
    
    def __iadd__(self, other):
        self.value = self + other
        return self.value

    def __mul__(self, other):
        if '.' in self.value:
            return float(self) * other
        return int(self) * other
    
    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self.value = self * other
        return self.value

#     QUIZ #1
#     Challenge Task 1 of 1

# Let's use __str__ to turn Python code into Morse code! OK, not really, but we can turn class instances into a representation of their Morse code counterparts.
# I want you to add a __str__ method to the Letter class that loops through the pattern attribute of an instance and returns "dot" for every "." (period) and "dash" for every "_" (underscore). Join them with a hyphen.
# I've included an S class as an example (I'll generate the others when I test your code) and it's __str__ output should be "dot-dot-dot".

# class Letter:
#     def __init__(self, pattern=None):
#         self.pattern = pattern
#     def __str__(self):  #MY ADDED CODE 
#         string = []
#         for letter in self.pattern:
#             if  letter == ".":
#                 string.append("dot")
#             if  letter == "_":
#                 string.append("dash")

#         return "-".join(string) 

# class S(Letter):
#     def __init__(self):
#         pattern = ['.', '.', '.']
#         super().__init__(pattern)