groceries = ['beef', 'cucumbers', 'lettuce', 'peanut butter', 'bread', 'dog food']

for item in groceries:
    print(item)

index = 1
for item in groceries:
    print(f'{index}. {item}')
    index+=1

# another way to write the top function

for index, item in enumerate(groceries, 1): # 1 means starting the list at one, it can be any number
    print(f'{index}. {item}')