class TennisGame2:
    score_names = ["Love", "Fifteen", "Thirty", "Forty"]
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1points += 1
        else:
            self.p2points += 1

    def score(self):

        if self.p1points == self.p2points:
            if self.p1points < 3:
                return f"{self.score_names[self.p1points]}-All"
            return "Deuce"

        if self.p1points < 4 and self.p2points < 4:
            return f"{self.score_names[self.p1points]}-{self.score_names[self.p2points]}"

        diff = self.p1points - self.p2points

        if diff == 1:
            return "Advantage player1"
        if diff == -1:
            return "Advantage player2"
        if diff >= 2:
            return "Win for player1"
        return "Win for player2"