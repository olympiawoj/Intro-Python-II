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

choices = ["n", "s", "e", "w", "q"]

n = 0
s = 0
e = 0
w = 0

# TO DO
# Build a function that moves player based on new room
# IF there's no room to the n/s/e/w of the room yu're currently in, don't allow you to move in this


def build_initial_input():
    print('this is running')
    input_msg = "Enter a direction to move your player:"
    # room['outside'].n_to exists
    if hasattr(room[player.current_room], 'n_to'):
        input_msg += " n,"
    if hasattr(room[player.current_room], 's_to'):
        input_msg += " s,"
    if hasattr(room[player.current_room], 'e_to'):
        input_msg += " e,"
    if hasattr(room[player.current_room], 'w_to'):
        input_msg += " w,"
    input_msg += " enter q to quit game: "
    return input_msg

# Moves our player to new room, for this, we need to have a method on player


def move_to_new_room(new_room):
    if new_room.name == "Outside":
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
while done == False:

    print("\n*************************************************")
    print(f"\n{player.name} is in the {player.current_room} room")

    # try:
    # input returns an array of inputs, so we destructure to get the first

    # player_input = input(
    #     "Enter a cardinal direction (n, s, w, e) to move in that direction. Enter q to quit the game: ")
    player_input = input("\n" + build_initial_input()
                         ).strip().lower().split(" ")

    print('\nthis is the player choice', player_input[0])

    player_input = player_input[0]

    if player_input in choices:
        print("Player input ", player_input)

        if player_input == "n":
            if hasattr(room[player.current_room], 'n_to'):
                new_room = room[player.current_room].n_to
                move_to_new_room(new_room)
                print('new room', new_room)
            else:
                print("There is no room to the North of this room\n")

            # n += 1
        elif player_input == "s":
            if hasattr(room[player.current_room], 's_to'):
                new_room = room[player.current_room].s_to
                move_to_new_room(new_room)
                print("chose s")
                # s += 1
            else:
                print("There is no room to the South of this room\n")

        elif player_input == "e":
            if hasattr(room[player.current_room], 'e_to'):
                print("chose e"),
                new_room = room[player.current_room].e_to
                move_to_new_room(new_room)
            else:
                print("There is no room to the East of this room\n")

        elif player_input == "w":
            if hasattr(room[player.current_room], 'w_to'):
                print("chose w")
                new_room = room[player.current_room].w_to
                move_to_new_room(new_room)
            else:
                print("There is no room to the West of this room\n")

        elif player_input == "q":
            print("Goodbye")
            break

    else:
        print("I did not understand that command. Please pick n, s, e, w, or q")

    # except:
    #     print("\nThat is not a valid input.")
    #     break


# PSUEDO CODE
# 1) Take an input - game asks, Where do you want to go? And prints all possible options [N] --> Moves character north. [Q] -->Quit [where, whereami] --> gives character current location
# 2) Create a conditional, check if input is "n", "w", "s", "e". If it's not either of these, print an error
# if place is in the choices,


# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
