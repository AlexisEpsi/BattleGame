from Player import Player
from Player import Chevalier
from Player import Sorcier
from Player import Serpent
from arme import Arme
from arme import Epee

print("Bienvenue dans la contrée ancienne de l'EPSI en 1321...")


achats = [Epee(1, "Epee simple", 0), Epee(3, "Epee modifié", 10), Epee(100, "Epee legendaire", 100)]

chevalier = Chevalier(50, achats[0], 1000)
sorcier = Sorcier(20, achats[1])
serpent = Serpent(500, Arme(20, "dent de serpent"), "serpent")


while serpent.pV != 0 and chevalier.pV != 0:

    cmd = input("Que voulez vous faire ? ")

    if cmd.lower() == "attaque":
        chevalier.attaque(serpent)
        print(serpent.pV)

    elif cmd.lower() == "achat":
        for produit in achats:
            print(f"{produit.nom} est au prix de {produit.prix}")

        cmd = int(input("Que voulez-vous acheté ? "))

        if cmd > 0 and cmd <= len(achats):
            if chevalier.achat(achats[cmd - 1].prix):
                chevalier.arme = achats[cmd - 1]
    
    elif cmd.lower() == "spec":
        print(chevalier)


print("Bien jouer vous avez gagné. :D")
