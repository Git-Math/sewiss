import sys
import os
import tk_tournament_name
import tk_players_names
import tk_players_seeds
import tk_round
import tk_standings
from player import *

TOURNAMENT_RESULTS_DIRNAME = "tournament_results"

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        tournament_name, round_number, players = read_state_json(sys.argv[1])
    else:
        # tournament name
        tournament_name = tk_tournament_name.run()

        if not tournament_name:
            print("Le nom du tournoi est vide")
            exit()

        # players names
        players_names = tk_players_names.run()

        if len(players_names) != 16:
            print("Il n'y a pas 16 noms de joueurs")
            exit()

        # players seeding
        seeded_players_names = tk_players_seeds.run(players_names)

        if len(seeded_players_names) != 16:
            print("Il n'y a pas 16 noms de joueurs")
            exit()

        players = []

        for i, player_name in enumerate(seeded_players_names):
            players.append(Player(player_name, i + 1))

        round_number = 0

    # create tournament results directories
    dirname = TOURNAMENT_RESULTS_DIRNAME + os.sep + tournament_name
    os.makedirs(dirname, exist_ok = True)

    if round_number == 0:
        write_state_json(tournament_name, round_number, players, dirname)
        round_number = 1

    for r in range(round_number, 6):
        matchups = compute_matchups(players)
        round_results = tk_round.run(players, matchups, r)
        if not round_results:
            print("Il n'y a pas de résultats de round")
            exit()
        write_round_results(r, round_results, dirname)
        update_players_round(players, round_results)
        update_players_buchholz(players)
        sort_players(players)
        write_state_json(tournament_name, r, players, dirname)

    tk_standings.run(players)
