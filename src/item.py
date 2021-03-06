
from colorama import init, Fore
init()
'''
* Create a file called `item.py` and add an `Item` class in there.

  * The item should have `name` and `description` attributes.

     * Hint: the name should be one word for ease in parsing later.

  * This will be the _base class_ for specialized item types to be declared
    later.


'''


class Item:
    def __init__(self, name, description):
        """
        This constructor function creates all needed variables to instantiate a new Item
        """
        self.name = name
        self.description = description

    def on_take(self):
        """
        Used to perform logic when item is picked up by player
        """
        print(Fore.MAGENTA + f"\nYou have picked up the item: {self.name}!")
        print()

    def on_drop(self):
        """
        Used to perform logic when item is dropped by player
        """
        print(Fore.MAGENTA, f"\nYou have dropped {self.name} item!")
        print()

    def __str__(self):
        """
        Replacement string for Item class
        """
        return f"Item: {self.name}, Description: {self.description}"

    def __repr__(self):
        """
        REPR method for the Item class
        """
        return f'Item({repr(self.name), {repr(self.description)}})'
