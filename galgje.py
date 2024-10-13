import random


# Stap 1: Laad woorden uit een tekstbestand
def laad_woorden():
    try:
        with open("woordenlijst.txt", "r") as bestand:
            woorden = bestand.readlines()
            woorden = [woord.strip() for woord in woorden]  # Verwijder eventuele nieuwe regels
        return woorden
    except FileNotFoundError:
        print("Het woordenbestand is niet gevonden!")
        return []


# Stap 2: Kies een willekeurig woord
def kies_willekeurig_woord(woorden):
    return random.choice(woorden).lower()


# Stap 3: Vraag de naam van de gebruiker
def vraag_gebruikersnaam():
    naam = input("Wat is je naam? ")
    return naam


# Stap 4: Start het raadspel
def raadspel(woord):
    goed_geraden = ["_"] * len(woord)  # Maak een lijst voor geraden letters
    pogingen = 5  # Aantal pogingen

    print(f"Welkom bij het spel! Je hebt {pogingen} pogingen om het woord te raden.")

    while pogingen > 0 and "_" in goed_geraden:
        print(f"\nStatus van het woord: {' '.join(goed_geraden)}")
        print(f"Je hebt nog {pogingen} pogingen over.")

        letter = input("Raad een letter: ").lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Voer een enkele letter in!")
            continue

        if letter in goed_geraden:
            print("Deze letter heb je al geraden!")
            continue

        if letter in woord:
            for i in range(len(woord)):
                if woord[i] == letter:
                    goed_geraden[i] = letter
            print(f"Goed gedaan! De letter '{letter}' komt in het woord voor.")
        else:
            pogingen -= 1
            print(f"Helaas, de letter '{letter}' komt niet in het woord voor.")

    if "_" not in goed_geraden:
        print(f"Gefeliciteerd! Je hebt het woord '{woord}' geraden!")
    else:
        print(f"Jammer! Je hebt geen pogingen meer. Het woord was '{woord}'.")


# Stap 5: Hoofdprogramma
def hoofd():
    woorden = laad_woorden()
    if woorden:
        naam = vraag_gebruikersnaam()
        print(f"Hoi {naam}, laten we beginnen!")
        willekeurig_woord = kies_willekeurig_woord(woorden)
        raadspel(willekeurig_woord)
    else:
        print("Kan het spel niet starten zonder woorden.")


# Start het spel
hoofd()
