import os #best module, change my mind

#________________________________________________________________________________________________________________________________

#setup globals
possible_locations = ['woods', 'factory', 'heaven']
current_location = possible_locations[possible_locations.index('woods')] #get location of value `'Woods'` in list

#________________________________________________________________________________________________________________________________

def startup() -> None: #Startup Screen
	'''
	Prints title art and saves `username`
	'''
	
	print('                                       _            _   \n                                      | |          | |  \n  __ _  __ _ _ __ ___   ___   ______  | |_ ___  ___| |_ \n / _` |/ _` | \'_ ` _ \ / _ \ |______| | __/ _ \/ __| __|\n| (_| | (_| | | | | | |  __/          | ||  __/\__ \ |_ \n \__, |\__,_|_| |_| |_|\___|           \__\___||___/\__|\n  __/ |                                                 \n |___/                                                  \n')
	#ascii art^^
	username = input('What shall we call you, explorer?\n >\t') #creates little arrow to indicate input
	username = capital_each(username)
	print(f'Welcome to my game, {username}') #fstrings

def capital_each(string: str) -> str: 
	'''
	Makes each word in `string` lowercase and start with a capital
	
	Returns `string` with new formatting
	'''

	string = string.lower().split(' ') #make a list from each word
	for word in string: #for each word
		string[string.index(word)] = word.capitalize() #make it capital
	string = ' '.join(string) #make back into str
	return string #return str

def ask_location(current_location: str) -> str: 
	'''
	Asks for location and changes `current_location` if `new_location` is valid

	Returns the new location (sourced from `possible_locations`) if `new_location` is valid, else `current_location`
	'''

	current_location = capital_each(current_location) #print it nicely just for u
	new_location = input(f'\nYou are currently in the {current_location.strip()}! Where would you like to go?\n >\t') # `current_location.strip()` just removes trailing whitespace

	if new_location.lower() in possible_locations: #convert new loc to lowercase then see if it is a valid loc
		return possible_locations[possible_locations.index(new_location.lower())] #lookup new location in list, return value at the point (should be same as new location)
	else: 
		print('Not a valid answer')
		return current_location

def main(current_location: str) -> None: #had to pass var through
	'''
	Simply loops through each stage, has to be called with `current_location` to be able to pass it through to `ask_location()`

	In future will run the order of storyline
	'''
	
	startup() #start screen
	
	try: #when not `Ctrl+C`
		while True: #Loops
			current_location = ask_location(current_location) #ask, passing params & returns
			#smth happens in that place
	except KeyboardInterrupt: pass #if you press `Ctrl+C` the game ends

#________________________________________________________________________________________________________________________________

if __name__ == '__main__': main(current_location) #if run directly, do `main()`