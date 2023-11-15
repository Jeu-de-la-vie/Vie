from grille_cellule_regles import jeu_de_la_vie


def afficher_grille_graphique(grille, canvas):
    canvas.delete("all")  # effacer le contenu précédent du canvas

    # dessiner les lignes horizontales
    for i in range(1, grille.cote):
        canvas.create_line(0, i * 20, grille.cote * 20, i * 20)

    # dessiner les lignes verticales
    for j in range(1, grille.cote):
        canvas.create_line(j * 20, 0, j * 20, grille.cote * 20)

    for i in range(grille.cote):
        for j in range(grille.cote):
            x0, y0 = j * 20, i * 20
            x1, y1 = x0 + 20, y0 + 20
            if grille.matrice[i][j] == 1:
                canvas.create_rectangle(x0, y0, x1, y1, fill="black")


def jouer_tour(grille, vivantes, root, canvas):
    vivantes = jeu_de_la_vie(grille, vivantes)
    print(len(vivantes), "cellules vivantes au prochain tour")
    grille.modifier(vivantes)
    afficher_grille_graphique(grille, canvas)
    root.after(1000, lambda: jouer_tour(grille, vivantes, root, canvas))  # Attendre 1 seconde entre les tours pour mieux visualiser
