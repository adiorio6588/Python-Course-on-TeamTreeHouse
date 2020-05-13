import random

class Character:
    def __init__(self, name, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)

class Thief(Character):
    sneaky = True

    def __init__(self, name, sneaky=True, **kwargs):
        super().__init__(name, **kwargs)
        self.sneaky = sneaky

    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))
    
    def hide(self, light_level):
        return self.sneaky and light_level < 10

# Quiz #1
# Challenge Task 1 of 3

# I've made you a super-simple Inventory class that would let someone store items in it. Not the most useful class, but we'll build something better in a few videos.
# For now, though, I need you to create a new class, SortedInventory that should be a subclass of Inventory.
# You can just put pass in the body of your class for this step.

# class Inventory:
#     def __init__(self):
#         self.slots = []

#     def add_item(self, item):
#         self.slots.append(item)
 
# class SortedInventory(Inventory):
#     pass


# Challenge Task 2 of 3

# Great! Now override the add_item method. Use super() in it to make sure the item still gets added to the list.

# class Inventory:
#     def __init__(self):
#         self.slots = []

#     def add_item(self, item):
#         self.slots.append(item)
 
# class SortedInventory(Inventory):
#     def add_item(self, item):
#         super().add_item(item)


# Challenge Task 3 of 3

# Sorted inventories should be just that: sorted. Right now, we just add an item onto the slots list whenever our add_item method is called. Use the list.sort() method to make sure the slots list gets sorted after an item is added. Only do this in the SortedInventory class.

class Inventory:
    def __init__(self):
        self.slots = []

    def add_item(self, item):
        self.slots.append(item)
 
class SortedInventory(Inventory):
    def add_item(self, item):
        super().add_item(item)
        list.sort(self.slots)



# QUIZ #2
# Alright, here's a fun task!
# Create a function named combiner that takes a single argument, which will be a list made up of strings and numbers.
# Return a single string that is a combination of all of the strings in the list and then the sum of all of the numbers. For example, with the input ["apple", 5.2, "dog", 8], combiner would return "appledog13.2". Be sure to use isinstance to solve this as I might try to trick you.

def combiner(list):
    num = 0
    str = []
    for item in list: 
        if isinstance(item, int):
           num += item
        elif isinstance(item, float):
            num += item
        else: 
            str.append(item)

    return "{}{}".format("".join(str), num)



# NOTES:
# isinstance(<object>, <class>) - This function will tell you whether or not <object> is an instance of <class>. If it could be an instance of several classes, you can use a tuple of classes like so: isinstance(<object>, (<class1>, <class2>, <class3>)).
# issubclass(<class>, <class>) - This function will tell you whether or not one class is a descendent of another class. Just like isinstance(), you can use a tuple of classes to compare against.
# type(<instance>) will give you the class for an instance, as will instance.__class__. Neither of these is particularly useful.
