# Write a class to hold player information, e.g. what room they are in
# currently.
from colorama import init, Fore
init()


class Player:
    def __init__(self, name, current_room, inventory):
        """
        This is constructor function creates all needed variables for
        instantiation of a new player
        """
        self.name = name
        self.current_room = "outside"
        self.inventory = []

    def set_room(self, current_room):
        self.current_room = current_room

    def add_item(self, item):
        """
        This method adds an item to the player's inventory
        """
        self.inventory.append(item)

    def drop_item(self, item):
        """
        This method removes an item from the player's inventory and drops it in the room
        """
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            print(Fore.RED, "Cannot drop an item that's not in your inventory")

    def print_inventory(self):
        if len(self.inventory) > 0:
            print(Fore.WHITE,  "\n*************************************************")
            print(Fore.MAGENTA, f"\nYour Inventory:")
            for item in self.inventory:
                print(Fore.MAGENTA,
                      f"   * {item.name}: {item.description}")
        else:
            print(Fore.RED, "\nYour inventory is empty")

    def __str__(self):
        """
        Replacement string method for the Player class
        """
        # Method __str__ should return string, not print.
        return f"The player {self.name} is in {self.current_room}"

    def __repr__(self):
        """
        REPR method for the Player class
        """
        return f'Player({repr(self.name)})'
