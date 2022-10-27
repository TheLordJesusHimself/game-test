import os #best module, change my mind

#________________________________________________________________________________________________________________________________

#setup globals
Possible_Locations = ['woods', 'factory']
Current_Location = Possible_Locations[Possible_Locations.index('woods')] #get location of value `'Woods'` in list

#________________________________________________________________________________________________________________________________

def startup() -> None: #Startup Screen
    print('                                       _            _   \n                                      | |          | |  \n  __ _  __ _ _ __ ___   ___   ______  | |_ ___  ___| |_ \n / _` |/ _` | \'_ ` _ \ / _ \ |______| | __/ _ \/ __| __|\n| (_| | (_| | | | | | |  __/          | ||  __/\__ \ |_ \n \__, |\__,_|_| |_| |_|\___|           \__\___||___/\__|\n  __/ |                                                 \n |___/                                                  \n')
    #ascii art^^
    Username = input('What shall we call you, explorer?\n >\t') #creates little arrow to indicate input
    print (f'Welcome to my game, {Username}') #fstrings

def Ask_Location(Current_Location) -> str | None: #This asks for your location
    New_Location = input(f'\nYou are currently in the {Current_Location.strip()}! Where would you like to go?\n >\t') # `Current_Location.strip()` just removes trailing whitepace
    if New_Location in Possible_Locations: #english syntax
        return Possible_Locations[Possible_Locations.index(New_Location)] #lookup new location in list, return value at the point (should be same as new location)
    else: Ask_Location(Current_Location)

def main(Current_Location) -> None: #had to pass var through
    startup() #start screen
    
    try: #when not `Ctrl+C`
        while True: #Loops
            Current_Location = Ask_Location(Current_Location) #ask, passing parems & returns
            #smth happens in that place
    except KeyboardInterrupt: pass #if you press `Ctrl+C` the game ends

#________________________________________________________________________________________________________________________________

if __name__ == '__main__': main(Current_Location) #if run directly, do `main()`