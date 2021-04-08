class Rps:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2

        self.winner = None

    def set_the_winner(self, player):
        self.winner = player
        