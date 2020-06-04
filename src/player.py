# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_location):
        self.name = name
        self.current_location = current_location
    
    def __str__(self):
        return f"{self.name} is currently in {self.current_location}"
    
    def move(self, direction):
        if self.current_location.connections[direction] is not None:
            self.current_location = self.current_location.connections[direction]
        else:
            print("You cannot move in that direction")
