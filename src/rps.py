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

        # first checks if player_1 = game[0], then checks if player_2 = game[0]
        for game in self.win_game:   # example. wing_game[0] = ["Rock","Scissors"]
            if [player_1_input, player_2_input] == game:  # list = ["Rock","Scissors"]
                self.set_the_winner(self.player_1)
                return f"{self.winner.name} wins"
            elif [player_2_input, player_1_input] == game: # list = ["Rock","Scissors"]
                self.set_the_winner(self.player_2)
                return f"{self.winner.name} wins"
        
        return "Please enter valid gesture"

        