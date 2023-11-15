
def test_carre(grille):
    c1 = Cellule(4,4,grille)
    voisines = c1.donner_voisines(grille)
    return voisines + [c1.rang]
