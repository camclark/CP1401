def greeting():
    # appears on startup, asks for users name. Response saved as userName.
    userName = input("Please enter your name:\n")
    print("Welcome " + userName + "\n")
    return userName


def getAge():
    #gets age from the user, ensure is within expected range
    continueSwitch = False
    while continueSwitch == False:
        passengerAge = input("What is the age of the passenger?\n")

        if not passengerAge.isdigit():
            print("Error: Please input numbers")
            continue
        else:
            passengerAge = int(passengerAge)

        if passengerAge >= 0 and passengerAge <= 130:
            continueSwitch = True
        else:
            print("Please ensure you entered the correct age of the passenger")
    return passengerAge

def checkHandle(prompt,codeArray,wordArray):
    #codes are passed in along with array
    continueSwitch = False
    wrongCheck = True
    while continueSwitch == False:
        #uses prompt provided
        instanceInput = input(prompt + "\n")
        instanceInput = instanceInput.lower()
        #for i in len(codeArray):
        #remove x fill in i where req
        x = 0
        for Number in codeArray:
            #checks codeArray for expected
            if Number == instanceInput:
                continueSwitch = True
                #changes user input into a word
                instanceInput = wordArray[x]
                wrongCheck = False
            #special case for who for
            elif len(codeArray) == 2 and instanceInput == "s":
                instanceInput = input("Please enter the passenger's name\n")
                continueSwitch = True
                wrongCheck = False
                continue
            x = x + 1
            # Error message - none of the array match input
        if wrongCheck == True:
            print("Error input not recognised. \nPlease select what you would like by entering the corosponding letter in brackets \n")
    return instanceInput

def costCalculation(tripDestination, flightType, seatType, seatClass, passengerAge):
    # Calculates cost of trip from expected values
    if tripDestination == "Cairns" and flightType == "One-way":
        tripValue = 250
    elif tripDestination == "Cairns" and flightType == "Return":
        tripValue = 400
    elif tripDestination == "Sydney" and flightType == "One-way":
        tripValue = 420
    elif tripDestination == "Sydney" and flightType == "Return":
        tripValue = 575
    elif tripDestination == "Perth" and flightType == "One-way":
        tripValue = 510
    else:
        tripValue = 700

    if seatClass == "Business":
        classValue = 275
    elif seatClass == "Economy":
        classValue = 25
    else:
        classValue = 0

    if seatType == "Window":
        typeValue = 75
    elif seatType == "Aisle":
        typeValue = 50
    else:
        seatType == "Middle"
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

    #format "$0.00 - for display later"
    tripValue = "${:,.2f}".format(tripValue)
    classValue = "${:,.2f}".format(classValue)
    typeValue = "${:,.2f}".format(typeValue)

    return tripValue, classValue, typeValue, ageDiscountEligibility, cost



def acceptPurchase(cost):
    # presents user with a y/n to purchase ticket.
    # returns as cancelled if not accepted
    # otherwise leaves cost the way it is
    acceptSwitch = False
    while acceptSwitch == False:
        acceptPurchase = input("Would you like to purchase this ticket: (Y)es or (N)o \n")
        acceptPurchase = acceptPurchase.lower()
        if acceptPurchase == "y":
            print("Your ticket has been purchased. Thank you for flying with Tropical Airlines. \nYou have been returned to the main menu.")
            acceptSwitch = True
        elif acceptPurchase == "n":
            cost = "CANCELLED ORDER"
            print("Your ticket has not been purchased. You have been returned to the main menu.")
            acceptSwitch = True
        else:
            print("ERROR: Input not recognised. Please enter Y for yes or N for No.")
    return cost

def orderTicket(userName):
    #the main component of the program
    #passes information in arrays to check handle - ensures information is expected

    codeArray = ["y", "s"]
    wordArray = [userName]
    prompt = "Is the ticket for (Y)ou or (S)omeone else?"
    passengerName = checkHandle(prompt,codeArray,wordArray)

    passengerAge = getAge()

    codeArray = ["c", "s", "p"]
    wordArray = ["Cairns","Sydney","Perth"]
    prompt = "Please select the destination for your return trip. Base fare prices are listed below: \n(C)airns – $400 \n(S)ydney – $575 \n(P)erth - $700"
    tripDestination= checkHandle(prompt,codeArray,wordArray)


    codeArray = ["o", "r"]
    wordArray = ["One-way","Return"]
    prompt = "Is this a: \n(R)eturn trip  \n(O)ne-Way"
    flightType = checkHandle(prompt,codeArray,wordArray)


    codeArray = ["b", "e","f"]
    wordArray = ["Business", "Economy", "Frugal"]
    prompt = "Please choose the type of fare. Fees are displayed below and are in addition to the basic fare. \nPlease note choosing Frugal fare means you will not be offered a seat choice. \n(B)usiness - $275 \n(E)conomy - $25 \n(F)rugal - $0"
    seatClass = checkHandle(prompt, codeArray, wordArray)

    if seatClass == "Frugal":
        seatType = "Middle"
    else:
        codeArray = ["w", "a","m"]
        wordArray = ["Window", "Aisle", "Middle"]
        prompt = "Please choose the seat type.  Choosing the middle seat will deduct 25 from the total fare. \n(W)indow  $75 \n(A)isle  $50 \n(M)iddle -$25"

        seatType = checkHandle(prompt, codeArray, wordArray)

    #calculate cost from codes
    tripValue, classValue, typeValue, ageDiscountEligibility, cost = costCalculation(tripDestination,flightType,seatType,seatClass,passengerAge)
    costDisplay = "${:,.2f}".format(cost)

    #ensure user wants ticket
    print(" Ticket for: " + passengerName + "\nPassenger age: " + str(passengerAge) + "\t" + ageDiscountEligibility + "\nTrip destination: " + tripDestination + "(" + flightType + ")\t\t" + tripValue  + "\nSeat class: " + seatClass + "\t\t\t\t\t" + classValue + "\nSeat type: " + seatType + "\t\t\t\t\t\t" + typeValue + "\nTotal cost: " + costDisplay)
    cost = acceptPurchase(cost)
    return cost



def main():
    userName = greeting()
    exitProgram = False
    ticketCost = []

    while not exitProgram:
        print("Tropic Airlines Ticket Ordering System: \n(I)nstructions \n(O)rder ticket \n(E)xit ")

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
            print("Thank you for choosing Tropical Airlines for your air travel needs. \nYou will be asked questions regarding what type of ticket you would like to purchase as well as destination information. \nWe also offer 50% discounted fares for children under the age of 16. Infants under the age of 2 are free.")
            print("You have been returned to the main menu.\n")
        else:
            print("ERROR: Input not recognised. Please enter the letter in brackets to complete the intended action.")

main()

