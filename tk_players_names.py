import tkinter as tk
from tkinter import ttk

def read_players_names(players_texts, players_names, error_labels, root):
    for i, player_text in enumerate(players_texts):
        player_name = player_text.get('1.0', 'end').strip()
        if len(player_name) == 0:
            error_labels.config(text = "Player" + str(i + 1) + " is empty")
            return
        players_names[i] = player_name

    root.destroy()

def run():
    players_names = [""] * 16

    root = tk.Tk()

    # window name
    root.title("Players Names")

    # window size
    root.geometry("700x700")

    ft = ttk.Frame(root)
    ft.pack()

    fg = ttk.Frame(root)
    fg.pack()

    fe = ttk.Frame(root)
    fe.pack()

    # title
    ttk.Label(ft, text = "Entrer les noms des joueurs").pack()

    # error
    error_label = ttk.Label(ft, text = "")
    error_label.pack()

    # grid
    players_labels = [None] * 16
    players_texts = [None] * 16

    for i in range (0, 16):
        players_labels[i] = ttk.Label(fg, text = "Joueur " + str(i + 1) + ": ")
        players_labels[i].grid(column = 0, row = i)

        players_texts[i] = tk.Text(fg, height = 1, width = 20)
        players_texts[i].grid(column = 1, row = i)

    ttk.Button(fg, text = "Valider", command = lambda: read_players_names(players_texts, players_names, error_label, root)).grid(column = 1, row = 16)

    root.mainloop()

    return players_names
