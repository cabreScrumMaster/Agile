import sys
sys.path.append('.')
sys.path.append('../')

class Player:

    nom : str

    def __init__(self, nom) : 
        self.nom = nom