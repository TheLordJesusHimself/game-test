#import section

#random variables
Nothing = ""
#location variables
Possible_Locations = ["Woods","Factory"]
Current_Location = "Woods"
New_Location = ""


# Startup Screen
Username = input("What shall we call you,explorer?\n")
print ("Welcome to my game,"+Username+".")
New_Location = input("You are currently in the "+Current_Location+"! where would you like to go?\n")
if New_Location in Possible_Locations:
    Current_Location = New_Location
    New_Location = None
print ("Current Location =",Current_Location)
print ("New_Location =",New_Location)