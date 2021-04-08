class Rps:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

        self.winner = None

    def set_the_winner(self, player):
        self.winner = player

    def test_result(self, player_1_input, player_2_input):

        if player_1_input == player_1_input:
            return "tie"
        