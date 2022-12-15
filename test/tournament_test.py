import sys
sys.path.append('.')
sys.path.append('../')
import unittest
from app.Tournament import Tournament as t
from app.Player import Player as p

class TournamentTest(unittest.TestCase):

    def test_create_empty_tournament(self):
        test = t()
        self.assertEqual(test.listPlayers, [])
        self.assertEqual(test.listMatch, [])

    def test_create_tounament_with_players(self):
        p1 = p("Jean")
        p2 = p("Jack")
        listPlayers = [p1, p2]
        test = t(listPlayers)
        self.assertEqual(test.listPlayers, listPlayers)
        self.assertEqual(len(test.listPlayers), 2)
