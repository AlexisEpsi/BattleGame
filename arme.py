

class Arme:
    def __init__(self, pA:int, nom:str):
        self.pA = pA
        self.nom = nom

class Epee(Arme):
    def __init__(self, pA:int, nom:str, prix:int=0):
        super().__init__(pA, nom)
        self.prix = prix
