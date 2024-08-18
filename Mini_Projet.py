class Carre:
    """Initialisation des variables"""

    def __init__(self, nb1, nbc):
        self.nb1 = nb1
        self.nbc = nbc
        self.array = []

    """Initialiser toutes les variables du carre a 0"""

    def Array(self):
        self.array = [[0 for j in range(self.nb1)] for i in range(self.nbc)]

    """Afficher le carre en 2 dimensions"""

    def Afficher(self):
        for v in self.array:
            for i in v:
                print(i, end=" ")
            print()

    """Getters et Setters"""

    def getPosition(self, Pos1, Pos2):
        return self.array[Pos1][Pos2]

    def setPosition(self, Pos1, Pos2, value):
        self.array[Pos1][Pos2] = value
        return obj.array[Pos1][Pos2]

    """Verification de la somme en ligne et colone"""

    def sommeLigne(self, PosLigne):
        s = 0
        for v in self.array[PosLigne]:
            s += v
        return s

    def sommeColonne(self, PosColonne):
        s = 0
        for v in self.array:
            s += v[PosColonne]
        return s

    """Verification des diagonales principales et secondaires"""

    def sommeDiagonale(self):
        index = 0
        s = 0
        for v in self.array:
            s += v[index]
            index += 1
        return s

    """Regroupation de toutes les fonctions somme pour verifier si le carre est magique"""

    """Construction du carre magique"""

    def Solve(self):
        print("Construction du carree magique...")
        i, j = self.nb1, (self.nb1 + 1) // 2
        """Donner 1 dans le milieu du ligne 2"""
        self.array[i - 1][j - 1] = 1
        for k in range(2, self.nb1 ** 2 + 1):
            i2 = (i + 1) % self.nb1
            j2 = (j + 1) % self.nb1
            if self.array[i2 - 1][j2 - 1] == 0:
                i, j = i2, j2
            else:
                i = (i - 1) % self.nb1
            self.array[i - 1][j - 1] = k

    def Check(self):
        a = False
        j = 0
        for i in range(len(self.array)):
            if  (self.sommeLigne(i) == self.sommeLigne(j)) and (self.sommeLigne(j) == self.sommeColonne(i)) and (self.sommeColonne(i) == self.sommeColonne(j)) \
                    and (self.sommeColonne(j) == self.sommeDiagonale()) and (self.sommeDiagonale() == 15):
                a = True
            else:
                return "Le carree n'est pas magique"
        if (a == True):
            return "Le carree est magique"

"""Determination des dimensions et affichage du carre magique"""
obj = Carre(3, 3)
obj.Array()
obj.Solve()
obj.Afficher()
print(obj.Check())