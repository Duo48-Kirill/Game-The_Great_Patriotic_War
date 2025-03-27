import os
import time
import random


class Stalingrad:
    @staticmethod
    def tank() -> bool:
        TANK: str = "🚜"
        WALLS: str = "⬛️"
        NAZI: str = "🦼"
        OPEN_SPACE: str = "🟩"
        print("Передвигайтесь по направлению к нацистам и стреляйте по ним!")
        print("Стрельба может производиться сквозь преграды")
        field: list[list[str]] = [
            ['⬛️','⬛️','⬛️','⬛️','⬛️','⬛️','⬛️','⬛️','⬛️','⬛️','⬛️','⬛️','⬛️','⬛️','⬛️','⬛️','⬛️', '⬛️'],
            ['⬛️','🦼','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','⬛️','🟩','🟩','⬛️','⬛️','⬛️', '⬛️'],
            ['⬛️','🟩','⬛️','🟩','⬛️','🟩','⬛️','🟩','🟩','⬛️','🟩','🟩','🟩','🟩','🟩','🟩','⬛️', '⬛️'],
            ['⬛️','🟩','⬛️','🟩','⬛️','⬛️','⬛️','⬛️','🟩','🟩','🟩','⬛️','⬛️','⬛️','🟩','⬛️','⬛️', '⬛️'],
            ['⬛️','🟩','🟩','🟩','🟩','⬛️','🟩','🟩','🟩','⬛️','⬛️','🟩','🟩','🟩','🟩','⬛️','🟩', '⬛️'],
            ['⬛️','🟩','⬛️','🟩','⬛️','⬛️','🟩','⬛️','🟩','⬛️','⬛️','⬛️','⬛️','⬛️','🟩','⬛️','🟩', '⬛️'],
            ['⬛️','🟩','🟩','🟩','🟩','⬛️','🟩','⬛️','🦼','🟩','🟩','🟩','🟩','⬛️','🟩','🟩','🟩', '⬛️'],
            ['⬛️','🟩','⬛️','⬛️','⬛️','⬛️','🟩','🟩','🟩','⬛️','🟩','🟩','🟩','⬛️','🟩','⬛️','🟩', '⬛️'],
            ['⬛️','🟩','🟩','🟩','⬛️','🟩','🟩','⬛️','🟩','⬛️','⬛️','🟩','🟩','⬛️','🟩','⬛️','⬛️', '⬛️'],
            ['⬛️','⬛️','⬛️','🟩','🟩','🟩','⬛️','⬛️','🟩','🟩','⬛️','⬛️','🟩','⬛️','🟩','🟩','⬛️', '⬛️'],
            ['⬛️','⬛️','🟩','🟩','⬛️','🟩','🟩','⬛️','🟩','⬛️','⬛️','🟩','🟩','🟩','🟩','⬛️','⬛️', '⬛️'],
            ['⬛️','⬛️','⬛️','🟩','⬛️','⬛️','🟩','⬛️','🟩','⬛️','🟩','🟩','⬛️','⬛️','🟩','🟩','🟩', '⬛️'],
            ['⬛️','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','⬛️','🟩','🟩','⬛️','🟩','🟩','⬛️','🟩', '⬛️'],
            ['⬛️','🟩','⬛️','⬛️','⬛️','⬛️','⬛️','🟩','⬛️','⬛️','⬛️','🟩','⬛️','⬛️','🟩','⬛️','🟩', '⬛️'],
            ['⬛️','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','🟩','⬛️','🟩','⬛️','🟩', '⬛️'],
            ['⬛️','🟩','⬛️','🟩','⬛️','🟩','⬛️','⬛️','⬛️','⬛️','🟩','🟩','⬛️','🟩','🟩','⬛️','🟩', '⬛️'],
            ['⬛️','🟩','⬛️','🟩','🟩','🟩','⬛️','🟩','🟩','🟩','🟩','⬛️','⬛️','🟩','⬛️','🚜','🟩', '⬛️'],
            ['⬛️','⬛️','⬛️','⬛️','⬛️','⬛️','⬛️','⬛️','⬛️','⬛️','⬛️','⬛️','⬛️','⬛️','⬛️','⬛️','⬛️', '⬛️']
        ]

        coordinate_x: int = 15
        coordinate_y: int = 16
        tank_armor: int = 100

        while True:
            for row in field:
                print("".join(row))

            for y, row in enumerate(field):
                for x, item in enumerate(row):
                    if item == TANK:
                        coordinate_x: int = x
                        coordinate_y: int = y

            print('Управление танком на "WASD"')
            print('Дать добро на выстрел на "E"')
            print(f"Прочность танка = {tank_armor}")
            if tank_armor < 100 and tank_armor > 0:
                print("Внимание, ваша броня повреждена!")

            action: str = input(">> ").lower()

            shot_a_nazi: bool = False
            nazi_in_radius: bool = False
            if action == "e":
                for i in range(coordinate_y - 4, coordinate_y + 5):
                    if i >= 0 and i <= 17:
                        if field[i][coordinate_x] == NAZI:
                            nazi_in_radius: bool = True
                            nazi_coordinate_y: int = i
                            nazi_coordinate_x: int = coordinate_x
                            break

                if nazi_in_radius != True:
                    for j in range(coordinate_x - 4, coordinate_x + 5):
                        if j >= 0 and j <= 17:
                            if field[coordinate_y][j] == NAZI:
                                nazi_in_radius: bool = True
                                nazi_coordinate_x: int = j
                                nazi_coordinate_y: int = coordinate_y
                                break

                if coordinate_y == nazi_coordinate_y:
                    for i in range(
                        min(coordinate_x, nazi_coordinate_x),
                        max(coordinate_x, nazi_coordinate_x),
                    ):
                        if field[coordinate_y][i] == WALLS:
                            break
                        else:
                            shot_a_nazi:bool = True
                            field[nazi_coordinate_y][nazi_coordinate_x] = OPEN_SPACE
                            break

                elif coordinate_x == nazi_coordinate_x:
                    for i in range(
                        min(coordinate_y, nazi_coordinate_y),
                        max(coordinate_y, nazi_coordinate_y),
                    ):
                        if field[i][coordinate_x] == WALLS:
                            break
                        else:
                            shot_a_nazi: bool = True
                            field[nazi_coordinate_y][nazi_coordinate_x] = OPEN_SPACE
                            break
                if shot_a_nazi == False:
                    print("Промах!")
                    time.sleep(2)

            if action == "s":
                item = field[coordinate_y + 1][coordinate_x]
                if item != WALLS and item != NAZI:
                    field[coordinate_y + 1][coordinate_x] = TANK
                    field[coordinate_y][coordinate_x] = OPEN_SPACE
                    coordinate_y += 1

            if action == "w":
                item = field[coordinate_y - 1][coordinate_x]
                if item != WALLS and item != NAZI:
                    field[coordinate_y - 1][coordinate_x] = TANK
                    field[coordinate_y][coordinate_x] = OPEN_SPACE
                    coordinate_y -= 1

            if action == "a":
                item = field[coordinate_y][coordinate_x - 1]
                if item != WALLS and item != NAZI:
                    field[coordinate_y][coordinate_x - 1] = TANK
                    field[coordinate_y][coordinate_x] = OPEN_SPACE
                    coordinate_x -= 1

            if action == "d":
                item = field[coordinate_y][coordinate_x + 1]
                if item != WALLS and item != NAZI:
                    field[coordinate_y][coordinate_x + 1] = TANK
                    field[coordinate_y][coordinate_x] = OPEN_SPACE
                    coordinate_x += 1

            is_NAZI: bool = False
            for row in field:
                if NAZI in row:
                    is_NAZI: bool = True
                    break
            if not is_NAZI:
                os.system("cls")
                for row in field:
                    print("".join(row))
                print("Поздравляю! Вы уничтожили все танки противников!")
                return 1

            nazis = []
            for y, row in enumerate(field):
                for x, item in enumerate(row):
                    if item == NAZI:
                        nazis.append((y, x))

            for y, x in nazis:
                nazi_coordinate_y: int = y
                nazi_coordinate_x: int = x

                tank_in_radius = False
                for i in range(nazi_coordinate_y - 4, nazi_coordinate_y + 5):
                    if i >= 0 and i <= 17:
                        if field[i][nazi_coordinate_x] == TANK:
                            tank_in_radius:bool = True
                            tank_coordinate_y: int = i
                            tank_coordinate_x: int = nazi_coordinate_x
                            break

                if tank_in_radius != True:
                    for j in range(nazi_coordinate_x - 4, nazi_coordinate_x + 5):
                        if j >= 0 and j <= 17:
                            if field[nazi_coordinate_y][j] == TANK:
                                tank_in_radius:bool = True
                                tank_coordinate_x: int = j
                                tank_coordinate_y: int = nazi_coordinate_y
                                break

                if tank_in_radius == True:
                    if tank_coordinate_y == nazi_coordinate_y:
                        for i in range(
                            min(tank_coordinate_x, nazi_coordinate_x),
                            max(tank_coordinate_x, nazi_coordinate_x),
                        ):
                            if field[coordinate_y][i] == WALLS:
                                break
                            else:
                                tank_armor -= 50
                                break

                    elif tank_coordinate_x == nazi_coordinate_x:
                        for i in range(
                            min(tank_coordinate_y, nazi_coordinate_y),
                            max(tank_coordinate_y, nazi_coordinate_y),
                        ):
                            if field[i][coordinate_x] == WALLS:
                                break
                            else:
                                tank_armor -= 50
                                break

                else:
                    nazi_action = random.randint(1, 4)
                    if nazi_action == 1:
                        item = field[nazi_coordinate_y + 1][nazi_coordinate_x]
                        if item != WALLS and item != NAZI:
                            field[nazi_coordinate_y + 1][nazi_coordinate_x] = NAZI
                            field[nazi_coordinate_y][nazi_coordinate_x] = OPEN_SPACE
                            nazi_coordinate_y += 1
                            break

                    if nazi_action == 2:
                        item = field[nazi_coordinate_y - 1][nazi_coordinate_x]
                        if item != WALLS and item != NAZI:
                            field[nazi_coordinate_y - 1][nazi_coordinate_x] = NAZI
                            field[nazi_coordinate_y][nazi_coordinate_x] = OPEN_SPACE
                            nazi_coordinate_y -= 1
                            break

                    if nazi_action == 3:
                        item = field[nazi_coordinate_y][nazi_coordinate_x - 1]
                        if item != WALLS and item != NAZI:
                            field[nazi_coordinate_y][nazi_coordinate_x - 1] = NAZI
                            field[nazi_coordinate_y][nazi_coordinate_x] = OPEN_SPACE
                            nazi_coordinate_x -= 1
                            break

                    if nazi_action == 4:
                        item = field[nazi_coordinate_y][nazi_coordinate_x + 1]
                        if item != WALLS and item != NAZI:
                            field[nazi_coordinate_y][nazi_coordinate_x + 1] = NAZI
                            field[nazi_coordinate_y][nazi_coordinate_x] = OPEN_SPACE
                            nazi_coordinate_x += 1
                            break

            if tank_armor <= 0:
                os.system("cls")
                for row in field:
                    print("".join(row))

                print("Ваш танк был уничтожен")
                time.sleep(2)
                os.system("cls")
                print("Попробуйте заново!")
                Stalingrad.tank()

            os.system("cls")