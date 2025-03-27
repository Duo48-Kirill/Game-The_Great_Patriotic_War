import time  # Импорт всех необходимых библиотек и классов из других файлов
import os
from playsound import playsound
from mechanics.name import male_names, female_names
from mechanics.end.final import Ending
from mechanics.snipe.sniper_rifle import Sniper
from mechanics.tank.tank import Stalingrad
from mechanics.medic.medicine import Bullet_wound

name: str = input("Введите ваше имя: ").capitalize()
if (
    name == False
    or name in female_names
    or name==""
    or (name[-1] in "ая" and name not in male_names)
):  # Если имя пустое, то по стандарту оно будет являться Алексеем
    name: str = "Алексей"
    print("Извините, у нас есть подозрение, что у вас женское имя или оно пустое")
    time.sleep(1)
    print(
        'Этот фактор будет мешать восприятию истории, поэтому, имя останется "Алексей"'
    )
time.sleep(2)

start: str = input("Нажмите любую клавишу, для того чтобы начать ")
if start == "":
    start: str = "start"  # Главное прожать Enter, не важно, что вы введете

if start:
    file: list[str] = open(
        "mechanics/plot.txt", encoding="utf-8"
    ).readlines()  # Открытие файла с повествованием

    for line in file:
        line: str = line.replace(
            "Алексей", name
        )  # Замена имени, на то которое ввели вы

        if line == "stuk\n":  # Включение звуков в определенных моментах
            playsound("mechanics/music/Knock.mp3")
        elif line == "step\n":
            playsound("mechanics/music/Step.mp3")
        elif line == "kettle\n":
            playsound("mechanics/music/Kettle.mp3")
        elif line == "cry\n":
            playsound("mechanics/music/Cry.mp3")
        elif line == "cough\n":
            playsound("mechanics/music/Cough.mp3")
        elif line == "bird\n":
            playsound("mechanics/music/Bird.mp3")
        elif line == "molotov\n":
            playsound("mechanics/music/Molotov.mp3")
        elif line == "plane\n":
            playsound("mechanics/music/Plane.mp3")
        elif line == "teapot\n":
            playsound("mechanics/music/Teapot.mp3")
        elif line == "metal\n":
            playsound("mechanics/music/Metal.mp3")
        elif line == "gun\n":
            playsound("mechanics/music/Gun.mp3")
        elif line == "machine_gun\n":
            playsound("mechanics/music/Machine_gun.mp3")

        elif line == "sniper\n":
            shot: bool = Sniper.shooting()  # Механика стрельбы
            playsound("mechanics/music/Sniper.mp3")
            while shot == 0:
                shot: bool = Sniper.shooting()
                playsound("mechanics/music/Sniper.mp3")  # Звук выстрела винтовки
                os.system("cls")
            os.system("cls")
        elif line == "tank\n":
            Stalingrad.tank()  # Механика танка
            playsound("mechanics/music/Tank.mp3")
            os.system("cls")
        elif line == "medicine\n":
            result: int = Bullet_wound.wound()  # Механика спасения товарища
            if result == 2:
                playsound("mechanics/music/Bandage.mp3")
            os.system("cls")

        elif line == "final":
            if result == 1:
                Ending.first_end(name)
            else:  # Финал с двумя концовками, смотря, спасли ли вы товарища или же нет
                Ending.second_end(name)

        else:
            time.sleep(3)
            print(line)  # Обычный вывод строк с повествованием
