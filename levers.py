from lever import Lever


class Levers:
    def __init__(self):
        self.levers = ""

    def add_lever(self, pos):
        self.levers += str(Lever(len(self.levers) + 1, pos).pos)
