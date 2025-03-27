import time


class Ending:
    def first_end(name: str) -> None:
        file: list[str] = open("mechanics/end/end_1.txt", encoding="utf-8").readlines()
        for line in file:
            line: str = line.replace("Алексей", name)
            print(line)
            time.sleep(3)

    def second_end(name: str) -> None:
        file: list[str] = open("mechanics/end/end_2.txt", encoding="utf-8").readlines()
        for line in file:
            line: str = line.replace("Алексей", name)
            print(line)
            time.sleep(3)
