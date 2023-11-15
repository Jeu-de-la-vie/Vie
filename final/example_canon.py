from grille_cellule_regles import Grille

def canon_init():
    vivantes = [(10,1),(10,2),(11,1),(11,2),
                (10,11),(11,11),(12,11),(9,12),(8,13),(8,14),
                (13,12),(14,13),(14,14),(13,16),(12,17),(11,17),
                (10,17),(9,16),(11,15),(11,18),
                (10,21),(10,22),(9,21),(9,22),(8,21),(8,22),
                (11,23),(11,25),(12,25),(7,23),(7,25),(6,25),
                (8,35),(8,36),(9,35),(9,36)]
    return vivantes

# Générer la grille

grille = Grille(50)
grille.generer()

# Placer les cellules vivantes dans la grille

vivantes = canon_init()
print(vivantes)
grille.modifier(vivantes)

# Générer l'interface graphique

import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=grille.cote * 20, height=grille.cote * 20)
canvas.pack()

# Montrer les cellules vivantes, appliquer les règles du jeu et mettre à jour l'interface

from interface import jouer_tour

jouer_tour(grille, vivantes, root, canvas)  # lancer le premier tour
root.mainloop()
