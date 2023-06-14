import random


def demander_nombre(nb_min, nb_max):
    nombre_int = 0
    while nombre_int == 0:
        nombre_str = input(f"quel est le nombre magique (entre {nb_min} et {nb_max}) ?")
        try:
            nombre_int = int(nombre_str)
        except:
            print("ERREUR: Vous devez rentrer un nombre. Réessayez ")
        else:
            if nombre_int < nb_min or nombre_int > nb_max:
                print(f"ERREUR: Le nombre doit etre entre {nb_min} et {nb_max}. Réessayez")
                nombre_int = 0

    return nombre_int


NOMBRE_MIN = 0
NOMBRE_MAX = 57
NOMBRE_MAGIQUE = random.randint(NOMBRE_MIN, NOMBRE_MAX)
NB_VIES = 5

"""nombre = 0
vies = NB_VIES
while not nombre == NOMBRE_MAGIQUE and vies > 0:
    print(f"Il vous reste {vies} vies")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print("Bravo, vous avez gagné")
    elif nombre > NOMBRE_MAGIQUE:
        print("le nombre magique est plus petit")
        vies -= 1
    else:
        print("le nombre magique est le plus grand ")
        vies -= 1

if vies == 0:
    print(f"Vous avez perdu! le nombre magique etait: {NOMBRE_MAGIQUE}")"""


gagne = False
for i in range(0, NB_VIES):
    vies = NB_VIES-i
    print(f"Il vous reste {vies} vies")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre == NOMBRE_MAGIQUE:
        print("Bravo, vous avez gagné")
        gagne = True
        break
    elif nombre > NOMBRE_MAGIQUE:
        print("le nombre magique est plus petit")
    else:
        print("le nombre magique est le plus grand ")

if not gagne:
    print(f"Vous avez perdu! le nombre magique etait: {NOMBRE_MAGIQUE}")