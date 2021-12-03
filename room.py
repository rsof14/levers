from door import Door
from levers import Levers


class Room:
    def __init__(self):
        self.doors = []
        self.opened_doors = []

    def add_door(self, door: Door):
        door.num = len(self.doors) + 1
        self.doors.append(door)

    def print_room(self):
        for door in self.doors:
            print(f"Дверь №{door.num} {'открыта' if door.opened else 'закрыта'}")

    def try_to_open(self, position: Levers):
        flag = False
        for door in self.doors:
            if door.pos == position.pos and door.opened is False:
                door.opened = True
                self.opened_doors.append(door)
                flag = True
                print(f"Открылась дверь №{door.num}")
        if flag is False:
            print("Комбинация не открыла ни одну дверь")
        if len(self.opened_doors) != 0:
            print("Открыты двери №", end=' ')
            for door in self.opened_doors:
                print(door.num, end=' ')
            print()
