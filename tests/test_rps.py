import unittest
from src.rps import Rps
from src.player import Player

class RockPaperScissorTest(unittest.TestCase):
    def setUp(self): 
        self.user_1 = Player("Bob", "Rock")
        self.user_2 = Player("John", "Paper")
        self.game_1 = Rps(self.user_1, self.user_2)
    
    def test_game_has_players(self):
        self.assertEqual(self.user_1, self.game_1.player_1)