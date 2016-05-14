def completeOrder(userName, otherUser, tripType, destinationTypes, fareType, seatType, passengerAge):
    if tripType == "o":
        print("Fare: One way")
    else:
        print("Fare : round trip")

    if destinationType == "c":
        print("Destination: Cairns")
    elif destinationType == "s":
        print("Destination: Sydney"
        else:
        print("Destination: Perth")

        if fareType == "b":
            print("Fare : Buisness")
        elif fareType == "e"
        print("Fare: Economy")
        else:
            print("Fare: Frugal")

        if seatType == "w":
            print("Seat: Window")
        elif seatType == "a":
            print("seat: Aisle")
        else:
            print("seat: Middle")
        if passengerAge <= 2:
            print("Age discount: 100%")
        elif passengerAge > 12
        print("Age discount: 0")
        elif: passengerAge <= 12:
        print("Age discount: 50%")

        print(
            "Name:" + userName + "\n" + "Other user name:" + otherUser + "\n" + "fare:" + fareType + "\n" + "seat:" + seatType + "\n")
        print("age:")
        print(passengerAge)


def age():
    switch = False
    while switch == False:
        passengerAge = int(input("What is your age?\n"))
        if passengerAge >= 120:
            print("invalid age. please try again\n")
        elif passengerAge <= 0:
            print("Invalid age. please try again\n")
        elif passengerAge <= 12:
            print("you are eligible to recieve the child discount, you will recieve a 50% discount\n")
            switch = True
        elif passengerAge > 12:
            print("you are unable to recieve the child discount, you will have to pay the full fee\n")
            switch = True
        else:
            print("error: \nInput not recognised.\n  ")
            switch = False
    return passengerAge


def seat():
    switch = False
    while switch == False:
        seatType = input("What seat would you like to have? (W) window, (A)aisle, (M)middle\n")
        seatType = seatType.lower()
        if seatType == "w":
            print("You have selected the Window seat")
            switch = True
        elif seatType == "a":
            print("You have selected the Aisle seat")
            switch = True
        elif seatType == "m":
            print("You have selected the Middle seat")
            switch = True
        else:
            print("error: \nInput not recognised.  ")
            switch = False
    return seatType


def fare():
    switch = False
    while switch == False:
        fareType = input("What type of fare would you like?, (B)business, (E)economy, (F)frugal\n")
        fareType = fareType.lower()
        if fareType == "b":
            print("You have selected Buisness class fare")
            switch = True
        elif fareType == "e":
            print("You have selected Economy class fare")
            switch = True
        elif fareType == "f":
            print("You have selected Frugal class fare")
            switch = True
        else:
            print("error: \nInput not recognised.  ")
            switch = False
    return fareType


def destination():
    switch = False
    while switch == False:
        destinationType = input("Where is your destination?, (C)Cairns, (S)sydney or (P) perth\n")
        destinationType = destinationType.lower()
        if destinationType == "c":
            print("You have selected Cairns as your destination")
            destinationTypes = "Cairns"
        switch = True
    elif destinationType == "s":
    print("You have selected Sydney as your destination")
    switch = True

elif destinationType == "p":
print("You have selected Perth as your destination")
switch = True
else:
print("Error: \nInput not recognised.  ")
switch = False
return destinationTypes


def trip():
    switch = False
    while switch == False:
        tripType = input("Please enter if the ticket will be a (O) one way trip or (R) return trip\n")
        tripType = tripType.lower()
        if tripType == "o":
            print("You have selected one way ticket")
            switch = True
        elif tripType == "r":
            print("You have selected return trip ticket")
            switch = True
        else:
            print("Error: \nInput not recognised. ")
            switch = False
    return tripType


def otherUsers():
    otherUser = input("Please enter the persons full name (first, last)\n")
    print("Thankyou" + otherUser + ".")
    switch = True
    return otherUser


def user(Name):
    switch = False
    while switch == False:
        userName = input(
            "Is the ticket for this user or for another person?\n (Y)yes if user, (N) no if for other person\n")
        userName = userName.lower()
        if userName == "y":
            print("Thankyou " + Name + ".")
            switch = True
        elif userName == "n":
            switch = True
        else:
            print("Error: \nInput not recognised. ")
            switch = False

    return userName


def orderTicket(Name):
    userName = user(Name)
    otherUser = otherUsers()
    tripType = trip()
    destinationType = destination()
    fareType = fare()
    seatType = seat()
    passengerAge = age()
    completeOrder(userName, otherUser, tripType, destinationTypes, fareType, seatType, passengerAge)


def main():
    Name = input("Please enter your name, (first, last)")
    switch = False
    while switch == False:
        menuin = input("Welcome please choose (I)for information, (O) for order ticket or (E) for exit\n")
        menuin = menuin.lower()

        if menuin == 'i':
            print(
                "Thank you for choosing Tropical Airlines for your air travel needs.\nYou will be asked questions regarding what type of ticket you would like to purchase as well as destination information. We also offer 50% discounted fares for children.")
        elif menuin == "o":
            order = orderTicket(Name)
            switch = True

        elif menuin == "e":
            print("Goodbye, friend.")
            switch = True
        else:
            print("Error: \nInput not recognised. ")
            switch = False


main()