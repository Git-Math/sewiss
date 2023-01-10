import tkinter as tk
from tkinter import ttk

ROW_MIN_SIZE = 20

def run(players):
    root = tk.Tk()

    # window name
    root.title("Final Standings")

    # window size
    root.geometry("700x700")

    # frame
    frame = ttk.Frame(root)
    frame.pack()

    # title
    ttk.Label(frame, text = "Final Standings") \
       .grid(row = 0, column = 0, columnspan = 5)

    # standings
    standings_start_column = 0
    standings_start_row = 2

    ttk.Label(frame, text = "Placement", borderwidth = 10, relief="solid", width = 10) \
       .grid(column = standings_start_column, row = standings_start_row)
    ttk.Label(frame, text = "Name", borderwidth = 10, relief="solid", width = 20) \
       .grid(column = standings_start_column + 1, row = standings_start_row)
    ttk.Label(frame, text = "Set count", borderwidth = 10, relief="solid", width = 10) \
       .grid(column = standings_start_column + 2, row = standings_start_row)
    ttk.Label(frame, text = "Buchholz", borderwidth = 10, relief="solid", width = 10) \
       .grid(column = standings_start_column + 3, row = standings_start_row)
    ttk.Label(frame, text = "Seed", borderwidth = 10, relief="solid", width = 10) \
       .grid(column = standings_start_column + 4, row = standings_start_row)

    for i, player in enumerate(players):
        ttk.Label(frame, text = str(i + 1), borderwidth = 10, relief="solid", width = 10) \
           .grid(column = standings_start_column, row = standings_start_row + 1 + i)
        ttk.Label(frame, text = player.name, borderwidth = 10, relief="solid", width = 20) \
           .grid(column = standings_start_column + 1, row = standings_start_row + 1 + i)
        ttk.Label(frame, text = f"{player.sets_win}-{player.sets_lose}", borderwidth = 10, relief="solid", width = 10) \
           .grid(column = standings_start_column + 2, row = standings_start_row + 1 + i)
        ttk.Label(frame, text = str(player.buchholz), borderwidth = 10, relief="solid", width = 10) \
           .grid(column = standings_start_column + 3, row = standings_start_row + 1 + i)
        ttk.Label(frame, text = str(player.seed), borderwidth = 10, relief="solid", width = 10) \
           .grid(column = standings_start_column + 4, row = standings_start_row + 1 + i)

    # configure all rows min size
    for row_i in range(frame.grid_size()[1]):
        frame.rowconfigure(row_i, minsize = ROW_MIN_SIZE)

    root.mainloop()
   
