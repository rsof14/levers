from levers import Levers
from room import Room
from door import Door

if __name__ == "__main__":
    room = Room()
    room.add_door(Door(1, [1, 3, 4]))
    room.add_door(Door(2, [3, 2, 1]))
    room.add_door(Door(3, [2, 1, 3]))
    room.print_room()
    position = Levers([3, 2, 1])
    room.try_to_open(position)
    room.print_room()
    position.change_pos([1, 3, 4])
    room.try_to_open(position)
    room.print_room()
    position.change_pos([2, 3, 4, 1])
    position.change_pos([2, 3, 11])
    position.change_pos([2, 2, 2])
    room.try_to_open(position)
    room.print_room()


