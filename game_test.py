#import section

#setting var
Possible_Locations = ["Woods","Factory"]
Current_Location = "Woods"
New_Location = ""

# Startup Screen
Username = input("What shall we call you,explorer?\n")
print ("Welcome to my game,"+Username+".")
New_Location = input("You are currently in the "+Current_Location+"! where would you like to go?\n")
if New_Location in Possible_Locations:
    print("in location")
elif New_Location not in Possible_Locations:
    print("not in location")