import tk_players_names
import tk_players_seeds
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

    for player in players:
        print(player)

    matchups = compute_matchups(players)

    print(matchups)
