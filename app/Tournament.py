import array
import sys
sys.path.append('.')
sys.path.append('../')

from app.Match import Match
from app.Player import Player

class Tournament  : 

    listPlayers : Player
    listMatch : Match

    def __init__(self, listPlayer = [] ):
        self.listPlayers = listPlayer
        self.listMatch = []