from levers import Levers
from doors import Doors

if __name__ == "__main__":
    n = int(input("Введите число рычагов "))
    m = int(input("Введите число дверей "))
    levers = Levers()
    doors = Doors()
    for i in range(m):
        pos = int(input(f"Введите комбинацию позиций рычагов для открытия двери №{i+1} "))
        doors.add_door(pos)
    for i in range(n):
        pos = int(input(f"Введите позицию для рычага №{i+1} "))
        levers.add_lever(pos)
    if levers.levers not in doors.doors:
        print("Все двери закрыты")
    else:
        i = 1
        for door in doors.doors:
            if door == levers.levers:
                print("Открыта дверь №", i)
            i += 1





