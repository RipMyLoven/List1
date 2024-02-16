﻿import random
import time

raha = 100  # Alguses on mängijal 100 eurot

print("Tere tulemast kasiinosse!")
print("Siin kasiinos on mäng, kus võitmine on võimatu.")

while raha >= 10:  # Mäng jätkub seni, kuni mängijal on vähemalt 10 eurot

    print(f"\nTeil on hetkel {raha} eurot.")

    while True:
        try:
            panus = int(input("Palun sisestage oma panus (vähemalt 10 eurot): "))
            if panus < 10:
                raise ValueError("Panus peab olema vähemalt 10 eurot!")
            if panus > raha:
                raise ValueError("Teil pole piisavalt raha selle panuse tegemiseks!")
            break
        except ValueError as ve:
            print(ve)

    print("Pöörutan ratast...")
    time.sleep(1)  # Ootame 1 sekund enne tulemuse kuvamist

    # Simuleerime ratta pööramist
    varv = random.randint(1, 10)

    # Näitame ratta pöörlemist
    for frame_number in range(5):
        if frame_number == 0:
            print("|   |   |   |", end="\r")
        elif frame_number == 1:
            print("| {} |   |   |".format(varv), end="\r")
        elif frame_number == 2:
            print("| {} | {} |   |".format(varv, varv), end="\r")
        elif frame_number == 3:
            print("| {} | {} | {} |".format(varv, varv, varv), end="\r")
        elif frame_number == 4:
            print("| {} | {} | {} |".format(varv, varv, varv), end="\r")

        time.sleep(0.5)  # Ootame enne järgmise kaadri kuvamist

    # Näitame tulemust järk-järgult
    print("\nTeie number on:", end=" ")
    for i in range(1, varv + 1):
        print(i, end=" ", flush=True)
        time.sleep(0.5)
    print()

    # Mängijaraha uuendamine vastavalt tulemusele
    if varv == 10:
        print("Te võitsite!")
        raha += panus
    else:
        print("Te kaotasite!")
        # Simuleerime juhuslikud numbrid enne lõpliku tulemuse kuvamist
        for i in range(varv + 1, 10):
            print(i, end=" ", flush=True)
            time.sleep(0.5)
        print()
        raha -= panus

print("Teil ei ole piisavalt raha, et mängida. Aitäh mängimast! Teie järel olev summa on", raha, "eurot.")
