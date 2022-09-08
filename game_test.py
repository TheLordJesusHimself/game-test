import os #best module, change my mind

#________________________________________________________________________________________________________________________________

#setup globals
Possible_Locations = ['Woods', 'Factory']
Current_Location = Possible_Locations[0]

#________________________________________________________________________________________________________________________________

def startup():
    # Startup Screen
    Username = input('What shall we call you,explorer?\n')
    print (f'Welcome to my game, {Username}')

#This asks for your location in an inifite loop
def Ask_Location(Current_Location):
    New_Location = input(f'You are currently in the {Current_Location}! Where would you like to go?\n')
    if New_Location in Possible_Locations: 
        return Possible_Locations[Possible_Locations.index(New_Location)]
    else: return None

def main(): 
    startup()
    Current_Location = Ask_Location(Current_Location)

#________________________________________________________________________________________________________________________________

if __name__ == '__main__': main()