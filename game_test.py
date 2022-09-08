#import section

#random variables
Nothing = ""
#location variables
Possible_Locations = ["Woods","Factory"]
Current_Location = "Woods"
New_Location = ""

#This asks for your location in an inifite loop
def Ask_Location():
    New_Location = input("You are currently in the "+Current_Location+"! where would you like to go?\n")
    if New_Location in Possible_Locations:
        Current_Location = New_Location
        New_Location = None
    Ask_Location()

# Startup Screen
Username = input("What shall we call you,explorer?\n")
print ("Welcome to my game,"+Username+".")

Ask_Location()
