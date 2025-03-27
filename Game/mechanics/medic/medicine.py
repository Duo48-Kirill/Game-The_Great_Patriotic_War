import os


class Bullet_wound:
    def wound() -> int:
        SKIN: str = "🟨"
        CLOTHES: str = "⬛"
        CUT: str = "🟥"
        WOUND: str = "🛑"
        BLOOD: str = "🟧"
        BANDAGE: str = "🔘"
        print("Обработайте пулевое ранение, при этом убрав всю кровь!")

        arm: list[list[str]] = [
            ['⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛'],
            ['⬛','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','⬛'],
            ['⬛','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','⬛'],
            ['⬛','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟧','🟧','🟧','🟨','🟨','🟨','⬛'],
            ['⬛','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟧','🟧','🟥','🟧','🟧','🟨','🟨','⬛'],
            ['⬛','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟧','🟥','🛑','🟥','🟧','🟨','🟨','⬛'],
            ['⬛','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟧','🟥','🟥','🟥','🟧','🟨','🟨','⬛'],
            ['⬛','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟧','🟧','🟥','🟧','🟧','🟨','🟨','⬛'],
            ['⬛','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟧','🟧','🟧','🟧','🟨','🟨','⬛'],
            ['⬛','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟧','🟧','🟨','🟨','🟨','⬛'],
            ['⬛','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟧','🟧','🟨','🟨','🟨','⬛'],
            ['⬛','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟧','🟨','🟨','🟨','🟨','⬛'],
            ['⬛','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟧','🟨','🟨','🟨','🟨','⬛'],
            ['⬛','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','⬛'],
            ['⬛','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','⬛'],
            ['⬛','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','⬛'],
            ['⬛','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','⬛'],
            ['⬛','🟨','🟨','🔘','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','⬛'],
            ['⬛','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','⬛'],
            ['⬛','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','🟨','⬛'],
            ['⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛','⬛']]

        coordinate_x: int = 0
        coordinate_y: int = 0

        while True:
            game_end: int = 2
            for row in arm:
                print("".join(row))

                if CUT in row or BLOOD in row or WOUND in row:
                    game_end: int = 1
                    if WOUND in row:
                        game_end: int = 0

            if game_end == 2:
                print('Теперь нажмите "E", чтобы заткнуть отверстие')
                action: str = input(">> ").lower()
                if action == "e":
                    print("Поздравляю, рана успешно обработана!")
                    return 2

            for y, row in enumerate(arm):
                for x, item in enumerate(row):
                    if item == BANDAGE:
                        coordinate_x: int = x
                        coordinate_y: int = y

            print('Движение бинта на "WASD"')
            print('Заткнуть отверстие на "E"')

            action: str = input(">> ").lower()

            if action == "e":
                print(
                    "Рана не была полностью обработана, Михаил умирает из-за заражения!"
                )
                return 1

            if action == "s":
                item = arm[coordinate_y + 1][coordinate_x]
                if item != CLOTHES:
                    arm[coordinate_y + 1][coordinate_x] = BANDAGE
                    arm[coordinate_y][coordinate_x] = SKIN

            if action == "w":
                item = arm[coordinate_y - 1][coordinate_x]
                if item != CLOTHES:
                    arm[coordinate_y - 1][coordinate_x] = BANDAGE
                    arm[coordinate_y][coordinate_x] = SKIN

            if action == "a":
                item = arm[coordinate_y][coordinate_x - 1]
                if item != CLOTHES:
                    arm[coordinate_y][coordinate_x - 1] = BANDAGE
                    arm[coordinate_y][coordinate_x] = SKIN

            if action == "d":
                item = arm[coordinate_y][coordinate_x + 1]
                if item != CLOTHES:
                    arm[coordinate_y][coordinate_x + 1] = BANDAGE
                    arm[coordinate_y][coordinate_x] = SKIN

            os.system("cls")