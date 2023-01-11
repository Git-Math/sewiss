import tkinter as tk
from tkinter import ttk

def read_seeding(players_labels, seeded_players_names, root):
    for player_label in players_labels:
        seeded_players_names.append(player_label.cget("text").strip())

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
    widget.config(state = "disabled")
    x, y = root.winfo_pointerxy()
    target_widget = root.winfo_containing(x, y)
    widget.config(state = "enabled")
    if target_widget in players_labels:
        swap_widgets(widget, target_widget)
    widget.grid(row = widget_grid_info['row'], column = widget_grid_info['column'])

def run(players_names):
    seeded_players_names = []

    root = tk.Tk()

    # window name
    root.title("Players Seeds")

    # window size
    root.geometry("500x500")

    # frame
    frame = ttk.Frame(root)
    frame.pack()

    # title
    ttk.Label(frame, text = "Seed les joueurs en faisant glisser les noms") \
       .grid(row = 0, column = 0, columnspan = 2)

    frame.rowconfigure(1, minsize = 20)

    # players
    players_labels = [None] * 16

    for i, player_name in enumerate(players_names):
        ttk.Label(frame, text = "Seed " + str(i + 1) + ": ") \
           .grid(column = 0, row = i + 2, sticky = tk.E)

        players_labels[i] = ttk.Label(frame, text = player_name, borderwidth = 10, relief="solid", width = 20);
        players_labels[i].grid(column = 1, row = i + 2, sticky = tk.W)

    frame.rowconfigure(18, minsize = 20)

    # validate button
    ttk.Button(frame, text = "Valider", command = lambda: read_seeding(players_labels, seeded_players_names, root)) \
       .grid(column = 1, row = 19, sticky = tk.W)

    # drag and drop button
    root.bind("<Button-1>", lambda event:on_click(event, players_labels, root))

    root.mainloop()

    return seeded_players_names
