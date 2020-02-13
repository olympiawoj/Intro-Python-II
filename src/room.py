# Implement a class to hold room information. This should have name and
# description attributes.

from colorama import init, Fore
init()


class Room:
    def __init__(self, name, description, item_list):
        self.name = name
        self.description = description
        self.item_list = item_list

    """TODO - player needs to be able to pick up items, dro pitems"""

    def print_items(self):
        """
        Prints all items in the room's item_list
        """
        for item in self.item_list:
            print(item)

    # I want to remove an item from a room
    def remove_item(self, item):
        # loop over item_list dict
        print('removing working')
        if item in self.item_list:
            print('in here', item)
            self.item_list.remove(item)
            print(Fore.MAGENTA, f"{item} removed from Room")

    def __str__(self):
        return f'Room: {self.name}, Description: {self.description}'

    def __repr__(self):
        return f'Room({repr(self.name)})'
