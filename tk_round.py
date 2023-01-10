import tkinter as tk
from tkinter import ttk

MAX_MATCHES_IN_ROW = 2
MATCH_COLUMN_SIZE = 3
MATCH_ROW_SIZE = 4
X_SPACE_BETWEEN_MATCHES = 50
Y_SPACE_BETWEEN_MATCHES = 20
X_SPACE_BEFORE_STANDINGS = 150

def read_round_results(matchups_widgets, round_results, error_label, root):
    for mw in matchups_widgets:
        player1_name = mw["player1"].cget("text")
        try:
            player1_score = int(mw["player1_score"].get("1.0", "end").strip())
        except ValueError:
            error_label.config(text = f"Le score de {player1_name} est invalide")
            round_results.clear()
            return
        if player1_score < 0:
            error_label.config(text = f"Le score de {player1_name} est négatif")
            round_results.clear()
            return

        player2_name = mw["player2"].cget("text")
        try:
            player2_score = int(mw["player2_score"].get("1.0", "end").strip())
        except ValueError:
            error_label.config(text = f"Le score de {player2_name} est invalide")
            round_results.clear()
            return
        if player2_score < 0:
            error_label.config(text = f"Le score de {player2_name} est négatif")
            round_results.clear()
            return

        if player1_score == player2_score:
            error_label.config(text = f"Les scores de {player1_name} et {player2_name} sont égaux")
            round_results.clear()
            return

        round_results.append({"player1_name": player1_name, "player1_score" : player1_score, "player2_name": player2_name, "player2_score" : player2_score})

    root.destroy()
       

def swap_widgets(start_widget, target_widget):
    start_text = start_widget.cget("text")
    target_text = target_widget.cget("text")
    start_widget.config(text = target_text)
    target_widget.config(text = start_text)

def on_click(event, players_labels, root):
    widget = event.widget

    if widget in players_labels:
        start_position = (event.x, event.y)
        widget_grid_info = widget.grid_info()
        widget.bind("<B1-Motion>", lambda event:drag_motion(event, widget, start_position))
        widget.bind("<ButtonRelease-1>", lambda event:drag_release(event, players_labels, widget, widget_grid_info, root))
    else:
        root.unbind("<ButtonRelease-1>")

def drag_motion(event, widget, start_position): 
    x = widget.winfo_x() + event.x - start_position[0]
    y = widget.winfo_y() + event.y - start_position[1]
    widget.lift()
    widget.place(x = x, y = y)

def drag_release(event, players_labels, widget, widget_grid_info, root):
    widget.lower()
    x, y = root.winfo_pointerxy()
    target_widget = root.winfo_containing(x, y)
    if target_widget in players_labels:
        swap_widgets(widget, target_widget)
    widget.grid(row = widget_grid_info['row'], column = widget_grid_info['column'])

def run(players, matchups, r):
    round_results = []

    root = tk.Tk()

    # window name
    root.title(f"Round {r}")

    # window size
    root.geometry("1000x500")

    # frame
    frame = ttk.Frame(root)
    frame.pack()

    # title
    ttk.Label(frame, text = f"Round {r}") \
       .grid(row = 0, column = 0, columnspan = 20)

    # set empty space between matches
    for i in range(MAX_MATCHES_IN_ROW - 1):
        if (i + 1) >= len(matchups):
            break
        frame.columnconfigure((i * MATCH_COLUMN_SIZE) + 2, minsize = X_SPACE_BETWEEN_MATCHES)

    # matchups
    matchups_widgets = []

    for i, (player1, player2) in enumerate(matchups):
        start_column = (i % MAX_MATCHES_IN_ROW) * MATCH_COLUMN_SIZE
        start_row = (int(i / MAX_MATCHES_IN_ROW) * MATCH_ROW_SIZE) + 1

        if i % MAX_MATCHES_IN_ROW == 0:
            frame.rowconfigure(start_row, minsize = Y_SPACE_BETWEEN_MATCHES)

        is_rematch = player1.is_rematch(player2)
        same_set_count = player1.compare_set_count(player2)

        warning_string = ""
        warning_string += "Rematch" if is_rematch else ""
        warning_string += (("/" if is_rematch else "") + "Set count diff") if not same_set_count else ""

        warning_label = ttk.Label(frame, text = warning_string) \
                           .grid(column = start_column, row = start_row + 1, columnspan = 2)
        
        player1_label = ttk.Label(frame, text = player1.name, borderwidth = 10, relief="solid", width = 20);
        player1_label.grid(column = start_column, row = start_row + 2, sticky = tk.E)

        player1_score_text = tk.Text(frame, height = 1, width = 3)
        player1_score_text.grid(column = start_column + 1, row = start_row + 2, sticky = tk.W)

        player2_label = ttk.Label(frame, text = player2.name, borderwidth = 10, relief="solid", width = 20);
        player2_label.grid(column = start_column, row = start_row + 3, sticky = tk.E)

        player2_score_text = tk.Text(frame, height = 1, width = 3)
        player2_score_text.grid(column = start_column + 1, row = start_row + 3, sticky = tk.W)

        matchups_widgets.append({"warning": warning_label, "player1": player1_label, "player1_score": player1_score_text, "player2": player2_label, "player2_score": player2_score_text})

    # error
    error_label = ttk.Label(frame, text = "")
    error_label.grid(column = 0, row = 21, columnspan = 20)

    # validate button
    ttk.Button(frame, text = "Valider", command = lambda: read_round_results(matchups_widgets, round_results, error_label, root)) \
       .grid(column = 0, row = 20, columnspan = 20)

    # standings
    standings_start_column = min(len(matchups), MAX_MATCHES_IN_ROW) * MATCH_COLUMN_SIZE
    standings_start_row = 2

    frame.columnconfigure(standings_start_column - 1, minsize = X_SPACE_BEFORE_STANDINGS)

    ttk.Label(frame, text = "Standings") \
       .grid(column = standings_start_column, row = standings_start_row, columnspan = 5)

    ttk.Label(frame, text = "Placement", borderwidth = 10, relief="solid", width = 10) \
       .grid(column = standings_start_column, row = standings_start_row + 1)
    ttk.Label(frame, text = "Name", borderwidth = 10, relief="solid", width = 20) \
       .grid(column = standings_start_column + 1, row = standings_start_row + 1)
    ttk.Label(frame, text = "Set count", borderwidth = 10, relief="solid", width = 10) \
       .grid(column = standings_start_column + 2, row = standings_start_row + 1)
    ttk.Label(frame, text = "Buchholz", borderwidth = 10, relief="solid", width = 10) \
       .grid(column = standings_start_column + 3, row = standings_start_row + 1)
    ttk.Label(frame, text = "Seed", borderwidth = 10, relief="solid", width = 10) \
       .grid(column = standings_start_column + 4, row = standings_start_row + 1)

    for i, player in enumerate(players):
        ttk.Label(frame, text = str(i + 1), borderwidth = 10, relief="solid", width = 10) \
           .grid(column = standings_start_column, row = standings_start_row + 2 + i)
        ttk.Label(frame, text = player.name, borderwidth = 10, relief="solid", width = 20) \
           .grid(column = standings_start_column + 1, row = standings_start_row + 2 + i)
        ttk.Label(frame, text = f"{player.sets_win}-{player.sets_lose}", borderwidth = 10, relief="solid", width = 10) \
           .grid(column = standings_start_column + 2, row = standings_start_row + 2 + i)
        ttk.Label(frame, text = str(player.buchholz), borderwidth = 10, relief="solid", width = 10) \
           .grid(column = standings_start_column + 3, row = standings_start_row + 2 + i)
        ttk.Label(frame, text = str(player.seed), borderwidth = 10, relief="solid", width = 10) \
           .grid(column = standings_start_column + 4, row = standings_start_row + 2 + i)

    # drag and drop button
    #root.bind("<Button-1>", lambda event:on_click(event, players_labels, root))

    root.mainloop()

    return round_results