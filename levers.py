class Levers:
    def __init__(self, pos):
        self.pos = pos
        self.num_pos = len(self.pos)

    def change_pos(self, pos):
        if self.num_pos == len(pos) and max(pos) <= 10:
            self.pos = pos
            print(f"Позиция поменялась. Текущая позиция: {str(self.pos)}")
        else:
            print("Недопустимая позиция")



