import unittest
from src.player import Player


class PlayerTest(unittest.TestCase):
    
    def setUp(self): 
        self.user_1 = Player("Bob", "Rock")
        self.user_2 = Player("John", "Paper")

    def test_check_user_name(self):
        self.assertEqual("Bob", self.user_1.name)

    def test_check_user_gesture(self):
        self.assertEqual("Rock", self.user_1.gesture)