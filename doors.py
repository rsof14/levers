from door import Door


class Doors:
    def __init__(self):
        self.doors = []

    def add_door(self, pos):
        self.doors.append(str(Door(len(self.doors) + 1, pos).pos))
