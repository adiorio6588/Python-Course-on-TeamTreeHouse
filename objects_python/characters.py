import random

class Wizard:
    magic = True

    def __init__(self, name, magic=True, **kwargs):
        self.name = name
        self.magic = magic

        for key, value in kwargs.items():
            setattr(self, key, value)

    def fortune_telling(self):
        return self.magic and  bool(random.randint(0, 1))
        
    def enemy(self, demon_count):
        return self.magic and demon_count < 10



# class Wizard:
#     magic = True

#     def __init__(self, name, sneaky=True, **kwargs):
#         self.name = name
#         self.magic = magic

#     def fortune_telling(self):
#         if self.magic:
#             return bool (random.randint(0, 1))
#         return False

#     def enemy(self, demon_count):
#         return self.magic and demon_count < 10


# class Wizard:
#     magic = True

#     def fortune_telling(self):
#         print("Called by {}".format(self))
#         return bool (random.randint(0, 1))


# class WizardTwo:
#     magic_two = True

#     def fortune_telling_two(self):
#         if self.magic_two:
#             return bool (random.randint(0, 1))
#         return False





# QUIZ 1
# Now, make an instance of your class named me.
# Then print() out the name attribute of your instance.

# class Student:
#     name = 'Anthony'

# me = Student()
# print(me.name)



# Quiz 2
# Challenge Task 1 of 1

# This class should look familiar!
# I need you to add a method name praise. The method should return a positive message about the student which includes the name attribute. As an example, it could say "You're doing a great job, Jacinta!" or "I really like your hair today, Michael!".
# Feel free to change the name attribute to your own name, too!
# class Student:
#     name = "Anthony"

#     def praise(self):
#         return("You're doing a great job {}".format(self.name))



# Quiz 3
# Alright, I need you make a new method named feedback. It should take an argument named grade. Methods take arguments just like functions do. You'll still need self in there, though.
# If grade is above 50, return the result of the praise method. If it's 50 or below, return the reassurance method's result.

# class Student:
#     name = "Karen"
    
       
#     def praise(self):
#         return "You inspire me, {}".format(self.name)
    
#     def reassurance(self):
#         return "Chin up, {}. You'll get it next time!".format(self.name)

#     def feedback(self, grade):
#         if grade > 50:
#             return self.praise()
#         return self.reassurance()



# Quiz 4
# Challenge Task 1 of 2

# Our Student class is coming along nicely!
# I'd like to be able to set the name attribute at the same time that I create an instance. Can you add the code for doing that? Remember, you'll need to override the __init__ method.

# Challenge Task 2 of 2

# Great!
# Sometimes I have other attributes I need to store on a Student instance, though. Can you use **kwargs and setattr to add attributes for any other key/value pairs I want to send to the instance when I create it?

# class Student:
#     name = "Your Name"
    
#     def __init__(self, name= "Your Name", **kwarg):
#         self.name = name

#     for key, value in kwarg.items():
#         setattr(self, key, value)
    
#     def praise(self):
#         return "You inspire me, {}".format(self.name)
    
#     def reassurance(self):
#         return "Chin up, {}. You'll get it next time!".format(self.name)
    
#     def feedback(self, grade):
#         if grade > 50:
#             return self.praise()
#         return self.reassurance()


#Quiz 5
# Challenge Task 1 of 3

# OK, let's combine everything we've done so far into one challenge!
# First, create a class named RaceCar. In the __init__ for the class, take arguments for color and fuel_remaining. Be sure to set these as attributes on the instance.
# Also, use setattr to take any other keyword arguments that come in.

# class RaceCar:
    
#     def __init__(self, color, fuel_remaining, **kwargs):
#         self.color = color
#         self.fuel_remaining = fuel_remaining
        
#         for key, value in kwargs.items():
#             setattr(self, key, value)

# Challenge Task 2 of 3

# Vrroom!
# OK, now let's add a method named run_lap. It'll take a length argument. It should reduce the fuel_remaining attribute by length multiplied by 0.125.
# Oh, and add a laps attribute to the class, set to 0, and increment it each time the run_lap method is called.

# class RaceCar:
#     def __init__(self, color, fuel_remaining, **kwargs):
#         self.color = color
#         self.fuel_remaining = fuel_remaining
#         self.laps = 0

#         for key, value in kwargs.items():
#                setattr(self, key, value)  

#     def run_lap(self, length):
#         self.fuel_remaining -= length * 0.125
#         self.laps = self.laps + 1

# Challenge Task 3 of 3

# Great! One last thing.
# In Python, attributes defined on the class, but not an instance, are universal. So if you change the value of the attribute, any instance that doesn't have it set explicitly will have its value changed, too!
# For example, right now, if we made a RaceCar instance named red_car, then did RaceCar.laps = 10, red_car.laps would be 10!
# To prevent this, be sure to set the laps attribute inside of your __init__ method (it doesn't have to be a keyword argument, though). If you already did it, just hit that "run" button and you're good to go!

class RaceCar:
    def __init__(self, color, fuel_remaining, **kwargs):
        self.color = color
        self.fuel_remaining = fuel_remaining
        self.laps = 0

        for key, value in kwargs.items():
               setattr(self, key, value)  

    def run_lap(self, length):
        self.fuel_remaining -= length * 0.125
        self.laps = self.laps + 1