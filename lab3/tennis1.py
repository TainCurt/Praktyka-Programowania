class TennisGame1:
    results_name = ["Love", "Fifteen", "Thirty", "Forty"]

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
        if self._is_draw():
            return self._draw_score()
        if self._is_endgame():
            return self._endgame_score()
        return self._regular_score()

    def _is_draw(self):
        return self.p1points == self.p2points

    def _is_endgame(self):
        return self.p1points >= 4 or self.p2points >= 4

    def _draw_score(self):
        if self.p1points < 3:
            return f"{self.results_name[self.p1points]}-All"
        return "Deuce"

    def _endgame_score(self):
        diff = self.p1points - self.p2points
        if diff == 1:
            return "Advantage player1"
        if diff == -1:
            return "Advantage player2"
        if diff >= 2:
            return "Win for player1"
        return "Win for player2"

    def _regular_score(self):
        return f"{self.results_name[self.p1points]}-{self.results_name[self.p2points]}"