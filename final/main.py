########################################################################################
# Générer la grille
########################################################################################
from grille_cellule_regles import Grille

grille = Grille(25)
grille.generer()


########################################################################################
# Placer les cellules vivantes dans la grille
########################################################################################
from random import shuffle

nombre = int(input("Nombre de cellules vivantes : "))
coordonnees = [(i, j) for i in range(grille.cote) for j in range(grille.cote)]
shuffle(coordonnees)
vivantes = coordonnees[:nombre]

print(vivantes)
grille.modifier(vivantes)


########################################################################################
# Générer l'interface graphique
########################################################################################
import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=grille.cote * 20, height=grille.cote * 20)
canvas.pack()


#########################################################################################
# Montrer les cellules vivantes, appliquer les règles du jeu et mettre à jour l'interface
#########################################################################################
from interface import jouer_tour

jouer_tour(grille, vivantes, root, canvas)  # lancer le premier tour
root.mainloop()
