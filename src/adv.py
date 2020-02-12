from room import Room
from player import Player

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
player_name = input("What is your name? ")
player = Player(player_name, [])
# print('player string', player)
# print('player repr', repr(player))

# print(f"\n{player.name} in the {player.current_room} room")


# to keep track of how many ns and s there are

room_choices = ["n", "s", "e", "w"]


def eval_room_choices(player_choice):
    n = 0
    s = 0
    e = 0
    w = 0
    print(f"n: {n}, s: {s}, e: {e}, w: {w}")
    if player_choice == "n":
        print("chose n")
        n += 1
    elif player_choice == "s":
        print("chose s")
        s += 1
    elif player_choice == "e":
        print("chose s"),
        e += 1
    elif player_choice == "w":
        print("chose w"),
        w += 1
    else:
        print("not an input option")


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

while True:
    print("\n*************************************************")
    print(f"\n{player.name} is in the {player.current_room} room")

    [player_choice] = input(
        "\nWhere do you want to go? ").strip().lower().split(' ')
    print('\nthis is the player choice', player_choice)

    if player_choice in room_choices:
        print("Player chose ", player_choice)
        eval_room_choices(player_choice)
    elif player_choice == "q":
        print("Goodbye")
        break
    else:
        print("I did not understand that command. Please pick n, s, e, w, or q")

        # if room in room_choices:
        #     # print(room)
        #     eval_room_choices(player_choice)
        # else:
        #     print("not in choices")

# PSUEDO CODE
# 1) Take an input - game asks, Where do you want to go? And prints all possible options [N] --> Moves character north. [Q] -->Quit [where, whereami] --> gives character current location
# 2) Create a conditional, check if input is "n", "w", "s", "e". If it's not either of these, print an error
# if place is in the choices,


# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
