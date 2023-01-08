class Player:
    def __init__(self, name, seed):
        self.name = name
        self.sets_win = 0
        self.sets_lose = 0
        self.opponents_win = []
        self.opponents_lose = []
        self.buchholz = 0
        self.seed = seed

    def add_win(opponent):
        self.sets_win += 1
        self.opponents_win.append(opponent)

    def add_lose(opponent):
        self.sets_lose += 1
        self.opponents_lose.append(opponent)

    def update_buchholz():
        for opponents in (self.opponents_win + self.opponents_lose):
            self.buchholz += opponents.sets_win
            self.buchholz -= opponents.sets_lose

    def __str__(self):
        return f"""Player {{
    name: {self.name}
    Sets win: {self.sets_win}
    Sets lose: {self.sets_lose}
    Opponents win: {self.opponents_win}
    Opponents lose: {self.opponents_lose}
    Buchholz score: {self.buchholz}
    Seed: {self.seed}
}}"""

def update_players_buchholz(players):
    for player in players:
        player.update_buchholz()

def sort_players(players):
    players.sort(key = lambda x: (x.sets_win, -x.sets_lose, x.buchholz, -x.seed), reverse = True)


