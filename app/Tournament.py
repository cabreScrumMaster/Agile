import sys
from typing import List
sys.path.append('.')
sys.path.append('../')

class Tournament  : 

    def __init__(self):
        self.listPlayers = []
        self.listMatch = []

    def add_player_to_tournament(self, player):
        self.listPlayers.append(player)
    
    def destroy(self):
        self.listPlayers = None
        self.listMatch = None
        print("Tournament destroyed")

    