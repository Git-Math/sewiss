class Player:
    def __init__(self, name, seed):
        self.name = name
        self.sets_win = 0
        self.sets_lose = 0
        self.opponents_win = []
        self.opponents_lose = []
        self.buchholz = 0
        self.seed = seed

    def add_win(self, opponent):
        self.sets_win += 1
        self.opponents_win.append(opponent)

    def add_lose(self, opponent):
        self.sets_lose += 1
        self.opponents_lose.append(opponent)

    def update_buchholz(self):
        for opponents in (self.opponents_win + self.opponents_lose):
            self.buchholz += opponents.sets_win
            self.buchholz -= opponents.sets_lose

    def is_rematch(self, player):
        return player in (self.opponents_win + self.opponents_lose)

    def compare_set_count(self, player):
        return self.sets_win == player.sets_win and self.sets_lose == player.sets_lose

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

    def __repr__(self):
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

def match_group(group, group_len, group_half_len, current_i, allowed_rematch, current_rematch, matchups):
    if current_i >= (group_len - 1):
        return False

    if (group[current_i]["has_matchup"]):
        return match_group(group, group_len, group_half_len, current_i + 1, allowed_rematch, current_rematch, matchups)

    # we first check matchups in the second half in ascending order
    matchups_i_to_check = [x for x in range(group_half_len, group_len)]

    # then we check in the first half in descending order
    matchups_i_to_check += [x for x in reversed(range(0, group_half_len))]

    # we only check indexes after the current index, because previous players are already matched
    matchups_i_to_check = [x for x in matchups_i_to_check if x > current_i]

    # check all possible matchups
    for i in matchups_i_to_check:
        if group[i]["has_matchup"]:
            continue

        is_rematch = group[current_i]["player"].is_rematch(group[i]["player"])

        if is_rematch:
            if current_rematch >= allowed_rematch:
                continue
            else:
                current_rematch += 1

        group[current_i]["has_matchup"] = True
        group[i]["has_matchup"] = True

        matchups.append((group[current_i]["player"], group[i]["player"]))

        if len(matchups) == group_half_len:
            return True

        ret = match_group(group, group_len, group_half_len, current_i + 1, allowed_rematch, current_rematch, matchups)

        if ret:
            return ret

        matchups.pop()

        group[current_i]["has_matchup"] = False
        group[i]["has_matchup"] = False

        if is_rematch:
            current_rematch -= 1

    return False

def compute_group_matchups(group):
    matchups = []

    group_len = len(group)
    group_half_len = int(group_len / 2)

    # try to match group with minimum rematch
    # we start to try with 0 rematch
    # and then increase progressively if we can't match
    for allowed_rematch in range(group_half_len + 1):
        if match_group(group, group_len, group_half_len, 0, allowed_rematch, 0, matchups):
            return matchups

def compute_matchups(players):
    matchups = []

    # get all unique sets counts in players
    sets_counts = list({ (x.sets_win, x.sets_lose) for x in players if x.sets_win < 3 and x.sets_lose < 3 })

    sets_counts.sort(key = lambda x: x[0], reverse = True)

    # compute matchups for each set count
    for set_counts in sets_counts:
        group = [ { "player": x, "has_matchup": False } for x in players if x.sets_win == set_counts[0] and x.sets_lose == set_counts[1] ]
        group_matchups = compute_group_matchups(group)

        matchups += group_matchups

    return matchups
