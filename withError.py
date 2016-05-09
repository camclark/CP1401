def greeting():
    # appears on startup, asks for users name. Response saved as userName.
    print("Please enter your name:")
    userName = input()
    print("Welcome " + userName)
    return userName

def checkHandle(prompt,codeArray,wordArray):
    switch = False
    wrongCheck = True
    while switch == False:
                #get input
                print(prompt)
                instanceInput = input()
                instanceInput = instanceInput.lower()
                x = 0
                for Number in codeArray:
                    if Number == instanceInput:
                        switch = True
                        instanceInput = wordArray[x]
                        wrongCheck = False
                    x = x + 1
                        # Error message - none of the array match input
                if wrongCheck == True:
                    print("Error input not recognised. \nPlease select what you would like by entering the corosponding letter in brackets \n")
    return instanceInput

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
        print("How old is the person travelling? Travellers under 16 years old will receive a 50% discount for the child fare.")
        inputAge = input()

        if not inputAge.isdigit():
            print("Error: Please input numbers")
            continue
        else:
            inputAge = int(inputAge)

        if inputAge >= 0 and inputAge <= 130:
            switch = True
        else:
            print("Please ensure you entered the correct age of the passenger")
    return inputAge




def costCalculation(tripDestination, flightType, seatType, seatClass, passengerAge):
    # Calculates cost of trip from expected values
    if tripDestination == "Cairns" and flightType == "one-way":
        tripValue = 250
    elif tripDestination == "Cairns" and flightType == "return":
        tripValue = 400
    elif tripDestination == "Sydney" and flightType == "one-way":
        tripValue = 420
    elif tripDestination == "Sydney" and flightType == "return":
        tripValue = 575
    elif tripDestination == "Perth" and flightType == "one-way":
        tripValue = 510
    else:
        tripValue = 700

    if seatClass == "business":
        classValue = 275
    elif seatClass == "economy":
        classValue = 25
    else:
        classValue = 0

    if seatType == "window":
        typeValue = 75
    elif seatType == "aisle":
        typeValue = 50
    else:
        typeValue = -25

    if passengerAge <= 2:
        ageDiscount = 0
        ageDiscountEligibility = "(Eligiable for infant ticket - free)"
    elif passengerAge <= 16 and passengerAge >= 3:
        ageDiscount = 0.5
        ageDiscountEligibility = "(Eligiable for child ticket - half price)"
    else:
        ageDiscount = 1
        ageDiscountEligibility = "(Not eligiable for child ticket)"

    cost = (tripValue + classValue + typeValue) * ageDiscount

    #format "$#.## - for display later"
    tripValue = "${:,.2f}".format(tripValue)
    classValue = "${:,.2f}".format(classValue)
    typeValue = "${:,.2f}".format(typeValue)

    return tripValue, classValue, typeValue, ageDiscountEligibility, cost



def acceptPurchase(cost):
    # presents user with a y/n to purchase ticket.
    # should make it to return cost 0 if not accepted
    acceptSwitch = False
    while acceptSwitch == False:
        print("Would you like to purchase this ticket: (Y)es or (N)o ")
        acceptPurchase = input()
        acceptPurchase = acceptPurchase.lower()
        if acceptPurchase == "y":
            print("Your ticket has been purchased. Thank you for flying with Tropical Airlines. You have been returned to the main menu.")
            acceptSwitch = True
        elif acceptPurchase == "n":
            cost = "CANCELLED ORDER"
            print("Your ticket has not been purchased. You have been returned to the main menu.")
            acceptSwitch = True
        else:
            print("ERROR: Input not recognised. Please enter Y for yes or N for No.")
    return cost





def orderTicket(userName):
    passengerName = getName(userName)

    passengerAge = getAge()

    codeArray = ["c", "s", "p"]
    wordArray = ["Cairns","Sydney","Perth"]
    prompt = "Please select the destination for your return trip. Base fare prices are listed below: \n(C)airns – $400 \n(S)ydney – $575 \n(P)erth - $700"
    tripDestination= checkHandle(prompt,codeArray,wordArray)


    codeArray = ["o", "r"]
    wordArray = ["one-way","return"]
    prompt = "Is this a: \n(R)eturn trip  \n(O)ne-Way"
    flightType = checkHandle(prompt,codeArray,wordArray)


    codeArray = ["b", "e","f"]
    wordArray = ["business", "economy", "frugal"]
    prompt = "Please choose the type of fare. Fees are displayed below and are in addition to the basic fare. \nPlease note choosing Frugal fare means you will not be offered a seat choice. \n(B)usiness - $275 \n(E)conomy - $25 \n(F)rugal - $0"
    seatType = checkHandle(prompt, codeArray, wordArray)

    if seatType == "frugal":
        seatClass = "middle"
    else:
        codeArray = ["w", "a","m"]
        wordArray = ["window", "aisle", "middle"]
        prompt = "Please choose the seat type.  Choosing the middle seat will deduct 25 from the total fare. \n(W)indow  $75 \n(A)isle  $50 \n(M)iddle -$25"

        seatClass = checkHandle(prompt, codeArray, wordArray)

    tripValue, classValue, typeValue, ageDiscountEligibility, cost = costCalculation(tripDestination,flightType,seatType,seatClass,passengerAge)
    costDisplay = "${:,.2f}".format(cost)

    print(" Ticket for: " + passengerName + "\nPassenger age: " + str(passengerAge) + "\t" + ageDiscountEligibility + "\nTrip destination: " + tripDestination + "(" + flightType + ")\t" + tripValue  + "\nSeat class: " + seatClass + "\t\t\t\t\t" + classValue + "\nSeat type: " + seatType + "\t\t\t\t\t" + typeValue + "\nTotal cost: " + costDisplay)
    cost = acceptPurchase(cost)
    return cost



def main():
    userName = greeting()
    exitProgram = False
    ticketCost = []

    while not exitProgram:
        print("Tropic Airlines Ticket Ordering System: \n (I)nstructions \n (O)rder ticket \n (E)xit ")

        userInput = input()
        userInput = userInput.lower()
        if userInput == "o":
            ticketInformation = orderTicket(userName)
            if ticketInformation == "CANCELLED ORDER":
                print("The ticket was not processed.")
            else:
                ticketCost.append(ticketInformation)

        elif userInput == "e":
            # exits program
            ticketCost.sort()

            #detemine how long the array is, depending on length different actions
            ticketCostLength = len(ticketCost)
            i = 0
            if ticketCostLength ==1:
                ticketCost[0] = "${:,.2f}".format(ticketCost[0])
                print(userName + ", your order is: " + ticketCost[0] + " Your final total is: " + ticketCost[0])
            elif ticketCostLength > 1:
                print(userName + " your orders are: ")
                for price in ticketCost:
                    i += 1
                    displayCost = "${:,.2f}".format(price)
                    print("Ticket " + str(i) + " " + displayCost)

                total=0
                for price in ticketCost:
                    total = total + price
                displayTotalCost = "${:,.2f}".format(total)
                print("Your final total is: " + displayTotalCost)


            print("Thank you for choosing Tropical Airlines for your air travel needs.")
            exitProgram = True

        elif userInput == "i":
            print(
                "Thank you for choosing Tropical Airlines for your air travel needs. \nYou will be asked questions regarding what type of ticket you would like to purchase as well as destination information. \nWe also offer 50% discounted fares for children under the age of 16. Infants under the age of 2 are free.")
            print("You have been returned to the main menu.")
            print(" ")
        else:
            print("ERROR: Input not recognised. Please enter the letter in brackets to complete the intended action.")

main()

