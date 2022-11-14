import os #best module, change my mind

#________________________________________________________________________________________________________________________________

#setup globals
Possible_Locations = ['woods', 'factory', 'heaven']
Current_Location = Possible_Locations[Possible_Locations.index('woods')] #get location of value `'Woods'` in list

#________________________________________________________________________________________________________________________________

def startup() -> None: #Startup Screen
	print('                                       _            _   \n                                      | |          | |  \n  __ _  __ _ _ __ ___   ___   ______  | |_ ___  ___| |_ \n / _` |/ _` | \'_ ` _ \ / _ \ |______| | __/ _ \/ __| __|\n| (_| | (_| | | | | | |  __/          | ||  __/\__ \ |_ \n \__, |\__,_|_| |_| |_|\___|           \__\___||___/\__|\n  __/ |                                                 \n |___/                                                  \n')
	#ascii art^^
	Username = input('What shall we call you, explorer?\n >\t') #creates little arrow to indicate input
	Username = capital_each(Username)
	print (f'Welcome to my game, {Username}') #fstrings

def capital_each(string: str) -> str: #makes each word lowercase and start with a capital letter
	string = string.lower().split(' ') #make a list from each word
	for word in string: #for each word
		string[string.index(word)] = word.capitalize() #make it capital
	string = ' '.join(string) #make back into str
	return string #return str

def Ask_Location(Current_Location: str) -> str | None: #This asks for your location
	Current_Location = capital_each(Current_Location) #print it nicely just for u
	New_Location = input(f'\nYou are currently in the {Current_Location.strip()}! Where would you like to go?\n >\t') # `Current_Location.strip()` just removes trailing whitespace

	if New_Location.lower() in Possible_Locations: #convert new loc to lowercase then see if it is a valid loc
		return Possible_Locations[Possible_Locations.index(New_Location.lower())] #lookup new location in list, return value at the point (should be same as new location)
	else: 
		print('Not a valid answer')
		Ask_Location(Current_Location) #redo the function (mildly illegal code)

def main(Current_Location: str) -> None: #had to pass var through
	startup() #start screen
	
	try: #when not `Ctrl+C`
		while True: #Loops
			Current_Location = Ask_Location(Current_Location) #ask, passing params & returns
			#smth happens in that place
	except KeyboardInterrupt: pass #if you press `Ctrl+C` the game ends

#________________________________________________________________________________________________________________________________

if __name__ == '__main__': main(Current_Location) #if run directly, do `main()`