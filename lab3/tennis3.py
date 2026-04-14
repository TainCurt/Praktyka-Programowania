class TennisGame3:
    results_names = ["Love", "Fifteen", "Thirty", "Forty"]
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player):
        if player == self.player1_name:
            self.p1points += 1
        else:
            self.p2points += 1  

    def score(self):

        if self.p1points < 4 and self.p2points < 4 and (self.p1points + self.p2points < 6):
            if self.p1points == self.p2points:
                return f"{self.results_names[self.p1points]}-All"
            return f"{self.results_names[self.p1points]}-{self.results_names[self.p2points]}"

        if self.p1points == self.p2points:
            return "Deuce"

        leader = self.player1_name if self.p1points > self.p2points else self.player2_name

        if abs(self.p1points - self.p2points) == 1:
            return f"Advantage {leader}"
        return f"Win for {leader}"