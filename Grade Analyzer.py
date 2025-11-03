# Tara Keaton Hill
# Grade Analyzer Assignment

#INPUT
# Ask for the person's name
sName = input ("Enter the name of the individual this Grade Analyzer is for: ")

#Ask for four test scores in whole numbers
iTestScore1 = int(input("What is Test Score 1: "))
iTestScore2 = int(input("What is Test Score 2: "))                 
iTestScore3 = int(input("What is Test Score 3: "))
iTestScore4 = int(input("What is Test Score 4: "))


#Check of grade is 0
if iTestScore1 < 0 or iTestScore2 < 0 or iTestScore3 < 0 or iTestScore4 < 0:
    print ("Test scores must be greater than 0")
    raise SystemExit
sTestDrop = input ("Should the lowest score determined be dropped? (Enter Y or N)")

#If the user said Yes,drop the lowest score
if sTestDrop == "Y" or sTestDrop == "y" or sTestDrop == "Yes" or sTestDrop == "yes":
   iTest = 3 
   if iTestScore1 <= iTestScore2 and iTestScore1 <=iTestScore3 and iTestScore1 <= iTestScore4:
        iLow = iTestScore1
   elif iTestScore2 <=iTestScore1 and iTestScore2 <= iTestScore3 and iTestScore2 <= iTestScore4:
        iLow = iTestScore2
   elif iTestScore3 <= iTestScore1 and iTestScore3 <= iTestScore2 and iTestScore3 <= iTestScore4:
        iLow = iTestScore3
   else:
        iLow = iTestScore4
        
   iAverage = (iTestScore1 + iTestScore2 + iTestScore3 + iTestScore4 - iLow)/iTest
   
elif sTestDrop == "N" or sTestDrop =="n" or sTestDrop == "No" or sTestDrop == "no":
    iLow = 0
    iTest = 4
    
#Calculate the Average and Drop the lowest score
    iAverage = (iTestScore1 + iTestScore2 + iTestScore3 + iTestScore4) /iTest
    
else:
    print("You need to enter Y or N")
    raise SystemExit

# Analyze the Letter grade based on the scores

if iAverage >=97:
    sGrade = "A+"
elif iAverage >= 94:
    sGrade = "A"
elif iAverage >=90:
    sGrade = "A-"
elif iAverage >=87:
    sGrade = "B+"
elif iAverage >=84:
    sGrade = "B"
elif iAverage >=80:
    sGrade = "B-"
elif iAverage >=77:
    sGrade = "C+"
elif iAverage >=74:
    sGrade = "C"
elif iAverage >=70:
    sGrade = "C-"
elif iAverage >=67:
    sGrade = "D+"
elif iAverage >=64:
    sGrade = "D"
elif iAverage >=60:
    sGrade = "D-"
else:
    sGrade = "F"

#Print out the average, formatted, print out the letter
print (sName, "'s test average is:", iAverage)
print("The letter grade is equal:", sGrade)


    
 
    
