# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, item_list):
        self.name = name
        self.description = description
        self.item_list = item_list

    def print_items(self):
        """
        Prints all items in the room's item_list
        """
        for item in self.item_list:
            print(item)

    def __str__(self):
        return f'Room: {self.name}, Description: {self.description}'

    def __repr__(self):
        return f'Room({repr(self.name)})'
