# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        """
        This is constructor function creates all needed variables for
        instantiation of a new player
        """
        self.name = name
        self.current_room = "outside"

    def set_room(self, current_room):
        self.current_room = current_room

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
