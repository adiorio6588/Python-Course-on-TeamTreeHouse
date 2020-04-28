import math



# def monday_algor(crates_backstock, amount_sold):
#     return crates_backstock - amount_sold

# crates_backstock = int(input("How many crates?"))
# amount_sold = int(input("How much sold"))

# results = monday_algor(crates_backstock, amount_sold)

# print(results)






def split_check(total, number_of_people):
    if number_of_people <= 1:
        raise ValueError("More than 1 person is required to split the check")
    return math.ceil(total / number_of_people)

try:
    total_due = float(input("What is the check total? "))
    number_of_people = int(input("How many people? "))
    amount_due = split_check(total_due, number_of_people)
except ValueError as err:
    print("Please enter a number value")
    print("({})".format(err))
else: 
    print("Each person owes ${}".format(amount_due))



# def bar_tab(bar_check, people_pay42ing):
#     return bar_check / people_paying












# def bar_tab(tab_cost, people):
#     price_per_person = math.ceil(tab_cost / people)
#     return price_per_person

# patrons = bar_tab(42.10, 2)

# print("Each person owe bar {}".format(patrons))

# def ipay(check, people):
#      cost_per_person =  math.ceil(total / number_of_people)
#      print(cost_per_person)
    
# ipay(42.08, 5)