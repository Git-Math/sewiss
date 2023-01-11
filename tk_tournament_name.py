import tkinter as tk
from tkinter import ttk

def read_tournament_name(tournament_name_text, tournament_name, error_labels, root):
    tournament_name[0] = tournament_name_text.get('1.0', 'end').strip()

    if not tournament_name[0]:
        error_labels.config(text = "Nom du tournoi vide")
        tournament_name[0] = ""
        return

    if not all(c.isalnum() or c == "-" for c in tournament_name[0]):
        error_labels.config(text = "Nom du tournoi invalide; uniquement les lettres, les chiffres et - sont autorisés")
        tournament_name[0] = ""
        return

    root.destroy()

def run():
    tournament_name = [""]

    root = tk.Tk()

    # window name
    root.title("Tournament Name")

    # window size
    root.geometry("500x150")

    # frame
    frame = ttk.Frame(root)
    frame.pack()

    # tournament name
    frame.rowconfigure(0, minsize = 20)

    ttk.Label(frame, text = "Nom du tournoi: ") \
       .grid(column = 0, row = 1, sticky = tk.E)

    tournament_name_text = tk.Text(frame, height = 1, width = 20)
    tournament_name_text.grid(column = 1, row = 1, sticky = tk.W)

    frame.rowconfigure(2, minsize = 20)

    # error
    error_label = ttk.Label(frame, text = "")
    error_label.grid(column = 0, row = 4, columnspan = 2)

    # button
    ttk.Button(frame, text = "Valider", command = lambda: read_tournament_name(tournament_name_text, tournament_name, error_label, root)) \
       .grid(column = 1, row = 3, sticky = tk.W)

    root.mainloop()

    return tournament_name[0]
