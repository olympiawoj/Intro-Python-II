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
to north. The smell of gold permeates the air.""", [Item("Invisibility Cloak", "This cloak has the power to shield the wearer from being seen from sight and protects against spells")]),

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
player_name = input(Fore.YELLOW + "What is your name? ")
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
    input_msg = "Enter a direction to move your player ("
    # room['outside'].n_to exists
    if hasattr(room[player.current_room], 'n_to'):
        input_msg += " n"
    if hasattr(room[player.current_room], 's_to'):
        input_msg += " s"
    if hasattr(room[player.current_room], 'e_to'):
        input_msg += " e"
    if hasattr(room[player.current_room], 'w_to'):
        input_msg += " w"
    input_msg += " ) to move in that direction \nEnter q to quit game\n\n "
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
while done is False:

    print(Fore.WHITE + "\n*************************************************")
    print(Fore.WHITE +
          f"\n{player.name} is in the {room[player.current_room].name} room")
    print(Fore.WHITE +
          f"\nDescription: {room[player.current_room].description}\n")

    # printing the room list
    for item in room[player.current_room].item_list:
        print("Item List:")
        print(f"     - {item.name}: {item.description}")

    # try:
    # input returns an array of inputs, so we destructure to get the first

    # player_input = input(
    #     "Enter a cardinal direction (n, s, w, e) to move in that direction.
    # Enter q to quit the game: ")
    # input_msg = puts(colored.yellow("\n" + build_initial_input()))

    player_input = input(
        (Fore.YELLOW + "\n" + build_initial_input() + "\n")).strip().lower().split(' ')

    print('this is the player input', player_input)

    if player_input[0] == "get" or player_input[0] == "take":
        if player_input[1] not in player.inventory:
            player.add_item(player_input[1])
            # prints what item was taken
            item.on_take()
        else:
            print(
                Fore.RED, f"${player_input[1]} is already in player inventory!\n")

    elif player_input[0] == "i" or player_input[0] == "inventory":
        player.print_inventory()

    elif player_input[0] == "e" or player_input[0] == "Exit":
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
            print("\nGoodbye")
            print("\n*************************************************")
            done = True

    else:
        print(Fore.RED + "\nI did not understand that command.")
        # print("\n*************************************************")

    # except:
    #     print("\nThat is not a valid input.")
    #     break


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
