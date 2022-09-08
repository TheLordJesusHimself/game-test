import os #best module, change my mind

#________________________________________________________________________________________________________________________________

#setup globals
Possible_Locations = ['Woods', 'Factory']
Current_Location = Possible_Locations[Possible_Locations.index('Woods')]

#________________________________________________________________________________________________________________________________

def startup(): #Startup Screen
    print('                                       _            _   \n                                      | |          | |  \n  __ _  __ _ _ __ ___   ___   ______  | |_ ___  ___| |_ \n / _` |/ _` | \'_ ` _ \ / _ \ |______| | __/ _ \/ __| __|\n| (_| | (_| | | | | | |  __/          | ||  __/\__ \ |_ \n \__, |\__,_|_| |_| |_|\___|           \__\___||___/\__|\n  __/ |                                                 \n |___/                                                  \n')
    
    Username = input('What shall we call you, explorer?\n >\t')
    print (f'Welcome to my game, {Username}')

def Ask_Location(Current_Location): #This asks for your location in an infinite loop
    New_Location = input(f'\nYou are currently in the {Current_Location.strip()}! Where would you like to go?\n >\t')
    if New_Location in Possible_Locations: 
        return Possible_Locations[Possible_Locations.index(New_Location)]
    else: Ask_Location(Current_Location)

def main(Current_Location): 
    startup()
    
    try:
        while True:
            Current_Location = Ask_Location(Current_Location)
            #print(Current_Location)
    except KeyboardInterrupt: pass

#________________________________________________________________________________________________________________________________

if __name__ == '__main__': main(Current_Location)