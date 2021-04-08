class Rps:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.win_game = [["Rock","Scissors"], ["Paper","Rock"], ["Scissors", "Paper"], 
        ["Rock", "Lizard"], ["Lizard", "Spock"], ["Spock", "Scissors"], ["Scissors", "Lizard"], 
        ["Lizard", "Paper"], ["Paper", "Spock"], ["Spock", "Rock"]]
        self.winner = None

    def set_the_winner(self, player):
        self.winner = player

    def test_result(self, player_1_input, player_2_input):

        if player_1_input == player_2_input:
            return "tie"

        for game in self.win_game:
            if [player_1_input, player_2_input] == game:
                self.set_the_winner(self.player_1)
                break
            else:
                self.set_the_winner(self.player_2)

        return f"{self.winner.name} wins"