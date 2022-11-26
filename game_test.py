# shebang
# -*- coding: UTF-8 -*-

# https://github.com/Cornelius-Figgle/TheLordJesusHimself--game-test/

'''
game test
'''

# note: view associated GitHub info as well
__version__ = 'Pre-release'  
__author__ = 'TheLordJesusHimself'
__email__ = 'callumblumfield08@gmail.com'
__maintainer__ = ['TheLordJesusHimself', 'Cornelius-Figgle']
__copyright__ = 'Copyright (c) 2022 Max Harrison'
__license__ = 'MIT'
__status__ = 'Development'
__credits__ = ['Callum Blumfield', 'Max Harrison']


import sys


possible_locations = ['woods', 'factory', 'heaven']
current_location = possible_locations[possible_locations.index('woods')]
# note: get location of value `Woods` in list

def startup() -> None:  # note: Startup Screen
    '''
    Prints title art and saves `username`
    '''
    
    print('                                       _            _   \n                                      | |          | |  \n  __ _  __ _ _ __ ___   ___   ______  | |_ ___  ___| |_ \n / _` |/ _` | \'_ ` _ \ / _ \ |______| | __/ _ \/ __| __|\n| (_| | (_| | | | | | |  __/          | ||  __/\__ \ |_ \n \__, |\__,_|_| |_| |_|\___|           \__\___||___/\__|\n  __/ |                                                 \n |___/                                                  \n')
    # note: ascii art^^
    username = input('What shall we call you, explorer?\n >\t')
    username = capital_each(username)
    print(f'Welcome to my game, {username}')

def capital_each(string: str) -> str: 
    '''
    Makes each word in `string` lowercase and start with a capital, 
    returns `string` with new formatting

    - makes a list from each word
    - for each word:
        - makes it a capital
    - makes it back into string
    '''

    string = string.lower().split(' ')
    for word in string:
        string[string.index(word)] = word.capitalize()
    string = ' '.join(string)
    return string

def ask_location(current_location: str) -> str: 
    '''
    Asks for location and changes `current_location` if `new_location`
    is valid. Returns the new location (sourced from 
    `possible_locations`) if `new_location` is valid, else 
    `current_location`

    - print it nicely just for u
    - `current_location.strip()` just removes trailing whitespace
    - convert `new_location` to lowercase then see if it is a valid 
    location
    - lookup new location in list, return value at the point (should 
    be same as new location)
    '''

    current_location = capital_each(current_location)
    new_location = input('\nYou are currently in the' \
    f'{current_location.strip()}! Where would you like to go?\n >\t')

    if new_location.lower() in possible_locations:
        return possible_locations[
            possible_locations.index(
                new_location.lower()
            )
        ] 
    else: 
        print('Not a valid answer')
        return current_location


def main(current_location: str) -> None:
    '''
    The main function that handles passing or args and return values.
    Also handles the application loop and errors from functions - has
    to be called with `current_location` to be able to pass it through
    to `ask_location()`

    In future will run the order of storyline etc
    '''
    
    startup()
    
    try:  # note: when not `Ctrl+C`
        while True: #Loops
            current_location = ask_location(current_location) 
            # note: ask, passing params & returns
            # note: smth happens in that place
    except KeyboardInterrupt: 
        sys.exit(0)  # note: if you press `Ctrl+C` the game loop ends

if __name__ == '__main__': 
    main(current_location)   #note: if run directly, do `main()`