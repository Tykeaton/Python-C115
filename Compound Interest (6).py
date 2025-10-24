# Tara Keaton Hill
# Compound Interest assignment

#input

PV = float(input("Enter the starting principal: "))#1000

R = float(input("Enter the annual interest Rate: "))/100 #2.5

t = int(input("How many times per year is the interest compounded? ")) #12

m=int(input("For how many years will the account earn interest? "))#2

#convert

FV = PV *(1+R/t)**(m*t)

#output

print(f"At the end of {m} years you will have ${FV:,.2f}")
