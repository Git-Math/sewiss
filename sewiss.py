import tk_players_names
import tk_players_seeds
import tk_round
import tk_standings
from player import *

if __name__ == '__main__':
    # players names
    players_names = tk_players_names.run()

    print(players_names)

    if len(players_names) != 16:
        print("Il n'y a pas 16 noms de joueurs")
        exit()

    # players seeding
    seeded_players_names = tk_players_seeds.run(players_names)

    print(seeded_players_names)

    if len(seeded_players_names) != 16:
        print("Il n'y a pas 16 noms de joueurs")
        exit()

    #seeded_players_names = ["Susu", "Dazed", "CHEF!", "Le Shibateur", "Suri", "Albertino", "Rico", "Manon", "Andreea", "Theo", "Logan", "Sirop", "Boris", "TBN", "Aness", "Marine"]

    players = []

    for i, player_name in enumerate(seeded_players_names):
        players.append(Player(player_name, i + 1))

    for r in range(1, 6):
        matchups = compute_matchups(players)
        round_results = tk_round.run(players, matchups, r)
        if not round_results:
            print("Il n'y a pas de résultats de round")
            exit()
        update_players_round(players, round_results)
        update_players_buchholz(players)
        sort_players(players)

    tk_standings.run(players)
