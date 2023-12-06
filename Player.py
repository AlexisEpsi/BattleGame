

class Player:
    def __init__(self, pV:int, arme, argent:int=20):
        self.pV = pV
        self.arme = arme
        self.argent = argent


    def __str__(self) -> str:
        return f"Pv = {self.pV}\nPa = {self.arme.pA}\nArgent = {self.argent} gallions"
    

    def attaque(self, jAttaquer):
        if jAttaquer.pV > self.arme.pA:
            jAttaquer.pV -= self.arme.pA
        else:
            jAttaquer.pV = 0

    def achat(self, prix:int):
        if self.argent > prix:
            self.argent -= prix
            print("Achat reussi !!!")
            return True
        else:
            print("Vous n'avez pas assez d'argent")
            return False


class Chevalier(Player):
    def __init__(self, pV:int, arme, argent:int=0):
        Player.__init__(self, pV, arme, argent)
    

class Sorcier(Player):
    def __init__(self, pV:int, arme, argent:int=0):
        Player.__init__(self, pV, arme, argent)


class Serpent(Player):
    def __init__(self, pV:int, arme, nom:str):
        super().__init__(pV, arme, nom)
        self.nom = nom
