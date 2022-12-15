import array
import sys
from typing import List
sys.path.append('.')
sys.path.append('../')

from app.Match import Match
from app.Player import Player

class Tournament  : 

    def __init__(self):
        self.listPlayers = []
        self.listMatch = []
    
    
    def add_player_to_tournament(self, player):
        self.listPlayers.append(player)