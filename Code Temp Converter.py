#Tara Keaton
#Code Temperature Converter assignment

#Input
#Welcome message

print (f"Tara's Code Temperature assignment ")

fTemp = float(input("Enter a temperature: "))

              
sDegree = input("Is this temperature F for Fahrenheit or C for Celsius? ")

if sDegree !="F" and sDegree !="C":
        print("Error: Enter (F) or (C)")


#Calculations
#Output
        
if sDegree == "F":
     if fTemp > 212:
      print("Error: Temp cannot be > 212 Fahrenheit ")
     else:
      fCelsius=(5.0/9)*(fTemp-32)
      print(f"The Celsius equivalent is: {fCelsius:.1f}C")

elif sDegree== "C":    
   if fTemp < 100:
     print("Error: Temp cannot be >100 Celsius ")
   else:
      fFahrenheit=((9.0/5.0)*fTemp)+32
      print(f"The Fahrenheit equivalent is: {fFahrenheit:.1f}F")
 




 



 
 

 

