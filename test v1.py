from random import randint
from random import shuffle

#Test jeu de la vie v1
        
class Grille:
    def __init__(self,cote):
        self.cote = cote
        self.taille = cote * cote
        
    def generer(self):
        self.matrice = [[0 for i in range(self.cote)] for j in range(self.cote)]
        return self.matrice
        
    def afficher(self):
        for ligne in self.matrice :
            print(ligne)
            
    def modifier(self,liste):
        self.generer()
        for element in liste:
            self.matrice[element[0]][element[1]] = 1
        return self.matrice
            
class Cellule:
    def __init__(self, x, y, grille):
        self.x = x
        self.y = y
        self.etat = grille.matrice[x][y]
        self.rang = (x,y)
        
    def donner_voisines(self):
        self.voisines = []
        a = -1
        for i in range(3):
            b = -1
            for j in range(3):
                voisine = (self.x + a, self.y + b)
                if voisine[0] in range(0,grille.cote):
                    if voisine[1] in range(0,grille.cote):
                        if voisine != (self.x,self.y):
                            self.voisines.append(voisine)
                b = b + 1
            a = a + 1
        return self.voisines

def test_jeu(grille):
    c1 = Cellule(4,4,grille)
    voisines = c1.donner_voisines()
    return voisines + [c1.rang]

grille = Grille(15)
grille.generer()
grille.afficher()

"""
Pour lancer le jeu, on rentre le nombre de cellules vivantes
que l'on veut en début de partie, puis elles sont placées de
façon aléatoire dans la grille (0 : cellule morte, 1 : vivante)
"""

nombre = int(input("Nombre de cellules vivantes : "))
coordonnees = [(i, j) for i in range(grille.cote) for j in range(grille.cote)]
# liste de toutes les coordonnées de la grille
shuffle(coordonnees)
vivantes = coordonnees[:nombre]

#vivantes = test_jeu(grille)
# liste des coordonnées des cellules vivantes
print(vivantes)
grille.modifier(vivantes)
grille.afficher()

max_tour = 3
for i in range(max_tour):
    print("Tour n°", i+1)
    stock = []      #future liste de cellules vivantes
    # on recherche des voisines de chaque cellule vivante
    for cellule in vivantes :
        cellule = Cellule(cellule[0],cellule[1],grille)
        cellule_voisines = cellule.donner_voisines()
        #print(cellule_voisines)
    # on détermine si les cellules vivante à t sont vivantes à t+1
        cnt_cellule = 0     # nombre de voisines vivantes
        for voisine in cellule_voisines :
            voisine = Cellule(voisine[0],voisine[1],grille)
            if voisine.etat == 1:
                cnt_cellule = cnt_cellule + 1
            voisine_entourage = voisine.donner_voisines()
            #print(voisine_entourage)
            cnt_voisine = 0
            for voisin in voisine_entourage :
                voisin = Cellule(voisin[0],voisin[1],grille)
                if voisin.etat == 1:
                    cnt_voisine = cnt_voisine + 1
            #print("Voisines de", voisine.rang, "vivantes : ", cnt_voisine)
            if cnt_voisine == 3 and voisine.etat == 0 :
                if voisine.rang not in stock :
                    stock.append(voisine.rang)
            elif cnt_voisine in [2,3] and voisine.etat == 1 :
                if voisine.rang not in stock :
                    stock.append(voisine.rang)
        #print("Voisines de", cellule.rang, "vivantes : ", cnt_cellule)      
        if cnt_cellule in [2,3] :
            if cellule.rang not in stock:
                stock.append(cellule.rang)
    vivantes = stock
    print(len(vivantes), "cellules vivantes au prochain tour")
    print(vivantes)
    grille.modifier(vivantes)
    grille.afficher()










    
