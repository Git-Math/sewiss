from tkinter import *
from tkinter import ttk

def p(players_names):
    print(players_names)

root = Tk()

# window name
root.title("Sewiss")

# window size
root.geometry("700x700")

#l = Label(root, text = "Entrer les noms des joueurs dans l'ordre du seeding")

# grid
gr = ttk.Frame(root, padding = 10)
gr.grid()

players_names = [None] * 16

ttk.Label(gr, text = "Seed 1:").grid(column = 0, row = 1)
players_names[0] = Text(gr, height = 1, width = 20)
players_names[0].grid(column = 1, row = 1)

ttk.Label(gr, text = "Seed 2:").grid(column = 0, row = 2)
ttk.Label(gr, text = "Seed 3:").grid(column = 0, row = 3)
ttk.Label(gr, text = "Seed 4:").grid(column = 0, row = 4)
ttk.Label(gr, text = "Seed 5:").grid(column = 0, row = 5)
ttk.Label(gr, text = "Seed 6:").grid(column = 0, row = 6)
ttk.Label(gr, text = "Seed 7:").grid(column = 0, row = 7)
ttk.Label(gr, text = "Seed 8:").grid(column = 0, row = 8)
ttk.Label(gr, text = "Seed 9:").grid(column = 0, row = 9)
ttk.Label(gr, text = "Seed 10:").grid(column = 0, row = 10)
ttk.Label(gr, text = "Seed 11:").grid(column = 0, row = 11)
ttk.Label(gr, text = "Seed 12:").grid(column = 0, row = 12)
ttk.Label(gr, text = "Seed 13:").grid(column = 0, row = 13)
ttk.Label(gr, text = "Seed 14:").grid(column = 0, row = 14)
ttk.Label(gr, text = "Seed 15:").grid(column = 0, row = 15)
ttk.Label(gr, text = "Seed 16:").grid(column = 0, row = 16)

printButton = Button(gr, text = "Ok", command = lambda: p(players_names)).grid(column = 0, row = 16)

root.mainloop()
