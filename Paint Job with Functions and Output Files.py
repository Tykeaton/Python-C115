# Tara Keaton
# Paint Job with Functions and Output Files assignment

import math

# Create float function

def getFloatInput(sInput):
    while True:
        try:
            fValue = float(input(sInput))
            if fValue <= 0:
                print("Input must be a positive numeric value")
            else:
                return fValue
        except ValueError:
            print("Input must be a postive numeric value")


#Get paint rounded up
def getGallonsOfPaint(fWallSize, fFeetPerGallon):
    fGallonsNeeded = fWallSize / fFeetPerGallon
    iGallonsOfPaint = math.ceil(fGallonsNeeded)
    return iGallonsOfPaint

#Define total hours
def getLaborHours(fLaborHours, iGallonsOfPaint):
    return fLaborHours * iGallonsOfPaint


#Define labor cost
def getLaborCost(fLaborHours, fLaborChargePerHour):
    return fLaborHours * fLaborChargePerHour

#Define cost of paint
def getPaintCost(iGallonsOfPaint, fPaintPrice):
    return iGallonsOfPaint * fPaintPrice


#Define Sales tax per state
def getSalesTax(sState):
    sState = sState.upper()

    if sState == "CT":
        return 0.06
    elif sState == "MA":
        return 0.0625
    elif sState == "ME":
        return 0.085
    elif sState == "NH":
        return 0.0
    elif sState == "RI":
        return 0.07
    elif sState == "VT":
        return 0.06
    else:
        return 0.0


# Show cost estimate and write to file
def showCostEstimate(iGallonsOfPaint, fLaborHours, fPaintPrice, fLaborCost, fTaxAmount, fTotalCost, sCustomerLastName):

    sFileName = sCustomerLastName + "_PaintJobOutput.txt"
    fOutFile = open(sFileName, "w")

    def print_and_write(sLine):
        print(sLine)
        fOutFile.write(sLine + "\n")

    print_and_write("Gallons of paint: " + str(iGallonsOfPaint))
    print_and_write("Hours of labor: " + format(fLaborHours, ".2f"))
    print_and_write("Paint charges: $" + format(fPaintPrice, ",.2f"))
    print_and_write("Labor ccharges: $" + format(fLaborCost, ",.2f"))
    print_and_write("Tax: $" + format(fTaxAmount, ",.2f"))
    print_and_write("Total cost: $" + format(fTotalCost, ",.2f"))

    fOutFile.close()
    print("File:", sFileName, "was created.")


def main():
    fWallSize = getFloatInput("Enter wall space in square feet: ")
    fPaintPrice = getFloatInput("Enter the price per gallon: " )
    fFeetPerGallon = getFloatInput("Enter feet per gallon: ")
    fLaborHours = getFloatInput("How many labor hours per gallon: ")
    fLaborCost = getFloatInput("Labor charge per hour: ")
    sState = input("State job is in: ")
    sCustomerLastName = input("Customer Last Name: ")

    iGallonsOfPaint = getGallonsOfPaint(fWallSize, fFeetPerGallon)
    fLaborHours = getLaborHours(fLaborHours, iGallonsOfPaint)
    fLaborCost = getLaborCost(fLaborHours, fLaborCost)
    fPaintCost = getPaintCost(iGallonsOfPaint, fPaintPrice)

    fTaxRate = getSalesTax(sState)
    fTaxAmount = (fLaborCost + fPaintCost) * fTaxRate
    fTotalCost = fLaborCost + fPaintCost + fTaxAmount

    showCostEstimate(iGallonsOfPaint, fLaborHours, fPaintCost, fLaborCost, fTaxAmount, fTotalCost, sCustomerLastName)

main()

