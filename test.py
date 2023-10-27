from random import randint

# Essayer de faire un code simple mais qui fonctionne
# Jeu de la vie

class Cellule :
    def __init__(self,x,y,etat=0):
        self.x = x
        self.y = y
        self.etat = etat
        self.rang = (x,y)
        #le rang de la cellule dans la grille (pas en pixel)
    def __repr__(self):
        return f"position : {self.rang} , etat : {self.etat}"
    def voisines(self):
        self.vois = []  #liste des 8 voisines
        #à améliorer
        a = - 1
        b = - 1
        for i in range(3):  #1ere ligne
            rang_vois = (self.x+a,self.y+b)
            if rang_vois[0] in range(0,15):
                if rang_vois[1] in range(0,15):
                    self.vois.append(rang_vois)
            b = b + 1
        a = 0
        b = - 1
        for i in range(2):  #2e ligne
            rang_vois = (self.x+a,self.y+b)
            if rang_vois[0] in range(0,15):
                if rang_vois[1] in range(0,15):
                    self.vois.append(rang_vois)
            b = b + 2
        a = 1
        b = - 1
        for i in range(3):  #3e ligne
            rang_vois = (self.x+a,self.y+b)
            if rang_vois[0] in range(0,15):
                if rang_vois[1] in range(0,15):
                    self.vois.append(rang_vois)
            b = b + 1
        return self.vois
    """
    def etat(self):
        pass
    def tabcell(self):
        tab = []
        for cell in Cellule :
            tab.append(cell)
        return tab
    """
def pprint(tab):
    for el in tab:
        print(el)

#c1 = Cellule(2,0)
#c2 = Cellule(4,1)
cote = 15   #côté de la grille
grille = [[0 for i in range(cote)] for i in range(cote)]
pprint(grille)
"""
Pour lancer le jeu, on rentre le nombre de cellules vivantes
que l'on veut en début de partie, puis elles sont placées de
façon aléatoire dans la grille (0 : cellule morte, 1 : vivante)
"""
nb = int(input("Nombre de cellules vivantes : "))
alive = []      #liste avec les rangs des cellules vivantes
for i in range(nb):
    el = (randint(0,cote-1),randint(0,cote-1))
    while el in alive :
        el = (randint(0,cote-1),randint(0,cote-1))
    alive.append(el)
#print(alive)

viv = []    #liste des instances de a classe Celulle
for cell in alive :
    cellule = Cellule(cell[0],cell[1],1)
    grille[cellule.x][cellule.y] = 1
    viv.append(cellule)
pprint(grille)

max_tour = 3
for i in range(max_tour):
    print("Tour n°",i+1)
    alive2 = []
    for cell in viv :
        if cell.etat == 1 :
            #print(cell.voisines())
            cnt = 0
            for v in cell.voisines():
                if grille[v[0]][v[1]] == 1 :
                    cnt = cnt + 1
            #print(cell.rang,":",cnt)
            if cnt == 3 :
                alive2.append(cell.rang)
    #print(len(alive2),"cellules vivantes au prochain tour :",alive2)
    print(len(alive2),"cellules vivantes au prochain tour")            
    print()
    grille = [[0 for i in range(cote)] for i in range(cote)]
    for cell in alive2 :
        cellule = Cellule(cell[0],cell[1],1)
        grille[cellule.x][cellule.y] = 1
        viv.append(cellule)
    pprint(grille)


