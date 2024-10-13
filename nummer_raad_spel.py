import random

getal = random.randint(1, 10)


max_pogingen = 3
print(f"Je mag {max_pogingen} keer raden om het juiste getal tussen 1 en 10 te vinden.")


for poging in range(1, max_pogingen + 1):
    kans = int(input(f"Poging {poging}: Raad het juiste getal: "))

    if kans == getal:
        print("Goed gedaan,je hebt het juiste getal geraden!")
        break
    resterende_pogingen = max_pogingen - poging
    if resterende_pogingen > 0:
        print(f"Je hebt nog {resterende_pogingen} poging over.")
    else:
        print(f"Helaas, je hebt geen pogingen meer. Het juiste getal was {getal}.")

