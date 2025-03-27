import os


class Sniper:
    def shooting() -> bool:
        RED_DOT: str = "📍"
        BORDER: str = "⬛️"
        NAZI: str = "👨"
        GRASS: str = "🟩"
        print("Найдите и выстрелите в нациста!")

        aim: list[list[str]] = [
            ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
            ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","🟩","🟩","🟩","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
            ["⬛️","⬛️","⬛️","⬛️","🟩","🟩","🟩","🟩","🟩","🟩","🟩","⬛️","⬛️","⬛️","⬛️"],
            ["⬛️","⬛️","⬛️","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","⬛️","⬛️","⬛️"],
            ["⬛️","⬛️","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","⬛️","⬛️"],
            ["⬛️","⬛️","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","⬛️","⬛️"],
            ["⬛️","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","👨","🟩","🟩","⬛️"],
            ["⬛️","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","⬛️"],
            ["⬛️","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","⬛️"],
            ["⬛️","🟩","🟩","🟩","🟩","🟩","🟩","📍","🟩","🟩","🟩","🟩","🟩","🟩","⬛️"],
            ["⬛️","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","⬛️"],
            ["⬛️","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","⬛️"],
            ["⬛️","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","⬛️"],
            ["⬛️","⬛️","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","⬛️","⬛️"],
            ["⬛️","⬛️","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","⬛️","⬛️"],
            ["⬛️","⬛️","⬛️","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","🟩","⬛️","⬛️","⬛️"],
            ["⬛️","⬛️","⬛️","⬛️","🟩","🟩","🟩","🟩","🟩","🟩","🟩","⬛️","⬛️","⬛️","⬛️"],
            ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","🟩","🟩","🟩","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
            ["⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️","⬛️"],
        ]

        coordinate_x: int = 0
        coordinate_y: int = 0

        while True:
            game_end: bool = True
            for row in aim:
                print("".join(row))

                if NAZI in row:
                    game_end: bool = False

            if game_end:
                print('Нажмите "E", для выстрела')
                action: str = input(">> ").lower()
                if action == "e":
                    print("Враг убит!")
                    return 1

            for y, row in enumerate(aim):
                for x, item in enumerate(row):
                    if item == NAZI:
                        coordinate_x: int = x
                        coordinate_y: int = y

            print('Управление прицелом на "WASD"')
            print('Сделать выстрел на "E"')

            action: str = input(">> ").lower()

            if action == "e":
                print("Вас обнаружили и убили!")
                return 0

            if action == "w":
                item = aim[coordinate_y + 1][coordinate_x]
                if (item != BORDER) and (item != RED_DOT):
                    aim[coordinate_y + 1][coordinate_x] = NAZI
                    aim[coordinate_y][coordinate_x] = GRASS
                elif item == RED_DOT:
                    aim[coordinate_y + 1][coordinate_x] = RED_DOT
                    aim[coordinate_y][coordinate_x] = GRASS

            if action == "s":
                item = aim[coordinate_y - 1][coordinate_x]
                if (item != BORDER) and (item != RED_DOT):
                    aim[coordinate_y - 1][coordinate_x] = NAZI
                    aim[coordinate_y][coordinate_x] = GRASS
                elif item == RED_DOT:
                    aim[coordinate_y - 1][coordinate_x] = RED_DOT
                    aim[coordinate_y][coordinate_x] = GRASS

            if action == "d":
                item = aim[coordinate_y][coordinate_x - 1]
                if (item != BORDER) and (item != RED_DOT):
                    aim[coordinate_y][coordinate_x - 1] = NAZI
                    aim[coordinate_y][coordinate_x] = GRASS
                elif item == RED_DOT:
                    aim[coordinate_y][coordinate_x - 1] = RED_DOT
                    aim[coordinate_y][coordinate_x] = GRASS

            if action == "a":
                item = aim[coordinate_y][coordinate_x + 1]
                if (item != BORDER) and (item != RED_DOT):
                    aim[coordinate_y][coordinate_x + 1] = NAZI
                    aim[coordinate_y][coordinate_x] = GRASS
                elif item == RED_DOT:
                    aim[coordinate_y][coordinate_x + 1] = RED_DOT
                    aim[coordinate_y][coordinate_x] = GRASS

            os.system("cls")