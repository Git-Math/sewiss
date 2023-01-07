import tkinter as tk
from tkinter import ttk

def read_players_names(players_texts, players_names, error_labels, root):
    for i, player_text in enumerate(players_texts):
        player_name = player_text.get('1.0', 'end').strip()
        if len(player_name) == 0:
            error_labels.config(text = "Joueur " + str(i + 1) + " is empty")
            players_names.clear()
            return

        players_names.append(player_name)

    duplicate_names = {x for x in players_names if players_names.count(x) > 1}

    if len(duplicate_names) != 0:
        error_labels.config(text = "Nom" + ("s" if len(duplicate_names) > 1 else "") + " dupliqué" + ("s" if len(duplicate_names) > 1 else "") + ": " + str(duplicate_names))
        players_names.clear()
        return

    root.destroy()

def run():
    players_names = []

    root = tk.Tk()

    # window name
    root.title("Players Names")

    # window size
    root.geometry("700x700")

    # frame
    frame = ttk.Frame(root)
    frame.pack()

    # title
    ttk.Label(frame, text = "Entrer les noms des joueurs") \
       .grid(row = 0, column = 0, columnspan = 2)

    # players
    players_texts = [None] * 16

    for i in range (0, 16):
        ttk.Label(frame, text = "Joueur " + str(i + 1) + ": ") \
           .grid(column = 0, row = i + 1)

        players_texts[i] = tk.Text(frame, height = 1, width = 20)
        players_texts[i].grid(column = 1, row = i + 1)

    # error
    error_label = ttk.Label(frame, text = "")
    error_label.grid(column = 0, row = 18, columnspan = 2)

    # button
    ttk.Button(frame, text = "Valider", command = lambda: read_players_names(players_texts, players_names, error_label, root)).grid(column = 1, row = 17)

    root.mainloop()

    return players_names
