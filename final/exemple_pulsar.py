def pulsar_init():
    vivantes = [(i, j) for i in [2, 7, 9, 14] for j in [4, 5, 6, 10, 11, 12]] +\
        [(j, i) for i in [2, 7, 9, 14] for j in [4, 5, 6, 10, 11, 12]]
    
    return vivantes

# Générer la grille
from grille_cellule_regles import Grille

grille = Grille(17)
grille.generer()

# Placer les cellules vivantes dans la grille
vivantes = pulsar_init()
print(vivantes)
grille.modifier(vivantes)

# Générer l'interface graphique
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=grille.cote * 20, height=grille.cote * 20)
canvas.pack()

# Montrer les cellules vivantes, appliquer les règles du jeu et mettre à jour
# l'interface
from interface import jouer_tour

jouer_tour(grille, vivantes, root, canvas)  # lancer le premier tour
root.mainloop()
