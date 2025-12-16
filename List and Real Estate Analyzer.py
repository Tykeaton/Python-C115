# Tara Hill Keaton

## Lists and Real Estate Analyzer

## Get float input

def getFloatInput(sQuery):
    while True:
        try:
            fValue = float(input(sQuery))
            if fValue > 0:
                return fValue
            else:
                print("Input a number greater than zero:")
        except ValueError:
            print("Input a number greater than zero")


## Get median

def getMedian(fNumbers):
    fCount = len(fNumbers)
    fMedian = fCount//2
    
    if fCount % 2 == 1:
        return fNumbers[fMedian]
    else:
        return (fNumbers[fMedian -1] + fNumbers[fMedian])/2
    

## main

def main():
    RealEstateList = []
    again = "Y"

    while again == "Y" or again == "y":
        fRealEstateValue = getFloatInput("Enter Property Sales Value: ")
        RealEstateList.append(fRealEstateValue)

        again = input("Enter another value Y or N: ")

        while again not in ["Y", "y", "N", "n"]:
            again = input("Enter Y or N: ")

    RealEstateList.sort()
    print ("\nSales Values")


    for iProperty in range(len(RealEstateList)):
        print("Property ", str(iProperty+1), "$", format((RealEstateList[iProperty]),'11,.2f'))
        
## Print and format output
    fMin = min(RealEstateList)
    fMax = max(RealEstateList)
    fTotal = sum(RealEstateList)
    fAverage = fTotal/len(RealEstateList)
    fMedian =getMedian(RealEstateList)
    fCommissionRate = 0.03
    fCommission = fTotal * fCommissionRate
    
    print("Min:","$",format(fMin,"12,.2f"))
    print("Max: ","$",format(fMax,"12,.2f"))
    print("Total:", "$",format(fTotal,"12,.2f"))
    print("Average:","$",format(fAverage,"12,.2f"))
    print("Median:","$",format (fMedian,"12,.2f"))
    print ("Commission:","$",format(fCommission,"12,.2f"))
    


main()



            
            
            
