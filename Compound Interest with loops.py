# Tara Keaton Hill
# Compound Interest with Loops assignment

# Initial Variable
fDeposit = 0

# Input, and data validation using try and except
while fDeposit <=0:
    try:
        fDeposit = float(input("Enter the starting deposit: "))
        if fDeposit <=0:
            print ("Input must be a positive numeric value")
    except ValueError:
        print ("Input a numeric value")

# Initial variable for interest rate
fRate = 0

# Input, and data validation using try except for fRate
while fRate <= 0:
   try:
        fRate = float(input("Enter the annual interest rate: "))/100
        if fRate <=0:
            print ("Input must be a positive numeric value")
   except ValueError:
        print ("Input a numeric value")

# Convert interest rate to monthly value
fRate = fRate / 12

# Initial variable for months
iNumberofMonths = 0

# Input, and data validation using try except for fNumber of Months
while iNumberofMonths <= 0:
   try:
        iNumberofMonths = int(input("How many total months invested? "))       
        if iNumberofMonths <= 0:
            print ("Input must be a positive numeric value")
   except ValueError:
        print ("Input a numeric value")

# Initial variable for goal
fGoal = -1

#Input, and data validation using try except for fGoal
while fGoal < 0:
   try:
        fGoal = float(input("What is the goal amount? "))       
        if fGoal < 0:
            print ("Input must be greater than 0")
        
   except ValueError:
        print ("Input must be a numeric value greater than 0")


# Initial, and data validation using while for iTime
iTime = 0
fAccountBalance = fDeposit

while iTime < iNumberofMonths:
    iTime +=1
    fAccountBalance = fDeposit * ((1+ fRate)**iTime)
    print ("Month", iTime, "Account Balance is $", format(fAccountBalance,",.2f"))
    

#Initial, and data validation using while for fAcountBalance
iTime = 0
fAccountBalance = fDeposit * ((1+ fRate)**iTime)

while fAccountBalance < fGoal:
    iTime +=1
    fAccountBalance = fDeposit * ((1+ fRate)**(iTime))

#Output
print("It will take",iTime,"months to reach your goal of $", format(fGoal,",.2f"))









