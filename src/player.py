# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = "outside"

    def __str__(self):
        # Method __str__ should return string, not print.
        return f"The player {self.name} is in {self.current_room}"

    def __repr__(self):
        return f'Player({repr(self.name)})'
