# Tara Hill Keaton
# Inter Planetary Weights assignment

# #1.
# fMERCURY = 0.38
# fVENUS   = 0.91
# fMOON    = 0.165
# fMARS    = 0.38
# fJUPITER = 2.34
# fSATURN  = 0.93
# fURANUS  = 0.92
# fNEPTUNE = 1.12
# fPLUTO   = 0.066

fMERCURY = 0.38
fVENUS   = 0.91
fMOON    = 0.165
fMARS    = 0.38
fJUPITER = 2.34
fSATURN  = 0.93
fURANUS  = 0.92
fNEPTUNE = 1.12
fPLUTO   = 0.066

#Input 
sName = input("Enter Name: ")
fWeight = float(input("Enter Weight: "))
                
fMercuryWeight = fWeight * fMERCURY
fVenusWeight = fWeight *   fVENUS
fMoonWeight = fWeight *    fMOON
fMarsWeight = fWeight *    fMARS
fJupiterWeight = fWeight * fJUPITER
fSaturnWeight =  fWeight * fSATURN
fUranusWeight = fWeight * fURANUS
fNeptuneWeight = fWeight * fNEPTUNE
fPlutoWeight = fWeight * fPLUTO

print("Moose here are your weights on the Solar System's planets:")

 #print("Weight on Mercury:", fMercuryWeight)
 #print("weight on venus:", fVenusWeight)
 #print("Weight on Moon:", fMoonWeight)
 #print("Weight on Mars:", fMarsWeight)
 #print("Weight on Jupiter:", fJupiterWeight)
 #print("Weight on Saturn:", fSaturn Weight)
 #print("Weight on Uranus:", fUranusWeight)
 #print("Weight on Neptune:", fNeptuneWeight)
 #print("Weight on Pluto:", fPlutoWeight)

 #print using a f string or fast string

 #print(f"{Weight on Mercury:':20s}{fMercuryWeight:10,.2f}) 
 #print(f"{Weight on Venus:':20s}{fVenusWeight:10,.2f}) 
 #print(f"{Weight on Moon:':20s}{fMoonWeight:10,.2f})
 #print(f"{Weight on Mars:':20s}{fMarsWeight:10,.2f})
 #print(f"{Weight on Jupiter:':20s}{fJupiterWeight:10,.2f})
 #print(f"{Weight on Saturn:':20s}{fSaturnWeight:10,.2f})
 #print(f"{Weight on Uranus:':20s}{fUranusWeight:10,.2f})
 #print(f"{Weight on Neptune:':20s}{fNeptuneWeight:10,.2f})
 #print(f"{Weight on Pluto:':20s}{fPlutoWeight:10,.2f})


print(f"Weight on Mercury:  {fMercuryWeight:10.2f}")
print(f"Weight on Venus:    {fVenusWeight:10.2f}")
print(f"Weight on Moon:     {fMoonWeight:10.2f}")
print(f"Weight on Mars:     {fMarsWeight:10.2f}")
print(f"Weight on Jupiter:  {fJupiterWeight:10.2f}")
print(f"Weight on Saturn:   {fSaturnWeight:10.2f}")
print(f"Weight on Uranus:   {fUranusWeight:10.2f}")
print(f"Weight on Neptune:  {fNeptuneWeight:10.2f}")
print(f"Weight on Pluto:    {fPlutoWeight:10.2f}")

       
