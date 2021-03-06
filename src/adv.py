from room import Room
from player import Player
from item import Item
from colorama import init, Fore

init()

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("Flashlight", "It's dark in there, take this flashlight")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Wand", "The Wand of Destiny is made of elder wood with a core of Thestral hair. It's allegience can only be won by killing its previous owner. ")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Rope", "Don't fall, take this rope!")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("Cloak", "This is an invisibilty has the power to shield the wearer from being seen from sight and protects against spells")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Resurrection Stone", "Bring back your deceased loved ones with this magical stone")]),
}

# print('room string', room['outside'])
# print('room repr', repr(room['outside']))

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
player_name = input(Fore.YELLOW + "\nWhat is your name? ")
player = Player(player_name, [], [])
# print('player string', player)
# print('player repr', repr(player))

# print(f"\n{player.name} in the {player.current_room} room")


# to keep track of how many ns and s there are

choices = ["n", "s", "e", "w", "q"]

n = 0
s = 0
e = 0
w = 0

# TO DO
# Check input if there are 2 inputs in sys.arg, then check if it's get or take,


def build_initial_input():
    input_msg = "Enter a direction to move your player:"
    # room['outside'].n_to exists
    if hasattr(room[player.current_room], 'n_to'):
        input_msg += " n, "
    if hasattr(room[player.current_room], 's_to'):
        input_msg += " s, "
    if hasattr(room[player.current_room], 'e_to'):
        input_msg += " e, "
    if hasattr(room[player.current_room], 'w_to'):
        input_msg += " w, "
    input_msg += "or i/inventory for inventory.\nEnter exit or q to quit game "
    input_msg += "\nEnter take or get followed by item name to add item to inventory.\nEnter drop to remove item from inventory and add to room.\n\n "
    return input_msg

# Moves our player to new room, for this, we need to have a method on player


def move_to_new_room(new_room):
    if new_room.name == "Outside Cave Entrance":
        player.set_room("outside")
    elif new_room.name == "Foyer":
        player.set_room("foyer")
    elif new_room.name == "Grand Overlook":
        player.set_room("overlook")
    elif new_room.name == "Narrow Passage":
        player.set_room("narrow")
    elif new_room.name == "Treasure Chamber":
        player.set_room("treasure")


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

done = False
print('this is done', done)
while True:

    print(Fore.WHITE,  "\n*************************************************")
    print(Fore.MAGENTA +
          f"\n{player.name} is in the {room[player.current_room].name} room")
    print(Fore.WHITE +
          f"\n{room[player.current_room].description}\n")

    # printing the room list
    print(Fore.WHITE, "Item List:")
    if len(room[player.current_room].item_list) > 0:
        for item in room[player.current_room].item_list:
            print(Fore.WHITE, f"   * {item.name}: {item.description}")
    else:
        print(Fore.RED, "   * No items in room.")

    # try:
    # input returns an array of inputs, so we destructure to get the first

    # player_input = input(
    #     "Enter a cardinal direction (n, s, w, e) to move in that direction.
    # Enter q to quit the game: ")
    # input_msg = puts(colored.yellow("\n" + build_initial_input()))

    player_input = input(
        (Fore.YELLOW + "\n" + build_initial_input() + "\n~~~> ")).strip().lower().split(' ')

    # print('this is the player input', player_input)

    if player_input[0] == "get" or player_input[0] == "take":
        # if this weapon is not in the inventory, add it
        # otherwise print that it's already in the invenoty
        # if player_input[1] not in player.inventory:
        #     print('here its the inventory', player.inventory)
        item_moved = False
        for item in room[player.current_room].item_list:
            if item.name.lower() == player_input[1]:
                player.add_item(item)
                item_moved = True
                room[player.current_room].remove_item(item)
                # also where we should remove item fro mroom
                # prints what item was taken
                item.on_take()

        if not item_moved:
            print(Fore.RED, f"\nNo item by name {player_input[1]}")

    elif player_input[0] == "d" or player_input[0] == "drop":
        print("Dropped")
        item_moved = False
        for item in player.inventory:
            if item.name.lower() == player_input[1]:
                player.drop_item(item)
                room[player.current_room].add_item(item)
                item.on_drop()
                item_moved = True
        if not item_moved:
            print(
                Fore.RED, f"\nItem {player_input[1]} is not in your inventory")

    elif player_input[0] == "i" or player_input[0] == "inventory":
        player.print_inventory()

    elif player_input[0] == "Exit":
        print(Fore.RED, "Goodbye")
        break

    elif player_input[0] in choices:

        if player_input[0] == "n":
            if hasattr(room[player.current_room], 'n_to'):
                new_room = room[player.current_room].n_to
                move_to_new_room(new_room)
            else:
                print(Fore.RED + "\nThere is no room to the North of this room")
        elif player_input[0] == "s":
            if hasattr(room[player.current_room], 's_to'):
                new_room = room[player.current_room].s_to
                move_to_new_room(new_room)
            else:
                print(Fore.RED + "\nThere is no room to the South of this room")

        elif player_input[0] == "e":
            if hasattr(room[player.current_room], 'e_to'):
                new_room = room[player.current_room].e_to
                move_to_new_room(new_room)
            else:
                print(Fore.RED + "\nThere is no room to the East of this room")

        elif player_input[0] == "w":
            if hasattr(room[player.current_room], 'w_to'):
                new_room = room[player.current_room].w_to
                move_to_new_room(new_room)
            else:
                print(Fore.RED + "\nThere is no room to the West of this room")

        elif player_input[0] == "q":
            print(Fore.BLUE, "\nGoodbye")
            print(Fore.BLUE, "\n*************************************************")
            break

    else:
        print(Fore.RED + "\nI did not understand that command.")
        done = True
        break


#  CODE
# 1) Take an input - game asks, Where do you want to go? And prints all
# possible options [N] --> Moves character north. [Q] -->Quit [where, whereami]
# #--> gives character current location
# 2) Create a conditional, check if input is "n", "w", "s", "e". If it's not
# either of these, print an error
# if place is in the choices,


# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
