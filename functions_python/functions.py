def two_plus_two():
    sum = 2 + 2
    return (sum)

print(two_plus_two() * 2)

def add_two(num):
    val = 2 + num
    return(val)

print(add_two(5))


def calculate_total(*args):
    total = sum(args)
    print(total)

calculate_total(25, 25, 20, 30)

def unpacker():
    return(1,2,3)

var1, var2, var3 = unpacker()
print(var1)
print(var2)
print(var3)

first, last = input("What is your full name?:\n").split(' ')

print(first)
print(last)