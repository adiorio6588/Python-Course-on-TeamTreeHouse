name = "adiorio6588"
print(max(name))  #max = "r"
print(min(name)) #min = 5 (numbers are lower than letter)
print(len(name)) #len = 11

docs = 'Tuples are immutable sequences, typically used to store collections of heterogeneous data (such as the 2-tuples produced by the enumerate() built-in). Tuples are also used for cases where an immutable sequence of homogeneous data is needed (such as allowing storage in a set or dict instance).'

#in loop

if 'tuples' in docs:
    # do something
    print("tuple is here!")
else:
    # do somethinf else
    print("tuple is not here")

#not in loop

if 'tuples' not in docs:
    # do something
    print("tuple not in here")
else:
    # do somethinf else
    print("tuple is here!")

print(docs.count('tuple'))

print(docs.index('tuple'))




# Code Samples: Membership Testing, Count, and Index
# List & Tuples

# Membership Testing
fruits = ['apple', 'banana', 'orange', 'pear', 'strawberry']
vegetables = ('asparagus', 'corn', 'broccoli', 'eggplant', 'onion')

'eggplant' in fruits # False
'eggplant' not in fruits # True

'eggplant' in vegetables # True
'eggplant' not in vegetables # False

# Index
my_pets = ('dog', 'cat', 'cat', 'chicken', 'dog')

my_pets.index('dog') # 0
my_pets.index('chicken') # 3
my_pets.index('lizard') # ValueError: 'lizard' is not in list

# Count
my_pets = ['dog', 'cat', 'cat', 'chicken', 'dog']

my_pets.count('cat') # 2
my_pets.count('lizard') # 0


# Range
# Membership Testing
nums = range(10)

0 in nums # True
10 in nums # False
4 in nums # True

0 not in nums # False
15 not in nums # True
10 not in nums # True

nums = range(1, 10, 2)

0 in nums # False
6 in nums # False

4 not in nums # True
8 not in nums # True

# Index
nums = range(1, 10, 2)

0 in nums # False
6 in nums # False

4 not in nums # True
8 not in nums # True