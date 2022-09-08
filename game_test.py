import os #best module, change my mind

#________________________________________________________________________________________________________________________________

#setup globals
Possible_Locations = ['Woods', 'Factory']
Current_Location = Possible_Locations[0]

#________________________________________________________________________________________________________________________________

def startup(): #Startup Screen
    print('''
                                        _            _   
                                        | |          | |  
    __ _  __ _ _ __ ___   ___   ______  | |_ ___  ___| |_ 
    / _` |/ _` | '_ ` _ \ / _ \ |______| | __/ _ \/ __| __|
    | (_| | (_| | | | | | |  __/          | ||  __/\__ \ |_ 
    \__, |\__,_|_| |_| |_|\___|           \__\___||___/\__|
    __/ |                                                 
    |___/                                                  
    ''')

    Username = input('What shall we call you,explorer?\n')
    print (f'Welcome to my game, {Username}')

def Ask_Location(Current_Location): #This asks for your location in an infinite loop
    New_Location = input(f'You are currently in the {Current_Location}! Where would you like to go?\n')
    if New_Location in Possible_Locations: 
        return Possible_Locations[Possible_Locations.index(New_Location)]
    else: return None

def main(): 
    startup()
    Current_Location = Ask_Location(Current_Location)

#________________________________________________________________________________________________________________________________

if __name__ == '__main__': main()