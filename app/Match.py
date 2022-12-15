import datetime
import sys
sys.path.append('.')
sys.path.append('../')

from app.Player import Player

class Match:

    date : datetime
    player1 : Player
    player2 : Player
    score : int
    lieu : str

    def __init__(self, date : datetime, player1 : Player, player2 : Player):
        self.player1 = player1
        self.player2 = player2
        self.date = date
        self.score = 0
