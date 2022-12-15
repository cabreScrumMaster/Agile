import sys
sys.path.append('.')
sys.path.append('../')
import unittest
from app.Tournament import Tournament as t

class TournamentTest(unittest.TestCase):

    def test_create_empty_tournament(self):
        test = t()
        self.assertEqual(test.listPlayers, [])
        self.assertEqual(test.listMatch, [])
