def greeting():
    # appears on startup, asks for users name. Response saved as userName.
    print("Please enter your name:")
    userName = input()
    print("Hello " + userName + " Welcome to the Tropical Airlines .")
    return userName


def getName(userName):
    # asks user if ticket for them or other. If other asks for that persons name. Includes userproofing.
    switch = False
    while switch == False:
        print("Is the ticket for (Y)ou or (S)omeone else?")
        ticketFor = input()
        ticketFor = ticketFor.lower()
        if  ticketFor == "y":
            passengerName = userName
            switch = True
        elif ticketFor == "s":
            print("Please enter the name of the person traveling")
            passengerName = input()
            if passengerName == " " or passengerName == "":
                print("ERROR: Please input a name")
            else:
                switch = True
        else:
                print("ERROR: Input not recognised. Please input either (Y) for the ticket to be for yourself, or (S) for the ticket to be for someone else.")
    return passengerName


def getAge():
    # asks user for the passenger's age. Ensures age is within reasonable range.
    switch = False
    while switch == False:
        print("Please enter the passenger's age:")
        inputAge = input()
        while not int(inputAge):
            inputAge = input()

        passengerAge = int(inputAge)

        if passengerAge >= 0 and passengerAge <= 130:
            switch = True
        else:
            print("Please ensure you entered the correct age of the passenger")
    return passengerAge

def getTripCode():
    switchCode = False
    while switchCode == False:
        print("Please choose a destination and trip length. Fare choices are displayed below: (C1) Cairns One Way - $250. (C2) Cairns Return - $400, (S1) Sydney One Way - $420, (S2) Sydney Return - $575, (P1) Perth One Way - $510, (P2) Perth Return - $700")
        tripCode = input()
        tripCode = tripCode.lower()
        if tripCode == "c1" or tripCode == "c2" or tripCode == "s1" or tripCode == "s2" or tripCode == "p1" or tripCode == "p2":
            switchCode = True
        else:
            print("ERROR: Input not recognised. Please input the correct code which is indicated in brackets. The first letter is for the destination. 1 means one way, 2 means return trip.")
    return tripCode

def getClassCode():
    switchCode = False
    while switchCode == False:
        print("Please choose the type of fare. Fees are displayed below and are in addition to the basic fare; (B)usiness - $275, (E)conomy - $25, (F)rugal - $0")
        print("Please note choosing Frugal fare means you will not be offered a seat choice, it will be assigned to the ticketholder at travel time.")
        classCode = input()
        classCode = classCode.lower()
        if classCode.lower() == "b" or classCode.lower() == "e" or classCode.lower() == "f":
            switchCode = True
        else:
            print("ERROR: Input not recognised. Please enter the letter in brackets to complete the intended action.")
    return classCode

def getTypeCode():
    switchCode = False
    while switchCode == False:
        print("Please choose the seat type. Choosing the middle seat will deduct 25 from the total fare. (W)indow + $75, (A)isle + $50, (M)iddle - $25")
        typeCode = input()
        typeCode = typeCode.lower()
        if typeCode == "w" or typeCode == "a" or typeCode == "m":
            switchCode = True
        else:
            print("ERROR: Input not recognised. Please enter the letter in brackets to complete the intended action.")
    return typeCode

def checkAssign(passengerName, passengerAge, tripCode, classCode, typeCode):
    if tripCode == "c1":
        tripDestination = "Cairns One Way"
    elif tripCode == "c2":
        tripDestination = "Cairns Return"
    elif tripCode == "s1":
        tripDestination = "Sydney One Way"
    elif tripCode == "s2":
        tripDestination = "Sydney Return"
    elif tripCode == "p1":
        tripDestination = "Perth One Way"
    else:
        tripDestination = "Perth Return"

    if classCode == "b":
        seatClassWord = "Business"
    elif classCode == "e":
        seatClassWord = "Economy"
    else:
        seatClassWord = "Frugal"

    if typeCode == "w":
        seatTypeWord = "Window"
    elif typeCode == "a":
        seatTypeWord = "Aisle"
    else:
        seatTypeWord = "Middle"

    check = " Ticket for: " + passengerName + ", Passenger age: " + str(passengerAge) + ", Trip destination: " + tripDestination + ", Seat class: " + seatClassWord + ", Seat type: " + seatTypeWord
    return check

def formatCurrency(cost):
    cost = "${:,.2f}".format(cost)
    return cost

def costCalculation(tripCode, typeCode, classCode, passengerAge):
    if tripCode == "c1":
        tripValue = 250
    elif tripCode == "c2":
        tripValue = 400
    elif tripCode == "s1":
        tripValue = 420
    elif tripCode == "s2":
        tripValue = 575
    elif tripCode == "p1":
        tripValue = 510
    else:
        tripValue = 700

    if classCode == "b":
        classValue = 275
    elif classCode == "e":
        classValue = 25
    else:
        classValue = 0

    if typeCode == "w":
        typeValue = 75
    elif typeCode == "a":
        typeValue = 50
    else:
        typeValue = -25

    if passengerAge <= 2:
        ageDiscount = 0
    elif passengerAge <= 12 and passengerAge >= 3:
        ageDiscount = 0.5
    else:
        ageDiscount = 1

    cost = (tripValue + classValue + typeValue) * ageDiscount
    cost = formatCurrency(cost)
    return cost



def acceptPurchase():
    acceptSwitch = False
    while acceptSwitch == False:
        print("Would you like to purchase this ticket: (Y)es or (N)o ")
        acceptPurchase = input()
        acceptPurchase = acceptPurchase.lower()
        if acceptPurchase == "y":
            print("Your ticket has been purchased. Thank you for flying with Tropical Airlines. You have been returned to the main menu.")
            acceptSwitch = True
        elif acceptPurchase == "n":
            print("Your ticket has not been purchased. You have been returned to the main menu.")
            acceptSwitch = True
        else:
            print("ERROR: Input not recognised. Please enter Y for yes or N for No.")
    return acceptPurchase


def orderTicket(userName):
    passengerName = getName(userName)
    passengerAge = getAge()
    tripCode = getTripCode()
    classCode = getClassCode()
    if classCode == "b" or classCode == "e":
        typeCode = getTypeCode()
    else:
        typeCode = "m"

    acceptPurchase = False
    while acceptPurchase == False:
        check = checkAssign(passengerName, passengerAge, tripCode, classCode, typeCode)
        cost = costCalculation(tripCode, typeCode, classCode, passengerAge)
        print("Is the following information correct: " + check + " Your ticket will cost: " + str(cost))
        print("Is this information correct? (Y)es or (N)o?")
        correct = input()
        correct = correct.lower()
        if correct == "y":
            switch = True
        elif correct == "n":
            repeatChangeSwitch = False
            while repeatChangeSwitch == False:
                print("What would you like to change? " + "(N)ame, " + "(A)ge,  " + "(D)estination, " + "Seat (C)lass, " + "Seat (T)ype")
                change = input()
                change = change.lower()
                if change == "n":
                    passengerName = getName(userName)
                    print("The passenger's name on the ticket has been changed")

                elif change == "a":
                    passengerAge = getAge()
                    print("The passenger's age on the ticket has been changed.")

                elif change == "d":
                    tripCode = getTripCode()
                    print("The flight has been changed.")

                elif change == "c":
                    classCode = getClassCode()
                    print("The class has been changed.")

                elif change == "t":
                    if classCode == "f":
                        print("Due to your class choice you cannot change your seat. Please change your class to be able to change your seat")
                        print("Would you like to change your class?")
                        correct = input()
                        correct = correct.lower()
                        if correct == "y":
                            classCode = getClassCode()
                            print("The class has been changed.")
                    else:
                        typeCode = getTypeCode()
                        print("The seat position has been changed.")

                else:
                    print("ERROR: No change was made. Please enter the designated letter for the option you would like to change.")

                print("Would you like to make another change? (Y)es or (N)o?")

                repeatCheck = input()
                repeatCheck.lower()
                if repeatCheck == "y":
                    repeatChangeSwitch = False
                elif repeatCheck == "n":
                    repeatChangeSwitch = True
                else:
                    print("Error. Please enter Y for yes OR N for no.")
        else:
            print("ERROR: Input not recognised. Please enter Y for yes or N for no.")
        print("Your ticket has been purchased. ")
        print("The ticket is as follows: " + check + " Your ticket will cost: " + str(cost) + " ")
        acceptPurchase = True
    return cost




def main():
    userName = greeting()
    exitProgram = False
    ticketCost =  []

    while not exitProgram:
        print("Tropic Airlines Ticket Ordering System: (I)nstructions, (O)rder ticket or (E)xit");
        userInput = input()
        userInput = userInput.lower()
        if userInput == "o":
            ticketCost.append(orderTicket(userName))

        elif userInput == "e":
            ticketCost.sort()
            print(userName + " your orders are: ")
            x = len(ticketCost)
            i = 0
            for price in ticketCost:
                i = i + 1
                print("Ticket " + str(i)+ " " + price)

            print("Thank you for choosing Tropical Airlines for your air travel needs.")
            quitProgram = True
        elif userInput == "i":
            print("Thank you for choosing Tropical Airlines for your air travel needs. You will be asked questions regarding what type of ticket you would like to pruchase as well as destination information. We also offer 50% discounted fares for children under the age of 12. Children under the age of 2 are free.")
            print("You have been returned to the main menu.")
        else:
            print("ERROR: Input not recognised. Please enter the letter in brackets to complete the intended action.")

main()
