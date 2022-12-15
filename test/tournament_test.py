import sys
from typing import List
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
        test = t()
        test.add_player_to_tournament(p1)
        test.add_player_to_tournament(p2)
        self.assertEqual(test.listPlayers, listPlayers)
        self.assertEqual(len(test.listPlayers), 2)

    def test_add_player_to_tournament(self):
        test_p = p("Johnny")
        test_tournament = t()

        test_tournament.add_player_to_tournament(test_p)
        for (i, j) in zip(test_tournament.listPlayers, [test_p]):
            self.assertEqual(i.nom, j.nom)