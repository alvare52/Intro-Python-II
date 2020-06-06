from room import Room
from player import Player
from item import Item
import textwrap
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].connections["n"] = room['foyer']
room['foyer'].connections["s"] = room['outside']
room['foyer'].connections["n"] = room['overlook']
room['foyer'].connections["e"] = room['narrow']
room['overlook'].connections["s"] = room['foyer']
room['narrow'].connections["w"] = room['foyer']
room['narrow'].connections["n"] = room['treasure']
room['treasure'].connections["s"] = room['narrow']

# Items for each room
room["outside"].items = Item("Sword", "A big stupid sword")
room["foyer"].items = Item("Gun", "A handsome blue gun")
room["overlook"].items = Item("Soap", "An old bar of soap")
room["narrow"].items = Item("Napkins", "A bucket of wet napkins")

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
new_player = Player("John", room["outside"])
print(new_player)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
game_is_running = True
while game_is_running:
    print(new_player.current_location)
    
    for line in textwrap.wrap(new_player.current_location.description, 40):
        print(line)
    
    print(f"Contains: {new_player.current_location.items}")

    if new_player.current_location.name == "Treasure Chamber":
            print("*** You found the treasure! You win! ***")
            break
    
    user_input = input("Enter a direction(n, e, s, w) (q to quit): ")

    # If the user enters a cardinal direction, attempt to move to the room there.
    if user_input in ["n", "e", "s", "w"]:
        new_player.move(user_input)

    # Print an error message if the movement isn't allowed.
    elif user_input == "q":
        print("Thanks for playing")
        game_is_running = False

    # If the user enters "q", quit the game.
    else:
        print("That move isn't allowed")