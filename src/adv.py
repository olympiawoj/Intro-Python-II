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

n = 0
s = 0
e = 0
w = 0

# TO DO
# Build a function that moves player based on new room
# IF there's no room to the n/s/e/w of the room yu're currently in, don't allow you to move in this


def build_initial_input():
    # print('this is running')
    input_msg = "Enter a direction to move your player:"
    # player.current_room is outside
    # room['outside'].n_to exists
    if room[player.current_room].n_to is not None:
        # print('room', room[player.current_room].n_to)
        input_msg += " n,"
    elif room[player.current_room].s_to is not None:
        input_msg += "s,"
    elif room[player.current_room].e_to is not None:
        input_msg += "e,"
    elif room[player.current_room].w_to is not None:
        input_msg += "w,"
    input_msg += " or q: "

    return input_msg


def eval_room_choices(player_input):
    global n
    global s
    global e
    global w

    new_room = None

    print(f"n: {n}, s: {s}, e: {e}, w: {w}")
    if player_input == "n":
        print("chose n")
        new_room = room[player.current_room].n_to
        # choose room
        print('new room', new_room)
        n += 1
    elif player_input == "s":
        new_room = room[player.current_room].s_to
        print("chose s")
        s += 1
    elif player_input == "e":
        new_room = room[player.current_room].e_to
        print("chose s"),
        e += 1
    elif player_input == "w":
        new_room = room[player.current_room].w_to
        print("chose w")
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

    try:
      # input returns an array of inputs, so we destructure to get the first

        player_input = input(
            "\n" + build_initial_input()).strip().lower().split(' ')
        print('\nthis is the player choice', player_input[0])

        if player_input[0] in room_choices:
            # print("Player input ", player_input)
            eval_room_choices(player_input[0])
        elif player_input[0] == "q":
            print("Goodbye")
            break
        else:
            print("I did not understand that command. Please pick n, s, e, w, or q")

    except:
        print("\nThat is not a valid input.")
        break

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
