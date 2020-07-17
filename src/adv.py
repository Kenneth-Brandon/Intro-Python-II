from room import Room
from player import Player
from item import Item
import time
import getpass

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     Item('Dagger', 'A small dagger', "5", "15")),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", Item('Diamond', 'The most precious jewel of them all', "200", "0")),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", Item('Sword', 'A powerful sword!', "20", "30")),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", Item('Spear', 'A long shiny spear', "15", "25")),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", Item('Gold', "You're rich now!", "250", "0"))
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
playerName = getpass.getuser().title()

print('\nA fresh meat has joined our world...\n\nWelcome {}!'.format(playerName))
player = Player(playerName, room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
intro = """
The Menacing Cave has many treasures but the challenges will be difficult.
Look for these treasures in each room at your own risk
using the four cardinal directions (n, s, w, e).
Even if you die once there will be no reward, so
Beware of the masters of black magic and monsters that lurk around here.
You have been warned!"""

instructions = """
If you wish to return to safety, simply quit the game (q).
Use (b) if you would like to browse the current room for items.
Use (l) to loot the item.
And use (i) to check your current inventory of items."""

time.sleep(2)
print(intro)
time.sleep(1)
print(instructions)

print('\nStarting location: ' + player.location.name)

user_prompt = '\nMove around or just quit, but at the end it will be worth it... '

directions = ['n', 's', 'w', 'e']

response = ""
while response not in directions:

    response = input(user_prompt)

    if response == "n":
        player.move(response)
        print("Current location: " + player.location.name,
              "\nPrevious direction input: ", response)
        time.sleep(2)
        response = ""

    elif response == "s":
        player.move(response)
        print("Location: " + player.location.name,
              "\nPrevious direction input: ", response)
        time.sleep(2)
        response = ""

    elif response == "w":
        player.move(response)
        print("Location: " + player.location.name,
              "\nPrevious direction input: ", response)
        time.sleep(2)
        response = ""

    elif response == "e":
        player.move(response)
        print("Location: " + player.location.name,
              "\nPrevious direction input: ", response)
        time.sleep(2)
        response = ""

    elif response == "b":
        if player.browse_room_contents != []:
            time.sleep(2)
            print('\nName:', player.browse_room_contents.name,
                  '\nDescription:', player.browse_room_contents.description,
                  '\nDamage:', player.browse_room_contents.damage,
                  '\nValue:', player.browse_room_contents.value)
        else:
            time.sleep(2)
            print('\nNothing left to loot')

    elif response == "l":
        if player.location.loot != []:
            time.sleep(2)
            player.loot()
            print([item.name for item in player.items])
            print('\nThis might be useful.\n')
        else:
            time.sleep(2)
            print("Nothing left to loot. I'm serious.")

    elif response == "i":
        time.sleep(2)
        print("Player Inventory:\n\n", [item.name for item in player.items])

    elif response == "q":
        print('\n\nThanks for playing!')
        time.sleep(2)
        quit()

    else:
        time.sleep(2)
        print("I didn't quite catch that, try again.\n")
