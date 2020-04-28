#   TeamTreeHouse code below /////////////////////////////////////////////////////
SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remanining = 100

#   TeamTreeHouse Course Program Start
print("TeamTreeHouse Course Program Start")

#   Create the calculate_price function.  It takes number of tickets and returns
#       num_tickets * TICKET_PRICE
def calculate_price(number_of_tickets):
    #   Create a new constant for the 2 dollar service chargeN
    #   Add the service charge to our result
    return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remanining >= 1:
    print("You have {} remaining".format(tickets_remanining))
    name = input("What is your name?  ") 
    num_tickets = input("How many tickets would you like, {}?  ".format(name))
    #Except a ValueError to happen and handle it appropriately...remember to test it out!
    try:
        num_tickets = int(num_tickets)
        #   Raise a ValueError if the request is for more than are avaible  
        if num_tickets > tickets_remanining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remanining))
    except ValueError as err:
        #   Include the error text in the output
        print("Oh no, we ran into an issue.  {}. Please try again".format(err))
    else: 
        amout_due = calculate_price(num_tickets)
        print("The total due is ${}".format(amout_due))
        should_proceed = input("Do you want to proceed?  Y/N  ")
        if should_proceed.lower() == "y":
            #   TODO: Gather credit card information and process it.
            print("SOLD!")
            tickets_remanining -= num_tickets
        else:
            print("Thank you anyways {}".format(name))
print("Sorry the tickets are all sold out!!!")




#TICKET_PRICE = 10

#tickets_remanining = 100

#   TeamTreeHouse Course Program Start
#print("TeamTreeHouse Course Program Start")

#   Run this code continously until we run out of tickets
#while tickets_remanining >= 1:
    #   Output how many tickets are remaining using the ticket_remaining variable
    #print("You have {} remaining".format(tickets_remanining))

    #   Gather the user's name, and assign it to a new variable
    #name = input("What is your name?  ") 

    #   Prompt the user by name and ask how many tickets they would like
    #num_tickets = input("How many tickets would you like, {}?  ".format(name))
    #num_tickets = int(num_tickets)
    #   Calculate the price (number of tickets multiplied by the price) and assign it to a varible
    #amout_due = num_tickets * TICKET_PRICE
    #   Output the price to the screen 
    #print("The total due is ${}".format(amout_due))

    #   Prompt user if they want to proceed.  Y/N?
    #should_proceed = input("Do you want to proceed?  Y/N  ")
    #   If they want to proceed
    #if should_proceed.lower() == "y":
        #   print out to the screen "SOLD!" to confirm purchase
        #   TODO: Gather credit card information and process it.
        #print("SOLD!")
        #   and then drecement the ticket remaining by the number of tickets purchased
        #tickets_remanining -= num_tickets
    #Otherwise....
    #else:
        # Thank them by name
        #print("Thank you anyways {}".format(name))

#   Notify user that the tickets are sold out
#print("Sorry the tickets are all sold out!!!")






#   My code below ////////////////////////////////////////////////////////////////

ATICKET_PRICE = 10

atickets_remanining = 100

#   My Program Start
print("My Program Start")

#   Run this code continously until we run out of tickets
while atickets_remanining >= 0:
    #   Output how many tickets are remaining using the ticket_remaining variable
    print("(AD)There are {} remaining.".format(atickets_remanining))
    #   //////Wrong Code Below////////
    # atickets_sold = int(input("How many tickets do you want? "))
    # atickets_leftover = atickets_remanining - atickets_sold
    # print(atickets_leftover)

    #   Gather the user's name, and assign it to a new variable 
    user_name = input("(AD)What is your name?  ")

    #   Prompt the user by name and ask how many tickets they would like
    number_of_tickets_requested = int(input("{} how many tickets would you like?  ".format(user_name)))

    #   Calculate the price (number of tickets multiplied by the price) and assign it to a varible
    ticket_price_total = number_of_tickets_requested * ATICKET_PRICE

    #   Output the price to the screen 
    print("Your total will be ${}.".format(ticket_price_total))

    #   Prompt user if they want to proceed.  Y/N?

    confirmation = input("{} would you like to proceed with the purchase Y/N?  ".format(user_name))
    #   If they want to proceed
    if confirmation.lower() == "y":
    #   print out to the screen "SOLD!" to confirm purchase
        print("SOLD!")
        #   //////Wrong Code Below////////
        #   unsold_tickets = atickets_remanining - number_of_tickets_requested
        #   and then drecement the ticket remaining by the number of tickets purchased
        atickets_remanining -= number_of_tickets_requested

        print("There are {} remaining.".format(atickets_remanining))  
        #   Otherwise....
    else:
    # Thank them by name
        print("Thank you anyways {}.".format(user_name))

        #   Notify user that the tickets are sold out
else: 
    print("Sorry, the tickets are sold out.")