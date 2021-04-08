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

    def test_no_winner_at_start(self):
        self.assertEqual(None, self.game_1.winner)

    def test_winner_player_name(self):
        self.game_1.set_the_winner(self.user_1)
        self.assertEqual(self.user_1, self.game_1.winner)
    
    def test_player_gestures_passed_to_game(self):
        self.assertEqual(self.user_1.gesture, self.game_1.player_1.gesture)

    def test_player_draw(self):
        self.assertEqual("tie", self.game_1.test_result("Rock", "Rock")) 
    
    def test_player_1_wins_with_rock(self):
        self.assertEqual("Bob wins", self.game_1.test_result("Rock", "Scissors"))
    
    def test_player_1_wins_with_paper(self):
        self.assertEqual("Bob wins", self.game_1.test_result("Paper", "Rock"))

    def test_player_2_wins_with_rock(self):
        self.assertEqual("John wins", self.game_1.test_result("Scissors", "Rock"))
    
    def test_player_2_wins_with_paper(self):
        self.assertEqual("John wins", self.game_1.test_result("Rock", "Paper"))


# EXTENSIONS:
    def test_player_1_wins_scissors_paper(self):
        self.assertEqual("Bob wins", self.game_1.test_result("Scissors", "Paper"))

    def test_player_2_wins_scissors_paper(self):
        self.assertEqual("John wins", self.game_1.test_result("Paper", "Scissors"))

    def test_player_1_wins_rock_lizard(self):
        self.assertEqual("Bob wins", self.game_1.test_result("Rock", "Lizard"))

    def test_player_2_wins_Lizard_Rock(self):
        self.assertEqual("John wins", self.game_1.test_result("Lizard", "Rock"))

    def test_player_1_wins_lizard_spock(self):
        self.assertEqual("Bob wins", self.game_1.test_result("Lizard", "Spock"))

    def test_player_2_wins_Spock_Lizard(self):
        self.assertEqual("John wins", self.game_1.test_result("Spock", "Lizard"))

    def test_player_1_wins_spock_scissors(self):
        self.assertEqual("Bob wins", self.game_1.test_result("Spock", "Scissors"))

    def test_player_2_wins_Scissor_Spock(self):
        self.assertEqual("John wins", self.game_1.test_result("Scissors", "Spock"))

    def test_player_1_wins_scissors_lizard(self):
        self.assertEqual("Bob wins", self.game_1.test_result("Scissors", "Lizard"))

    def test_player_2_wins_Lizard_Scissors(self):
        self.assertEqual("John wins", self.game_1.test_result("Lizard", "Scissors"))

    def test_player_1_wins_lizard_paper(self):
        self.assertEqual("Bob wins", self.game_1.test_result("Lizard", "Paper"))

    def test_player_2_wins_Paper_Lizard(self):
        self.assertEqual("John wins", self.game_1.test_result("Paper", "Lizard"))

    def test_player_1_wins_paper_spock(self):
        self.assertEqual("Bob wins", self.game_1.test_result("Paper", "Spock"))

    def test_player_2_wins_Spock_Paper(self):
        self.assertEqual("John wins", self.game_1.test_result("Spock", "Paper"))

    def test_player_1_wins_spock_rock(self):
        self.assertEqual("Bob wins", self.game_1.test_result("Spock", "Rock"))

    def test_player_2_wins_Rock_Spock(self):
        self.assertEqual("John wins", self.game_1.test_result("Rock", "Spock"))
    
    def test_invalid_gesture(self):
        self.assertEqual("Please enter valid gesture", self.game_1.test_result("Rock", "Sock"))